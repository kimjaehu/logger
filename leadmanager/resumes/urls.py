from rest_framework import routers
from .api import ResumeViewSet

router = routers.DefaultRouter()
router.register('api/resumes', ResumeViewSet, 'resumes')

urlpatterns = router.urls
