import pdb

from rest_framework import serializers

# from core.serializers import UserInlineSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # user = UserInlineSerializer()
    # user_id = Serializers

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'user_id', ]

    def validate_title(self, value):
        if len(value) > 5 and value[2] != 'a':
            return value
        raise serializers.ValidationError('vlsdkdsad')


    # def validate(self, data):
    #     if data['title']
    #     if data['descriptipn']

    def create(self, request, args): # or update
        pdb.set_trace()
        # validated_data['description'] = f'description: {description}'
        # return self.meta.model.objects.create(**self.validated_data)
