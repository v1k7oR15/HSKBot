import django_tables2 as tables
from .models import Palabra

class PalabraTable(tables.Table):
    acciones = tables.TemplateColumn(
        template_code="""
        <a href="{% url 'eliminar_palabra' record.pk %}"
            class="bg-red-500 hover:bg-red-600 px-3 py-1 rounded-md text-sm transition font-bold"
            onclick="return confirm('¿Estás seguro de que quieres eliminar esta palabra?');"
            title="Eliminar palabra">
            Eliminar
        </a>
        <a href="{% url 'editar_palabra' record.pk %}"
            class="bg-yellow-500 ml-2 hover:bg-yellow-600 px-3 py-1 rounded-md text-sm transition font-bold mr-2"
            title="Editar palabra">
            Editar
        </a>
        """,
        orderable = False,
        verbose_name="Acciones"
    )

    class Meta:
        model = Palabra
        template_name = "django_tables2/tailwind.html"
        fields = ("palabra", "pinyin", "traduccion", "tipo", "nivel_hsk", "ejemplo")
        sequence = ("palabra", "pinyin", "traduccion", "tipo", "nivel_hsk", "ejemplo", "acciones")
        empty_text = "No hay palabras registradas"
