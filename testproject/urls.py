"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework import routers

# from core import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include([
        path('products/', include('product.urls', namespace='product'))
    ]))
]

# TODO
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ]
