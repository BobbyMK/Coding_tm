from rest_framework import generics

from response.models import FoodCategory
from response.serializers import FoodListSerializer

class FoodCategoryListAPIView(generics.ListAPIView):

    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(food__is_publish=True).distinct()
