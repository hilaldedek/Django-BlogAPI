from django.urls import path, include
from .views import UserView
from rest_framework.routers import DefaultRouter
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message":'User Logout : token deleted'})


router=DefaultRouter()

router.register('',UserView)

urlpatterns = [
    path('',include(router.urls)),
    path('login',obtain_auth_token),
    path('logout',logout),
]
