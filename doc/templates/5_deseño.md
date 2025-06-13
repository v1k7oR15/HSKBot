# DESEÑO

## Deseño do proxecto

### Modelo conceptual do dominio da aplicación e/ou Diagrama de clases.

<img src="doc/img/UML.svg" alt="Diagrama UML" />

### Casos de uso.

| ID   | Nome                | Actor   | Descrición                                                 |
|------|---------------------|---------|-------------------------------------------------------------|
| CU01 | Iniciar sesión      | Usuario | O usuario entra no sistema coa súa conta                    |
| CU02 | Engadir palabra     | Usuario | O usuario crea unha palabra e a IA completa os datos        |
| CU03 | Usar chat IA        | Usuario | O usuario conversa co asistente virtual integrado           |
| CU04 | Exportar listas     | Usuario | Pode descargar as súas palabras en PDF/XLSX                 |

### Deseño de interfaces de usuarios.

- A pantalla principal presenta unha barra lateral con navegación sinxela, filtros por categoría e nivel HSK, e unha táboa central de palabras. Inclúe tamén un buscador e botón para engadir novo vocabulario.

- O chat mostra mensaxes diferenciadas entre usuario e asistente virtual, cun deseño tipo burbulla, entrada de texto na parte inferior e botón de envío. Mantén o estilo escuro da aplicación.

- A pantalla de login ofrece un formulario centrado e limpo, sen elementos adicionais como menú ou chat, pensado para facilitar o acceso inicial á plataforma.

- O panel de progreso mostrará gráficas co avance por nivel HSK, resumo de palabras aprendidas e evolución temporal do usuario.

O estilo visual baséase en Tailwind CSS, con cores escuras e degradados azul-violeta, tipografía clara e deseño responsive adaptable a dispositivos móbiles.

### Diseño de interfaces software e hardware.

- Non se require hardware específico
- Software:
  - Backend: API Django, integración IA vía HTTP
  - Frontend: HTML + Tailwind CSS
  - Base de datos: PostgreSQL

### Diagrama de Base de Datos.

<img src="/doc/img/diagramadatos.svg" alt="Diagrama Base de datos" />

### Consideracións técnicas e de seguridade

- Acceso por login con autenticación de Django
- Variables sensibles (.env) con claves API, credenciais
- Uso de HTTPS
- Posibilidade de limitar chamadas á IA por usuario no futuro

## Calidade

### Aspectos clave a controlar:

- Corrección das funcionalidades (CRUD, IA, chat, exportación)
- Usabilidade da interface (limpa, clara, intuitiva)
- Rendemento do sistema (probas en VPS con usuarios simultáneos)
- Integración correcta coa API de IA (maneixo de erros incluído)

### Procedementos de control:

- Probas manuais por cada sprint
- Validación de formularios (lado cliente e servidor)
- Probas de exportación e datos