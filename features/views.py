from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Feature
from .forms import AddFeatureForm

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