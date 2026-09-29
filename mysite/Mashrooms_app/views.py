from pathlib import Path

import joblib
from rest_framework import views
from rest_framework.response import Response

from .serializers import MashroomsPredictionSerializer
from . import serializers
from rest_framework import status


base_dir=Path(__file__).resolve().parent.parent
path_model=base_dir/'model'/'mashrooms_model_2_ai32 (2)'

model=joblib.load(path_model)


cap_surface_list=['g','s','y']
gill_color_list=['e','g','h','k','n','o','p','r','u','w','y']
stalk_root_list=['b','c','e','r']
stalk_surface_above_ring_list=['k','s','y']
stalk_surface_below_ring_list=['k','s','y']
stalk_color_above_ring_list=['c','e','g','n','o','p','w','y']
stalk_color_below_ring_list=['c','e','g','n','o','p','w','y']
veil_color_list=['o','w','y']
ring_number_list=['o','t']
ring_type_list=['f','l','n','p']
spore_print_color_list=['h','k','n','o','r','u','w','y']
population_list=['c','n','s','v','y']
habitat_list=['g','l','m','p','u','w']

class MashroomsPredictionViewSet(views.APIView):
    def post(self,request):
        instance=serializers.MashroomsPredictionSerializer(data=self.request.data)
        if instance.is_valid():
            original_data = instance.validated_data.copy()
            data = instance.validated_data.copy()
            new_cap_surface = data.pop('cap_surface')
            cap_surface_0_1 = [1 if i == new_cap_surface else 0 for i in cap_surface_list]
            new_bruises = data.pop('bruises')
            bruises_0_1 = [1 if new_bruises == 't' else 0]
            new_gill_attachment = data.pop('gill_attachment')
            gill_attachment_0_1 = [1 if new_gill_attachment == 'f' else 0]
            new_gill_spacing = data.pop('gill_spacing')
            gill_spacing_0_1 = [1 if new_gill_spacing == 'w' else 0]
            new_gill_size = data.pop('gill_size')
            gill_size_0_1 = [1 if new_gill_size == 'n' else 0]
            new_gill_color = data.pop('gill_color')
            gill_color_0_1 = [1 if i == new_gill_color else 0 for i in gill_color_list]
            new_stalk_shape = data.pop('stalk_shape')
            stalk_shape_0_1 = [1 if new_stalk_shape == 't' else 0]
            new_stalk_root = data.pop('stalk_root')
            stalk_root_0_1 = [1 if i == new_stalk_root else 0 for i in stalk_root_list]
            new_stalk_surface_above_ring = data.pop('stalk_surface_above_ring')
            stalk_surface_above_ring_0_1 = [1 if i == new_stalk_surface_above_ring else 0 for i in
                                        stalk_surface_above_ring_list]
            new_stalk_surface_below_ring = data.pop('stalk_surface_below_ring')
            stalk_surface_below_ring_0_1 = [1 if i == new_stalk_surface_below_ring else 0 for i in
                                        stalk_surface_below_ring_list]
            new_stalk_color_above_ring = data.pop('stalk_color_above_ring')
            stalk_color_above_ring_0_1 = [1 if i == new_stalk_color_above_ring else 0 for i in stalk_color_above_ring_list]
            new_stalk_color_below_ring = data.pop('stalk_color_below_ring')
            stalk_color_below_ring_0_1 = [1 if i == new_stalk_color_below_ring else 0 for i in stalk_color_below_ring_list]
            new_veil_color = data.pop('veil_color')
            veil_color_0_1 = [1 if i == new_veil_color else 0 for i in veil_color_list]
            new_ring_number = data.pop('ring_number')
            ring_number_0_1 = [1 if i == new_ring_number else 0 for i in ring_number_list]
            new_ring_type = data.pop('ring_type')
            ring_type_0_1 = [1 if i == new_ring_type else 0 for i in ring_type_list]
            new_spore_print_color = data.pop('spore_print_color')
            spore_print_color_0_1 = [1 if i == new_spore_print_color else 0 for i in spore_print_color_list]
            new_population = data.pop('population')
            population_0_1 = [1 if i == new_population else 0 for i in population_list]
            new_habitat = data.pop('habitat')
            habitat_0_1 = [1 if i == new_habitat else 0 for i in habitat_list]

            features = (cap_surface_0_1 + bruises_0_1
                    + gill_attachment_0_1 + gill_spacing_0_1
                    + gill_size_0_1 + gill_color_0_1 + stalk_shape_0_1 +
                    stalk_root_0_1 + stalk_surface_above_ring_0_1 + stalk_surface_below_ring_0_1 +
                    stalk_color_above_ring_0_1 + stalk_color_below_ring_0_1 + veil_color_0_1 + ring_number_0_1 +
                    ring_type_0_1 + spore_print_color_0_1 + population_0_1 + habitat_0_1)
            predict=int(model.predict([features])[0])
            mashrooms=instance.save(**original_data,prediction=predict)
            return Response({'mashrooms_prediction':predict,'data':MashroomsPredictionSerializer(mashrooms).data},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)