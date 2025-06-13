# Fase de implementación

Durante esta fase desenvolvéronse as funcionalidades principais do sistema, estruturando o código nunha aplicación Django integrada con Tailwind CSS para un deseño moderno e responsivo. A implementación inclúe xestión de usuarios, almacenamento de vocabulario chinés, chat con IA, filtros e visualización personalizada dos datos.

---

## Estructura do proxecto

- **Backend**: Django 5
- **Frontend**: Tailwind CSS via `django-tailwind`
- **Base de datos**: SQLite
- **IA**: DeepSeek API (modelo `deepseek-chat`)

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

### `models.py`

Define os modelos **`Tipo`** e **`Palabra`**.
```python
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2, unique=True)
    color = models.CharField(max_length=7, default='#FFFFFF')  # Color en formato hexadecimal

    def __str__(self):
        return self.nombre

class Palabra(models.Model):
    palabra = models.CharField("Vocabulario en chino", max_length=10, db_index=True)
    pinyin = models.CharField(max_length=10)
    traduccion = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name='palabras', db_index=True)
    nivel_hsk = models.SmallIntegerField(default=1, null=True, blank=True ,db_index=True)
    ejemplo = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vocabulario')

    class Meta:
        unique_together = ('palabra', 'pinyin', 'tipo', 'nivel_hsk', 'usuario')
        ordering = ['nivel_hsk', 'tipo', 'palabra']

    def __str__(self):
        return f"{self.palabra} ({self.usuario.username})"
```

### `forms.py`

Inclúe tres formularios:

- `RegistroForm`: Rexistro con dobre contrasinal e validación.
- `LoginForm`: Login por email.
- `PalabraForm`: Entrada de vocabulario.

```python
class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class PalabraForm(forms.ModelForm):
    palabra = forms.CharField(label='Vocabulario en chino', max_length=10)
    pinyin = forms.CharField(label='Pinyin', max_length=10)
    traduccion = forms.CharField(label='Traducción', max_length=100)
    tipo = forms.ModelChoiceField(
        label='Tipo',
        queryset=Tipo.objects.all(),
        empty_label="Selecciona un tipo"
    )
    nivel_hsk = forms.IntegerField(label='Nivel HSK', min_value=1, max_value=6, required=False)
    ejemplo = forms.CharField(label='Ejemplo', widget=forms.Textarea, required=False)

    class Meta:
        model = Palabra
        fields = ['palabra', 'pinyin', 'traduccion', 'tipo', 'nivel_hsk', 'ejemplo']
```
### `views.py`

Contén toda a lóxica de negocio:

#### 1. **Login e rexistro**
- Autenticación manual con `request.session.set_expiry()` para "lembrar sesión".

```python
def login_view(request):
    form = LoginForm(request.POST or None)
    error = None
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = request.POST.get('remember_me')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    if remember_me:
                        # 30 días (en segundos)
                        request.session.set_expiry(2592000)
                    else:
                        # Sesión expira al cerrar el navegador
                        request.session.set_expiry(0)
                    return redirect('inicio')
                else:
                    error = "Correo o contraseña incorrectos"
            except User.DoesNotExist:
                error = "Correo o contraseña incorrectos"
    return render(request, 'login.html', {'form': form, 'error': error})

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})
```

#### 2. **Xestión de vocabulario**
- Crear, editar, eliminar e filtrar palabras por usuario.

```python
@login_required
def palabra_view(request):
    error = None
    if request.method == 'POST':
        form = PalabraForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            existe = Palabra.objects.filter(
                palabra=datos['palabra'],
                pinyin=datos['pinyin'],
                tipo=datos['tipo'],
                nivel_hsk=datos.get('nivel_hsk', 1),
                usuario=request.user
            ).exists()
            if existe:
                error = "¡Esa palabra ya existe con esos datos!"
            else:
                try:
                    Palabra.objects.create(
                        palabra=datos['palabra'],
                        pinyin=datos['pinyin'],
                        traduccion=datos['traduccion'],
                        tipo=datos['tipo'],
                        nivel_hsk=datos.get('nivel_hsk', 1),
                        ejemplo=datos.get('ejemplo', ''),
                        usuario=request.user
                    )
                    return redirect('palabra')
                except IntegrityError:
                    error = "¡Esa palabra ya existe!"
    else:
        form = PalabraForm()

    return render(request, 'palabra.html', {
        'form': form,
        'error': error
    })

@login_required
def mostrar_palabras_view(request):
    palabra_filter = PalabraFilter(request.GET, queryset=Palabra.objects.filter(usuario=request.user))
    table = PalabraTable(palabra_filter.qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(request, 'mostrar_palabras.html', {
        'table': table,
        'user': request.user,
        'filter': PalabraFilter(request.GET, queryset=Palabra.objects.filter(usuario=request.user)),
    })

def eliminar_palabra_view(request, pk):
    palabra = get_object_or_404(Palabra, pk=pk, usuario=request.user)
    palabra.delete()
    return redirect('mostrar_palabras')

def editar_palabra_view(request, pk):
    palabra = get_object_or_404(Palabra, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = PalabraForm(request.POST, instance=palabra)
        if form.is_valid():
            form.save()
            return redirect('mostrar_palabras')
    else:
        form = PalabraForm(instance=palabra)

    return render(request, 'palabra.html', {
        'form': form,
        'editar': True,
    })
```

#### 3. **Chat con IA (DeepSeek)**

- Gárdase o historial da conversa na sesión.
- Chámase a `ai_message()` con cada nova mensaxe do usuario.

```python
def chat_view(request):
    mensajes = request.session.get('mensajes', [])

    if request.method == 'POST':
        user_message = request.POST.get('mensaje')
        if user_message:
            mensajes.append({"role": "user", "content": user_message})
            respuesta = ai_message(user_message)
            mensajes.append({"role": "assistant", "content": respuesta})
        request.session['mensajes'] = mensajes

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('chat_messages.html', {'mensajes': mensajes}, request=request)
        return JsonResponse({'html': html})
    return render(request, 'chat.html', {'mensajes': mensajes})
```

### 📄 `filter.py`

Define `PalabraFilter` con `django-filters`, permitindo filtrar por varios campos.

´´´python
class PalabraFilter(django_filters.FilterSet):
    class Meta:
        model = Palabra
        fields = ['palabra', 'pinyin', 'traduccion', 'tipo', 'nivel_hsk']

´´´

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