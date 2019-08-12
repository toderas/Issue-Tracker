from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import bug_item, BugComment, Like, Views
from .forms import AddBugForm, AddCommentForm

# Create your views here.
def get_bugs(request):
    bugs = bug_item.objects.filter().order_by('-date_reported')
    page = request.GET.get('page', 1)

    paginator = Paginator(bugs, 5)
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)
    return render(request, "bugs.html", {"bugs": bugs})


@login_required()
def add_new_bug(request):
    """
    Renders AddBugForm saves its contents and returns to main page 
    """
    if request.method == 'POST':
        item_form = AddBugForm(request.POST)
        if item_form.is_valid():
            bug = item_form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect(get_bugs)
    else:
        item_form = AddBugForm()
    return render(request, 'new-bug.html', {"item_form": item_form})


@login_required
def get_current_bug(request, id):
    """
    Displays single item and related comments with option to insert new comment
    Checks whether user viewed item and if not adds 1 to views
    """
    bug = get_object_or_404(bug_item, id=id)
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = bug
            comment.author = request.user
            comment.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        comment_form = AddCommentForm()
    
    comment = BugComment.objects.filter(post_id=bug.id).order_by('-date_reported')
    views = Views.objects.filter(user=request.user, post_id=bug).count()
    if views < 1:
        Views.objects.create(user=request.user, post_id=bug.id)

    like = Like.objects.filter(post_id=bug.id).count()
    view = Views.objects.filter(post_id=bug.id).count()
    print(view)
    page = request.GET.get('page', 1)
    paginator = Paginator(comment, 5)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        comment = paginator.page(1)
    except EmptyPage:
        comment = paginator.page(paginator.num_pages)
    comment_form = AddCommentForm()
    return render(request, 'bug-details.html', {'bug': bug, 'comment': comment, 'comment_form': comment_form, 'like': like, 'view': view})
    
    
def remove_comment(request, BugComment_id):
    """
    Removes comment and returns to the same page 
    """
    comment = get_object_or_404(BugComment, pk=BugComment_id)
    print(comment)
    comment.delete()
    messages.error(request, "Comment has been removed")
    return redirect(request.META['HTTP_REFERER'])
    


def add_upvotes(request, id):
    """ Allows user to upvote an item and limits the number of likes to 1 """
    post = get_object_or_404(bug_item, id=id)
    upvotes = Like.objects.filter(user=request.user, post=post).count()
    if upvotes > 0:
        messages.error(request, 'You Already liked this post!')
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect(request.META['HTTP_REFERER'])
    
    
def delete_bug(request, id):
    """ Deletes the item and all related information (comments, likes and views)"""
    items = get_object_or_404(bug_item, id=id)
    items.delete()
    messages.success(request, "Item has been successfully removed!")
    return redirect(get_bugs)