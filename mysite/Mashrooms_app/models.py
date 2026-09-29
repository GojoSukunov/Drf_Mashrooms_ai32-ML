from django.db import models

class MashroomsPrediction(models.Model):
    cap_surface=models.CharField(max_length=32)
    bruises=models.CharField(max_length=32)
    gill_attachment=models.CharField(max_length=32)
    gill_spacing=models.CharField(max_length=32)
    gill_size=models.CharField(max_length=32)
    gill_color=models.CharField(max_length=32)
    stalk_shape=models.CharField(max_length=32)
    stalk_root=models.CharField(max_length=32)
    stalk_surface_above_ring=models.CharField(max_length=32)
    stalk_surface_below_ring=models.CharField(max_length=32)
    stalk_color_above_ring=models.CharField(max_length=32)
    stalk_color_below_ring=models.CharField(max_length=32)
    veil_color=models.CharField(max_length=32)
    ring_number=models.CharField(max_length=32)
    ring_type=models.CharField(max_length=32)
    spore_print_color=models.CharField(max_length=32)
    population=models.CharField(max_length=32)
    habitat=models.CharField(max_length=32)

    prediction=models.PositiveSmallIntegerField(default=0)
