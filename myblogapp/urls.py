from .views import PostViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('post',PostViews)

urlpatterns = router.urls

