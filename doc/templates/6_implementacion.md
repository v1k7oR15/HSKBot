# Fase de implementación

Durante esta fase desenvolvéronse as funcionalidades principais do sistema, estruturando o código nunha aplicación Django integrada con Tailwind CSS para un deseño moderno e responsivo. A implementación inclúe xestión de usuarios, almacenamento de vocabulario chinés, chat con IA, filtros e visualización personalizada dos datos.

---

## Estructura do proxecto

- **Backend**: Django 5
- **Frontend**: Tailwind CSS via `django-tailwind`
- **Base de datos**: SQLite
- **IA**: DeepSeek API (modelo `deepseek-chat`)
- **Outros**: Django Tables2, Django Filters, OpenAI

---

## Configuración do entorno

- **IDE**: Visual Studio Code
- **Librerías principais** (ver `requirements.txt`):
  - `django`
  - `django-tailwind`
  - `django-filter`
  - `django-tables2`
  - `openai`

---

## Arquitectura e implementación

- `views.py`: Define as vistas principais (`chat`, `login`, `registro`, `palabra`, `mostrar_palabras`) e a lógica de interacción coa IA.
- `models.py`: Contén o modelo `Palabra`, que representa o vocabulario dos usuarios, co campo `ForeignKey` ao modelo `User`.
```python
class Palabra(models.Model):
    TIPO_CHOICES = (
        ('S', 'Sustantivo'),
        ('V', 'Verbo'),
        ('A', 'Adjetivo'),
        ('AD', 'Adverbio'),
        ('P', 'Pronombre'),
        ('C', 'Conjunción'),
        ('I', 'Interjección'),
        ('D', 'Determinante'),
        ('N', 'Numeral'),
        ('O', 'Otro'),
    )
    palabra = models.CharField("Vocabulario en chino", max_length=10, db_index=True)
    pinyin = models.CharField(max_length=10)
    traduccion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, db_index=True)
    nivel_hsk = models.SmallIntegerField(default=1, null=True, blank=True ,db_index=True)
    ejemplo = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vocabulario')

    class Meta:
        unique_together = ('palabra', 'pinyin', 'tipo', 'nivel_hsk', 'usuario')
        ordering = ['nivel_hsk', 'tipo', 'palabra']

    def __str__(self):
        return f"{self.palabra} ({self.usuario.username})"
```
- `forms.py`: Formulario personalizado para introducir novas palabras, login e rexistro.
- `tables.py`: Usa Django Tables2 para mostrar os datos en táboas HTML estilizadas.
- `filter.py`: Permite filtrar o vocabulario por tipo, nivel HSK e outros criterios.
- `base.html`: Plantilla base con header, sidebar e main content, construído con Tailwind e bloques de Django templates.

---

## Funcionalidades destacadas

- **Login e Rexistro**: Sistema de autenticación simple con formularios propios e xestión de sesión.
- **Chat IA**: Interface de chat que conserva o historial e responde mediante a API de DeepSeek.
- **Xestión de palabras**:
  - Engadir palabras con comprobación de duplicados.
  - Mostrar e filtrar vocabulario.
  - Asociar palabras a cada usuario.
- **Estilo responsivo**: Tailwind permite que a web se adapte a móbil e tablet.
- **Panel lateral (Sidebar)**: Navegación clara entre as seccións principais da aplicación.

---

## Observacións

- A implementación completouse con éxito e pódese executar localmente sen configuración complexa.
- A integración con DeepSeek require unha API Key configurada en `settings.py`.
- As chamadas á IA están controladas para evitar uso indebido.