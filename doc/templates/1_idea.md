# Idea

Este proxecto consiste no desenvolvemento dunha aplicación web funcional destinada a estudantes da lingua chinesa. O seu propósito é ofrecer unha ferramenta flexible e visual para organizar, practicar e revisar vocabulario segundo os niveis do estándar oficial **HSK** (汉语水平考试).

A diferenza doutras solucións existentes, esta aplicación non se limita a un dicionario ou a un sistema de flashcards. Pretende dar ao usuario **control total sobre o seu vocabulario**, integrando tamén funcionalidades avanzadas como o **recheo automático con IA**.

---

##  Obxectivo Principal

O obxectivo fundamental é permitir aos usuarios:

- Crear e editar listas de vocabulario personalizadas.
- Clasificar palabras segundo o seu nivel HSK e categoría gramatical.
- Consultar información ampliada (pinyin, tipo, exemplos...).
- Acceder a un asistente virtual con IA para resolver dúbidas.
- Exportar o contido a formato **Excel profesional**.

Todo isto nunha interface moderna, práctica e deseñada para a aprendizaxe autónoma ou guiada.

---

## Público Obxectivo

A aplicación está orientada a diferentes perfís dentro do ámbito educativo e profesional:

- Estudantes autodidactas de chinés simplificado.
- Alumnado de escolas de idiomas ou institutos.
- Profesorado que desexe compartir listas co seu alumnado.

---

## Necesidades que Cobre

Actualmente existen poucas ferramentas que combinen:

- Organización estruturada por **nivel HSK e tipo gramatical**.
- **Edición libre e control total** sobre o vocabulario.
- Integración dunha **IA que axude a completar os campos automaticamente**.
- Funcionalidades de **práctica, revisión e exportación profesional**.

Esta aplicación cobre ese oco, ofrecendo unha solución moderna e adaptable.

---

## Integración con IA

Mediante a API de **DeepSeek**, a aplicación poderá:

- Responder a dúbidas lingüísticas mediante un asistente virtual.

---

## Modelo de Negocio (a futuro)

O proxecto poderá evolucionar a unha plataforma web con modelo **freemium**:

- Acceso básico gratuíto.
- Funcionalidades premium mediante subscrición:
  - Exportación avanzada.
  - Estatísticas personalizadas.
  - Exercicios xerados por IA.
  - Xestión multiusuario para academias ou profesorado.

---

## Funcionalidades Técnicas

A aplicación debe permitir:

- ✅ Crear, editar e eliminar entradas de vocabulario.
- ✅ Clasificar por **nivel HSK** e tipo gramatical.
- ✅ Consultar detalles como pinyin, tradución e exemplo.
- ✅ Exportar listas a **Excel (.xlsx)**.
- ✅ Usar un **asistente con IA** para completar ou revisar contido.

---

## Tecnoloxías e Arquitectura

- **Backend**: Python + Django
- **Frontend**: Tailwind CSS
- **Base de datos**: SQLite
- **Exportación**: Ficheiros Excel (.xlsx) con formato limpo e profesional
- **Autenticación**: Sistema de usuarios con login seguro
- **IA**: API de DeepSeek para recheo e consulta intelixente
- **Control de uso da IA**: Limitación de chamadas para estabilidade e seguridade