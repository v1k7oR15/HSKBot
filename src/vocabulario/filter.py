import django_filters
from .models import Palabra

class PalabraFilter(django_filters.FilterSet):
    class Meta:
        model = Palabra
        fields = ['palabra', 'pinyin', 'traduccion', 'tipo', 'nivel_hsk']
