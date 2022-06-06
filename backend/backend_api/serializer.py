# from rest_framework import serializers
# from backend_api.models import Product

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     ref = serializers.CharField()
#     cost = serializers.FloatField()
#     price = serializers.FloatField()

#     def create(self, data):
#         return Product.objects.create(**data)

#     def update(self, instance, data):
#         instance.name = data.get('name', instance.name)
#         instance.ref = data.get('ref', instance.ref)
#         instance.cost = data.get('cost', instance.cost)
#         instance.price = data.get('price', instance.price)

#         instance.save()
#         return instance

from django.forms import ValidationError
from rest_framework import serializers
from backend_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def validate_name(self, data):
        if data["name"] == "Cannabis" | "Opium":
            raise ValidationError("Too bad, we only sell legalized crops")
        return data

    def get_description(self, data):
        return "This crop is called " + data.name + ", it costs $" + str(data.cost) + " and is sold for $" + (data.price)
