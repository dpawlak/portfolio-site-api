from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('quickstart.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]