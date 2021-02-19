from rest_framework.generics import RetrieveAPIView

from .models import ServiceCategory
from .serializers import ServiceCategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    context_object_name = 'category'
    serializer_class = ServiceCategorySerializer
    queryset = ServiceCategory.objects.all()

