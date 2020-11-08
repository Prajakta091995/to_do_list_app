"""to_do_app URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),  # Comment, if you are using custom user

    #url to run url from user model
    path('api/', include('user.urls')),
    #url to run url from to_do_logic
    path('api/to_do_list/',include('to_do_logic.urls')),
    ]