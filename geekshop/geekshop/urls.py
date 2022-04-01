from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

<<<<<<< HEAD
=======
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

>>>>>>> acd770417932e8546621d2347c271fd85985426b
from mainapp import views as mainapp

urlpatterns = [
<<<<<<< HEAD
    path("", include("social_django.urls", namespace="social")),
    path("admin/", include("adminapp.urls", namespace="admin")),
=======
    path("admin/", admin.site.urls),
>>>>>>> acd770417932e8546621d2347c271fd85985426b
    path("", mainapp.index, name="main"),
    path("contact/", mainapp.contact, name="contact"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("auth/", include("authapp.urls", namespace="auth")),
<<<<<<< HEAD
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("orders/", include("ordersapp.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> acd770417932e8546621d2347c271fd85985426b
