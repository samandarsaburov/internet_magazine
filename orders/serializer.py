from rest_framework.serializers import ModelSerializer
from .models import OrderModel

class OrderSerializer(ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('id','name','tel','yashash_joyi','order_name','create_at')