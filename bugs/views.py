from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import bug_item, BugComment
from .forms import AddBugForm, AddCommentForm

# Create your views here.
def get_bugs(request):
    bugs = bug_item.objects.filter().order_by('-date_reported')
    return render(request, "bugs.html", {"bugs": bugs})
    
@login_required()
def add_new_bug(request):
    """
    Renders AddBugForm saves its contents and returns to main page (user dependant yet to be implemented)
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
#

#
def get_current_bug(request, id):
    bug = get_object_or_404(bug_item, id=id)
    print(bug)
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = bug
            comment.author = request.user
            comment.save()
            print(comment)
           # return render(request, 'bug-details.html', {'bug': bug, 'comment': comment, 'comment_form': comment_form})

    else:
        comment_form = AddCommentForm()
        print(comment_form)
    comment = BugComment.objects.filter(post_id=bug.id).order_by('-date_reported')
    print(comment)
    comment_form = AddCommentForm()
    
    return render(request, 'bug-details.html', {'bug': bug, 'comment': comment, 'comment_form': comment_form})
    
