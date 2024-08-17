"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# add so we can get access to images in django
from django.conf.urls.static import static  # so , static files can be read
from django.conf import settings

# added for the Rest Api
from django.urls import include
from rest_framework import routers
# "movies" here is a name to the path's APP (directory called movies)
from movies.views import MovieViewset, ActionViewSet,ComedyViewSet

#router = routers.DefaultRouter() # this router was used before starting coding end points
# we move from DefaultRouter() to SimpleRouter()  because of end Points
router = routers.SimpleRouter()
# "movies" here represents the path (via browser) to the Api
router.register('movies', MovieViewset, basename='movies')
# "movies" here represents the path (via browser) to the Api
router.register('action',ActionViewSet,basename='action')  # with more than two routes, "basename" becomes mandatory
router.register('comedy',ComedyViewSet,basename='comedy')  # with more than two routes, "basename" becomes mandatory

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
