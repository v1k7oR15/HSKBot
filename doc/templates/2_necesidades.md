# ESTUDO DE NECESIDADES E MODELO DE NEGOCIO

## Xustificación das Necesidades Detectadas

A aprendizaxe do chinés nos primeiros niveis HSK carece de ferramentas verdadeiramente personalizables e prácticas. As solucións actuais, como PDFs oficiais ou apps de flashcards, resultan ríxidas, pouco adaptables e orientadas máis á memorización que á comprensión real. Este proxecto pretende cubrir esa carencia mediante unha aplicación que integre organización avanzada, práctica activa e apoio de intelixencia artificial.

### Problema Detectado

- As listas oficiais de vocabulario adoitan estar en PDF ou formatos estáticos.
- Non existe unha maneira sinxela de **organizar palabras por tipo gramatical ou nivel HSK**.
- A maioría das apps non permiten **editar nin personalizar** as listas de vocabulario.
- Falta integración con exemplos contextualizados ou funcionalidades dinámicas.
- Os estudantes teñen dificultades para facer un seguimento estruturado do que aprenden.

### Necesidade de Desenvolver Esta Aplicación

- Resolvería unha **carencia real no ensino do chinés** adaptado ao estudante actual.
- Permitiría unha **aprendizaxe máis activa, personalizada e estruturada**.
- Integraría IA para xerar exemplos, pinyin, traducións e exercicios de forma automática.
- Serviría tanto a nivel individual como en contextos educativos ou profesionais.

### Obxectivo Xeral

Desenvolver unha aplicación funcional que:

- Permita aos usuarios **organizar, clasificar e practicar vocabulario chinés**.
- Use tecnoloxía actual (Python, IA, exportación a Excel).
- Poida adaptarse a diferentes perfís de estudantes, desde autodidactas ata academias.

### Recursos e Actividades Previstas

- 💻 Ordenador persoal con Python e SQLite.
- 🧰 Bibliotecas: `django`, `django-tailwind`, `openpyxl`, `openai` para API.
- 🔌 Integración con API de **DeepSeek** (para IA).
- 📋 Actividades previstas:
  - Deseño da base de datos.
  - Creación da interface gráfica.
  - Programación de filtrado, edición e exportación.
  - Probas e corrección de erros.
  - Documentación técnica e entrega final.

### Metodoloxía

- Metodoloxía **iterativa**, baseada en ciclos curtos de:
  - Deseño → Desenvolvemento → Proba → Axuste.
- Permite entregar unha versión estable e funcional ao final do proceso.
- Flexibilidade para mellorar funcionalidades segundo avance o proxecto.

### Tempo Estimado

- Duración total: aproximadamente **2 meses efectivos**.
- Estimación de traballo: entre **40 e 50 horas** repartidas entre:
  - Análise de requisitos.
  - Deseño de interface e base de datos.
  - Desenvolvemento e probas.
  - Documentación.

### Equipo Necesario

- Para esta versión: unha soa persoa desenvolvedora (proxecto individual).
- Para unha versión profesional:
  - Desenvolvedor backend.
  - Deseñador UI/UX.
  - Especialista en IA.
  - Persoa de contidos académicos (para exercicios e revisión lingüística).

---

## Viabilidade e Comercialización

### Viabilidade Técnica

- O proxecto pode desenvolverse con **software libre e recursos accesibles**.
- Ferramentas empregadas:
  - Python, SQLite, bibliotecas open source.
  - API de DeepSeek, dispoñible de forma gratuíta para uso persoal.
- Non se detectan impedimentos técnicos relevantes a curto prazo.
- O único reto futuro sería o **control de custos da API**, en caso de escalar o uso.

### Viabilidade Económica

- O desenvolvemento inicial **non require investimento económico**.
- Os custos principais só aparecerían se se opta por unha versión web:
  - Infraestrutura (servidor, base de datos online, seguridade).
  - Uso intensivo da API.
- Estes custos poden cubrirse cun modelo de **subscrición freemium**.
- Non se contempla financiamento público inmediato, pero é un camiño a explorar.

### Competencia no Mercado

- Aplicacións como **Pleco**, **Anki** ou **HelloChinese** están ben posicionadas, pero:
  - Non permiten **organización personalizada do vocabulario**.
  - Non integran IA para crear contido dinámico.
  - Non ofrecen **exportación estruturada** para estudo externo (como Excel).
- A nosa aplicación cubriría un **nicho específico**, orientado a estudantes con necesidades avanzadas de organización e práctica.

### Estratexia de Comercialización

- Canles de promoción:
  - **Redes sociais** (Instagram, TikTok, Twitter/X).
  - Páxina web con presentación e acceso á demo/descarga.
  - Posicionamento SEO (palabras clave como “aprender chinés”, “HSK vocabulario”).
  - Participación en comunidades online de estudantes (Discord, foros).
  - **Colaboración con academias** e profesorado de chinés.

- Xustificación:
  - Difusión orgánica e de baixo custo.
  - Acceso directo ao público obxectivo.
  - Reforzo da credibilidade mediante alianzas estratéxicas.

### Modelo de Negocio

- Modelo **freemium + subscrición**:
  - Versión **gratuíta** local e funcional para uso persoal.
  - Versión **premium web** con:
    - Exercicios automáticos.
    - Exportación masiva.
    - Seguimento do progreso.
    - Acceso ampliado á API.
    - Soporte multiusuario para academias.

- Vantaxes:
  - Atracción inicial de usuarios sen barreiras de entrada.
  - Monetización sostible sen recorrer á publicidade.
  - Adaptación segundo o perfil do usuario (persoal vs educativo).