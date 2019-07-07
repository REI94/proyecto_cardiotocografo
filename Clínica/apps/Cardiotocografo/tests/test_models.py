from django.test import TestCase
from apps.Cardiotocografo.models import Historia

class HistoriaTestCase(TestCase):
    def setUp(self):
        Historia.objects.create(enfermedad_padecida="Fiebre", enfermedad_hereditarias="Ninguna")

    def test_enfermedad_padecida_label(self):
        historia = Historia.objects.get(codigo=1)        
        field_label_1 = historia._meta.get_field('enfermedad_padecida').verbose_name
        field_label_2 = historia._meta.get_field('enfermedad_hereditarias').verbose_name
        self.assertEqual(field_label_1, 'Enfermedad padecida')        
        self.assertEqual(field_label_2, 'Enfermedades hereditarias')

def test_enfermedad_padecida_length(self):
    historia = Historia.objects.get(codigo=1)
    max_length = historia._meta.get_field('enfermedad_padecida').max_length
    self.assertEqual(max_length, 200)

    def test_object_name_is_number_historia_plus_disease(self):
        historia = Historia.objects.get(codigo=1)
        expected_object_name = 'Historia Nro.: %s - %s'%(historia.codigo, historia.enfermedad_padecida)
        self.assertEqual(expected_object_name, str(historia))   

    def test_get_absolute_url(self):
        historia = Historia.objects.get(codigo=1)        
        self.assertEqual(historia.get_absolute_url(), 'historia/verHistoria/1')
