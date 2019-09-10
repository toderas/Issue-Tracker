from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Feature, FeatureContributors, FeatureViews
from .forms import AddFeatureForm, ContributeFeatureForm


# Create your views here.
def all_features(request):
    """ Returns all registered features and displays 5 per page  """
    features = Feature.objects.filter().order_by('-date_reported')
    count = features.count()
    contributors = FeatureContributors.objects.all()
    views = FeatureViews.objects.all()
    for feature in features:
        feature.contributors = contributors.filter(post=feature.pk).count()
        feature.views = views.filter(post=feature.pk).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(features, 5)
    try:
        features = paginator.page(page)
    except PageNotAnInteger:
        features = paginator.page(1)
    except EmptyPage:
        features = paginator.page(paginator.num_pages)
    return render(request, "features.html", {"features": features, 'count': count})
    

@login_required()
def add_new_feature(request):
    """
    Renders AddFeatureForm saves its contents and returns to main page 
    """
    if request.method == 'POST':
        feature_form = AddFeatureForm(request.POST)
        if feature_form.is_valid():
            feature = feature_form.save(commit=False)
            feature.author = request.user
            feature.save()
            return redirect(all_features)
    else:
        feature_form = AddFeatureForm()
    return render(request, 'request-feature.html', {"feature_form": feature_form})
    
@login_required
def get_current_feature(request, id):
    """
    Displays single item  with option to contribute with desired amount
    """
    feature = get_object_or_404(Feature, id=id)
    if feature.value_collected >= feature.target_value:
        progress = 100
        remaining = 0
    elif feature.target_value > 0:
        progress = int(feature.value_collected) / int(feature.target_value) * 100
        remaining = int(feature.target_value) - int(feature.value_collected)
    else:
        progress = 0
        remaining = 0
    if request.method == 'POST':
        contribute_form = ContributeFeatureForm(request.POST)
        if contribute_form.is_valid():
            amount = contribute_form.save(commit=False)
            amount.post = feature
            amount.author = request.user
            amount.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        contribute_form = ContributeFeatureForm()
    views = FeatureViews.objects.filter(post_id=feature).count()
    if views < 1:
        FeatureViews.objects.create(user=request.user, post_id=feature.id)
        feature.save()
    contributors = FeatureContributors.objects.filter(post_id=feature.id).count()
    contributor = FeatureContributors.objects.filter(post=feature.id).order_by('-date_contributed')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(contributor, 9)
    try:
        contributor = paginator.page(page)
    except PageNotAnInteger:
        contributor = paginator.page(1)
    except EmptyPage:
        contributor = paginator.page(paginator.num_pages)
    return render(request, 'feature-details.html', {'feature': feature, 'contribute_form': contribute_form, 'contributor': contributor, 'contributors': contributors, 'remaining': remaining, 'progress': progress, 'views': views})

