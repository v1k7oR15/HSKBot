# Idea

O proxecto que se vai levar a cabo consiste no desenvolvemento dunha aplicación funcional e operativa, non só un deseño teórico ou unha planificación. Trátase dun sistema real que permitirá aos usuarios xestionar, estudar e practicar vocabulario en chinés, concretamente adaptado aos primeiros niveis do estándar HSK (exames oficiais de lingua chinesa).
O propósito principal da aplicación é ofrecer unha ferramenta visual, ordenada e práctica para estudantes de chinés simplificado. A idea é que o usuario poida controlar o vocabulario que aprende, como o clasifica e dispoña sempre dun acceso á súa base de datos personalizada, sen depender de solucións pechadas ou ríxidas.
A aplicación está dirixida a un público educativo: estudantes autodidactas, alumnado de escolas de idiomas e profesorado que desexe organizar ou compartir listas personalizadas cos seus grupos. O seu contexto natural é o ensino formal ou informal da lingua chinesa, aínda que tamén podería utilizarse en contextos profesionais relacionados coa tradución ou preparación de certificacións oficiais.
A principal necesidade que cobre o proxecto é a falta de ferramentas que permitan ao estudante organizar o seu propio vocabulario dunha maneira estruturada por nivel HSK e categoría gramatical, mantendo ao mesmo tempo a posibilidade de practicar, revisar e exportar ese contido. Ademais, a integración dunha IA (DeepSeek) abre novas posibilidades como o recheo automático de información (pinyin, tipo, exemplo, etc.), o que supón un aforro de tempo e evita erros comúns.
Existen actualmente algunhas aplicacións que ofrecen funcionalidades parciais, como dicionarios en liña ou apps de flashcards, pero ningunha ofrece un enfoque personalizado, flexible e adaptado á progresión de cada usuario. Tampouco permiten organizar listas propias de maneira efectiva nin integrar funcionalidades de intelixencia artificial.
Este proxecto abre unha oportunidade clara de negocio. Podería evolucionar cara a unha plataforma web cun modelo freemium: acceso básico gratuíto e plans de subscrición con funcionalidades avanzadas como exportación de datos, estatísticas, exercicios xerados por IA e xestión multiusuario para academias. A comercialización sería viable mediante pagos recorrentes, dirixidos a estudantes e centros educativos.
En canto aos obxectivos técnicos, o sistema debe permitir ao usuario:
- Crear, editar e organizar entradas de vocabulario.
- Consultar e clasificar palabras segundo nivel HSK e tipo gramatical.
- Exportar listas personalizadas en formato Excel.
- Consultar un asistente virtual para dúbidas ou axuda.

Os requisitos básicos do sistema inclúen:
-Base de datos PostgreSQL (ou SQLite en desenvolvemento).
-Interfaz web moderna baseada en Tailwind CSS.
-Backend con Django e integración con API de IA (DeepSeek).
-Exportación de datos a Excel (formato profesional).
-Sistema de usuario con autenticación e sesión segura.
-Control de chamadas á IA para garantir seguridade e estabilidade.

As tecnoloxías empregadas serán Python como linguaxe principal, Django como framework de backend, Tailwind CSS para a construción da interface de usuario, PostgreSQL como base de datos en produción, e a API de DeepSeek para tarefas de enriquecemento automático e interacción intelixente.