from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return round(rate, 1)
        return None
        # reviews=obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars
       
        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 1)
        # return None

    def validate_resume(self, value):
        if len(value)>200:
            raise serializers.ValidationError('Resumo nao deve ser maior que 200 caracteres.')
        return value