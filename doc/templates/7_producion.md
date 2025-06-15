# Fase de Producción

## Manual técnico e de administración

### Información relativa á instalación ou despregamento

A aplicación está desenvolvida en **Django** (Python) e emprega **SQLite** como base de datos por defecto.

#### Requisitos
- Python 3.13+
- Node.js (para compilar Tailwind vía django-tailwind)
- SQLite (incluído por defecto)
- Sistema operativo: Linux / Windows / MacOS

#### Configuración inicial de seguridade
- O acceso á app require rexistro e autenticación.
- As vistas están protexidas para que cada usuario só vexa os seus datos.

#### Carga inicial de datos
- Existe opción de importar os datos ou directamente vía formulario web.
- Pódese preparar un script para converter CSV/Excel a modelos Django.

#### Alta de usuarios
- Cada usuario pode rexistrarse libremente.
- O administrador pode crear contas desde o panel admin (`/admin`).

---

### Administración do sistema

#### Copias de seguridade
- Base de datos SQLite pódese copiar directamente como ficheiro (`db.sqlite3`).

#### Xestión de usuarios
- A xestión faise desde o panel de administración.

#### Xestión de seguridade
- Acceso mediante login e control de sesión.
- Validación de formularios e permisos por usuario.

---

### Mantemento do sistema

#### Corrección de erros e melloras
- O proxecto utiliza control de versións (Git).
- As incidencias detectadas serán rexistradas nun sistema tipo Trello, GitHub Issues ou similar.
- Cada erro será revisado e asignado para a súa resolución.

#### Xestión de incidencias
- Os usuarios poderán comunicar erros vía formulario de contacto.
- As respostas daranse nun prazo razoable dependendo da gravidade.

---

## Manual de usuario

### Formación de usuarios
A aplicación é sinxela e intuitiva, non require formación previa.

### Instrucións iniciais
1. Rexístrate na aplicación.
2. Accede ao panel de vocabulario.
3. Engade palabras con significado, pinyin, nivel HSK e exemplo.
4. Utiliza os filtros para revisar o teu vocabulario.
5. Practica co asistente IA dende a sección de "Chat".

---

## FAQ (Preguntas frecuentes)

- **Podo usar a app sen rexistrarme?**  
  Non, é preciso crear unha conta para gardar o teu vocabulario personalizado.

- **Podo ver o vocabulario doutros usuarios?**  
  Non, cada usuario só pode acceder aos seus propios datos.

- **Como exporto os meus datos?**  
  Desde a sección "Ver palabras" tes un botón de exportación.

- **Funciona no móbil?**  
  Si, a aplicación está adaptada a dispositivos móbiles.

---

## Protección de datos de carácter persoal

- A aplicación almacena nomes de usuario e correos electrónicos cifrados mediante os mecanismos internos de Django.
- Os datos non se comparten nin se usan para fins comerciais.
- Cada usuario pode solicitar a eliminación da súa conta e datos asociados.
- A base de datos está protexida e accesible só desde o backend da aplicación.

## Licencia

```text
GNU General Public License v3.0
Copyright (c) 2025 Víctor Iglesias

Este proxecto está baixo a licenza GNU General Public License v3.0.
Podes usalo, modificalo e compartilo libremente, sempre que manteñas esta licenza.

Consulta o ficheiro LICENSE para máis información.
```