import django_tables2 as tables
from .models import Palabra

class PalabraTable(tables.Table):
    class Meta:
        model = Palabra
        template_name = "django_tables2/tailwind.html"
        fields = ("palabra", "pinyin", "traduccion", "tipo", "nivel_hsk", "ejemplo")
        empty_text = "No hay palabras registradas"
