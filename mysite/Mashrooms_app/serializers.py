from rest_framework import serializers
from .models import MashroomsPrediction


class MashroomsPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MashroomsPrediction
        fields=['cap_surface','bruises','gill_attachment','gill_spacing','gill_size','gill_color',
                'stalk_shape','stalk_root','stalk_surface_above_ring',
                'stalk_surface_below_ring','stalk_color_above_ring','stalk_color_below_ring',
                'veil_color','ring_number','ring_type','spore_print_color','population','habitat']
