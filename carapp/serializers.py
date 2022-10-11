from rest_framework import serializers
from . models import carlist
class carlistSerializer(serializers.ModelSerializer):
	class Meta:
		model = carlist
		fields = '__all__'

		