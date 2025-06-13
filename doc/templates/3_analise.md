# REQUIRIMENTOS DO SISTEMA
Este documento recolle os requirimentos do proxecto HSKBot, unha aplicación web para organizar e estudar vocabulario de chinés mandarín

## Descrición Xeral

HSKBot é unha plataforma en Django orientada a estudantes que necesitan rexistrar, clasificar e practicar léxico chinés.
A aplicación integra Tailwind CSS para unha interface limpa, IA (vía DeepSeek) para xerar pinyin, tradución, exemplos e exercicios, e posibilita a exportación visual a Excel. O sistema é multiusuario, preparado para crecemento SaaS.

## Funcionalidades

- Rexistro e autenticación (e-mail / social)
- Alta de caracteres e palabras:
  - Manual ou automática (petición á IA)
  - Clasificación por nivel HSK, tipo gramatical, tags personalizados
- Buscador avanzado (pola forma, pinyin, tradución, nivel, tipo)
- Filtros dinámicos: nivel HSK exacto ou acumulativo
- Exportación:
  - Folla de cálculo en formato XLSX con cores por categoría
- Rol administrador: xestión de usuarios, respaldo da BD, parámetros IA
- API REST (token-based) para integracións futuras (móbil, desktop, LMS)

## Requerimentos non funcionais
- Rendemento: tempo de resposta < 300 ms para consultas.
- Escalabilidade: dockerizado; preparado para réplicas horizontais.
- Seguridade: cifrado TLS 1.3; almacenamento de credenciais con Argon2; limitación de chamadas á IA por usuario.


## Tipos de usuarios
- Estudante: añadir vocabulario, crear listas, exportar material.
- Administrador: acceso total a configuración, facturación, API-keys e backups.


## Avaliación da viabilidade técnica do proxecto

### Hardware
- Desenvolvemento: Ordenador portátil i5/16 GB ou superior.

#### Software
- Backend: Python 3.12, Django 5, Django REST Framework, Celery + Redis.
- Frontend: Tailwind CSS; build automatizado con django-tailwind.
- Base de datos: SQLite para modo local.

#### Infraestrutura 
- Docker, docker-compose.

### Interfaces externos
- Interface de usuario: SPA progresiva servida por Django Templates.
- Interface software: REST JSON autenticado por token (JWT).
- Servizo IA: API DeepSeek Chat v3.

## Análise de riscos e interesados
# Tabla de riesgos y mitigaciones

| Interesado   | Impacto | Riesgo                             | Mitigación                                  |
|--------------|---------|------------------------------------|---------------------------------------------|
| Estudantes  | Alto    | Sobrecarga de la IA → latencia     | Caché de respuestas, límite de uso          |
| Estudantes    | Medio   | Datos incompletos                  | Validación manual + importación por lotes   |
| Estudantes   | Alto    | Fallo de exportación               | Backups diarios + tests de integración      |
| Proveedor IA | Alto    | Cambio de precios                  | Abstracción de driver, cambio a otro LLM    |


## Actividades
- Análise de requisitos e deseño BD
- Configuración do repo (GitLab) e CI/CD
- Integración Tailwind + prototipado UI
- Modelado de datos, vistas, formularios
- Integración DeepSeek e almacenamento de respostas
- Módulo de exercicios e estatísticas
- Exportación a Excel/PDF
- Tests, documentación, despregue en VPS con Docker
- Demo para titoría e iteración final

## Melloras futuras
- App móbil híbrida.
- Sincronización espaciada baseada en algoritmos SM-2.
- Múltiples idiomas.
- Facilitar tamén o aprendizaxe da gramática.
- Sistema de pagamento e plans de subscrición SaaS.