# Idea

* Qué tipo de proxecto vas levar a cabo? Vas realizar únicamente a planificación e deseño ou crearás un entregable?
Vou realizar un proxecto con entregable funcional. Non será só un deseño ou planificación, senón unha aplicación real que se poderá usar para xestionar, estudar e practicar vocabulario en chinés.

* En que consiste o teu proxecto? Cal é o propósito principal do mesmo?
O proxecto consiste nunha aplicación (inicialmente de escritorio) que permite organizar o vocabulario dos primeiros niveis de HSK (os exames oficiais de chinés) de forma ordenada, visual e filtrable.
O propósito principal é facilitar o estudo activo do chinés simplificado, permitindo ao usuario controlar que vocabulario aprende, como o clasifica e ter sempre un acceso ordenado e personalizado.

* A quen vai destinada a aplicación? (Cómo é o contexto social do cliente ou sector da empresa á que está dirixido).
Vai destinada principalmente a estudantes de chinés, tanto autodidactas como alumnos de escolas ou academias de idiomas. Tamén podería ser útil para profesores que queiran compartir listas personalizadas cos seus alumnos. O contexto é o sector educativo, especialmente no campo das linguas extranxeiras.

* Cal é a necesidade ou necesidades que se pretenden cubrir ou satisfacer? O desenvolvemento deste proxecto, abre unha oportunidade de negocio? É posible comercializalo? Como?
Si, abre unha oportunidade clara: a aplicación podería evolucionar a unha versión web con subscrición, incluíndo máis servizos como exercicios personalizados, IA máis avanzada, análises de progreso e mesmo acceso multiusuario para escolas ou academias. Poderíase monetizar a través de plans premium que cubran os custos da API e xeren beneficios.

* Existen na actualidade aplicacións que tenten dar resposta a esa(s) necesidade(s)? En que medida o conseguen?
Si, existen diccionarios online e apps de estudo de chinés, pero adoitan estar centradas en buscar palabras individuais ou practicar flashcards, non en permitir ao usuario construír e organizar a súa propia base de datos de vocabulario personalizada. Ningunha ofrece un enfoque tan flexible e ordenado por categorías gramaticais e niveis HSK combinados cun asistente IA que facilite a organización.

* Qué obxectivos ten o teu proxecto? Qué requisitos básicos debe cumprir?
Obxectivos principais:
- Crear unha aplicación funcional para xestionar e estudar vocabulario chinés.
- Integrar unha IA (DeepSeek) para facilitar a creación e clasificación automática de entradas.
- Permitir filtrar, exportar e practicar os datos de forma visual e organizada.
- Garantir unha experiencia de usuario intuitiva, sen rexistro complicado nin dependencia constante de conexión.

Requisitos básicos que debe cumprir:
- Base de datos local (SQLite) para almacenar o vocabulario.
- Interfaz gráfica moderna e scrolleable (CustomTkinter).
- Conexión coa API de IA para consultas automáticas e funcións específicas.
- Exportación dos datos filtrados a Excel con formato visual atractivo (openpyxl).
- Control seguro das funcións chamadas pola IA, asegurando que non hai riscos de modificacións perigosas na base de datos.

* Qué tecnoloxías tes pensado empregar para levalo a cabo?
- Python → Linguaxe principal de desenvolvemento.
- CustomTkinter → Biblioteca para a interfaz gráfica moderna.
- SQLite → Base de datos local lixeira e eficiente.
- DeepSeek API → Integración coa IA para análises e clasificación automática.
- openpyxl → Exportación de datos a ficheiros Excel personalizados.