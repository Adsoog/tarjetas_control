# forms.py
from django import forms
from .models import TarjetaDiaria
from modelos.models import Tarea  # Asegúrate de importar los modelos necesarios
from django.db import transaction

class TarjetaDiariaForm(forms.ModelForm):
    tareas = forms.ModelMultipleChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tareas'
    )

    class Meta:
        model = TarjetaDiaria
        fields = ['fecha', 'tareas', 'total_minutos', 'duracion_jornada']
        widgets = {
            'total_minutos': forms.NumberInput(attrs={'readonly': True}),
            'duracion_jornada': forms.Select()
        }

    def save_m2m(self):
        super(TarjetaDiariaForm, self).save_m2m()
        self.instance.total_minutos = self.instance.calcular_total_minutos()
        self.instance.save()

    def save(self, commit=True):
        with transaction.atomic():
            tarjeta_diaria = super(TarjetaDiariaForm, self).save(commit=False)
            if commit:
                tarjeta_diaria.save()
                self.save_m2m()  # Guarda las relaciones ManyToMany
                tarjeta_diaria.total_minutos = tarjeta_diaria.calcular_total_minutos()
                tarjeta_diaria.save()  # Guarda nuevamente con el total actualizado
            return tarjeta_diaria
