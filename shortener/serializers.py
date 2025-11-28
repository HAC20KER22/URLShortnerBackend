from rest_framework import serializers
from .models import ShortURL
from .utils import generate_short_code

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["original_url"]
    

    def create(self,validated_data):
        user = self.context['request'].user
        code = generate_short_code()

        while ShortURL.objects.filter(short_code=code).exists():
            code = generate_short_code()
        
        return ShortURL.objects.create(
            user = user,
            original_url = validated_data['original_url'],
            short_code = code
        )
