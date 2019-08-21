from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Feature
from .forms import AddFeatureForm, ContributeFeatureForm


# Create your views here.
def all_features(request):
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})
    

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
    if feature.target_value == feature.value_collected:
        progress = 100.0
    try:
        progress = (abs(int(feature.value_collected)) / int(feature.target_value)) * 100.0
        remaining = (abs(int(feature.target_value)) - int(feature.value_collected))
    except ZeroDivisionError:
        progress = 0
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
    
    return render(request, 'feature-details.html', {'feature': feature, 'contribute_form': contribute_form, 'progress': progress, 'remaining': remaining})
    