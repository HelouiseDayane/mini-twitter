from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from posts.views import PostCreateView  
from users.views import UserCreateView 
from users.views import UserLoginView 

schema_view = get_schema_view(
   openapi.Info(
      title="Mini Twitter API",
      default_version='v1',
      description="API para Mini-Twitter com Django",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="helouisedayane@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('api/posts/', include('posts.urls')),  
    path('api/users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
