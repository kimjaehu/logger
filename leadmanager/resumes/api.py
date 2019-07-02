from resumes.models import Resume
from rest_framework import viewsets, permissions
from .serializers import ResumeSerializer

# Resume Viewset


class ResumeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return self.request.user.resumes.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
