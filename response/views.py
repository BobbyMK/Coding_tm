from rest_framework import generics
from django.db.models import Prefetch

from response.models import FoodCategory, Food
from response.serializers import FoodListSerializer

class FoodCategoryListAPIView(generics.ListAPIView):

    serializer_class = FoodListSerializer
    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).distinct().prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )
        print(queryset.query)
        return queryset



