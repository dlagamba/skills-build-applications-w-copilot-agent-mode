"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
# Redirect root to /api/info/
def root_redirect(request):
    return HttpResponseRedirect('/api/info/')
from . import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

# API root info endpoint
def api_root_info(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        # fallback to localhost for local dev
        api_url = "http://localhost:8000/api/"
    return JsonResponse({
        "api_base_url": api_url,
        "docs": f"{api_url}"
    })



urlpatterns = [
    path('', root_redirect),
    path('admin/', admin.site.urls),
    path('api/info/', api_root_info, name='api-root-info'),
    path('api/', include(router.urls)),
]
