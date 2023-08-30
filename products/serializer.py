from rest_framework.serializers import ModelSerializer
from .models import ProductsModel

class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = ProductsModel
        fields = ('id','title','description','price','category','image','create_at')