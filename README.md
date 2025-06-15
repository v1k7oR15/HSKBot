# Proyecto fin de ciclo

## Descripción

**HSKBot** é unha aplicación web que facilita o estudo do vocabulario chinés mandarin, especialmente para os niveis 1 a 4 do exame oficial HSK. Permite crear unha base de datos personalizada de palabras, engadidas manualmente ou completadas automaticamente con IA (pinyin, tradución, tipo gramatical, nivel e exemplo).

Inclúe filtros por nivel e categoría, exportación visual a Excel con códigos de cor, e un chat integrado con IA para xerar exercicios ou resolver dúbidas. Todo iso nun entorno seguro, visual e adaptado ao ritmo de cada estudante.

## Instalación / Puesta en marcha

1. Clona o repositorio:
   ```bash
   git clone git@gitlab.com:iesleliadoura/DAM2/victor-manuel-iglesias.git
   cd victor-manuel-iglesias
   ```

2. Crea o entorno virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Instala os requisitos:
   ```bash
   pip install -r requirements.txt
   ```

4. Executa o servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

- **Inicio de sesión** e rexistro de usuarios.
- **Engadir palabras** manualmente ou mediante IA.
- **Filtrar e buscar vocabulario** por nivel HSK, tipo gramatical, etc.
- **Exportación a Excel** con formato de cores.
- **Chat con IA** para resolver dúbidas ou xerar exercicios.

Interface clara e responsiva, deseñada con Tailwind CSS.

## Sobre el autor

Chámome **Víctor Iglesias**, estudante de Desenvolvemento de Aplicacións Multiplataforma. Interésanme o deseño de páxinas web e as linguas estranxeiras, polo que este proxecto xorde da combinación de ambos intereses. A idea era crear unha ferramenta útil para estudantes coma min, que aprendan chinés dun xeito máis visual e organizado.
📧 Contacto: arcosvictor1@gmail.com

## Licencia

Este proxecto esta licenciado baixo a licencia GNU General Public License v3.0.
Consulte o archivo [LICENSE](.doc/LICENSE) para máis información

## Índice

1. Anteproyecto
    * 1.1. [Idea](doc/templates/1_idea.md)
    * 1.2. [Necesidades](doc/templates/2_necesidades.md)
2. [Análisis](doc/templates/3_analise.md)
3. [Planificación](doc/templates/4_planificacion.md)
4. [Diseño](doc/templates/5_deseño.md)
5. Implantación
    * 5.1 [Implementación](doc/templates/6_implementacion.md)
    * 5.2 [Producción](doc/templates/7_producion.md)


## Guía de contribución

Este é un proxecto de software libre. Se queres contribuír, podes:

- Engadir novas funcionalidades
- Corrixir ou optimizar o código
- Desenvolver novos tests automáticos
- Crear novos plugins ou integracións
- Mellorar a interface de usuario

## Links

- [Documentación de Django](https://docs.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [DeepSeek API](https://platform.deepseek.com/)