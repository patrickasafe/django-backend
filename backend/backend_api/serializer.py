from rest_framework import serializers
from backend_api.models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    ref = serializers.CharField()
    cost = serializers.FloatField()
    price = serializers.FloatField()

    def create(self, data):
        return Product.objects.create(**data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.ref = data.get('ref', instance.ref)
        instance.cost = data.get('cost', instance.cost)
        instance.price = data.get('price', instance.price)
