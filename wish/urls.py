
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from wishapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish/signup/', views.signup, name="signup"),
    path('wish/signin/',views.signin,name="signin"),
    path('wish/signout', views.signout,name="signout"),
    path('wish/',views.landing,name="landing"),
    path('wish/list/',views.list,name="list"),
    path('wish/create/',views.list_create,name="wish-create"),
    path('wish/delete/<int:wish_id>', views.list_delete, name="wish-delete")

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
