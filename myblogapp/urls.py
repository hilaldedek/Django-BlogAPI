from .views import PostViews,CategoryViews
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('post',PostViews)
router.register('category',CategoryViews)

urlpatterns = router.urls

