# FASE DE PLANIFICACIÓN DO PROXECTO

## Obxectivos do proxecto

- Dispoñibilizar unha aplicación web (SaaS auto-instalable) que permita rexistrar, clasificar e practicar vocabulario HSK (niveles 1-4, escalable a 6).
- Integrar IA DeepSeek para xeración de pinyin, significado, exemplos e exercicios.
- Ofrecer exportación a Excel/PDF con formato amigable.
- Facilitar panel de progreso para estudantes e zona de xestión para docentes/academias.
- Despregue dockerizado, preparado para multi-usuario e futuras versións móbil/API.

## Guía de planificación do proxecto

| Aspecto              | Decisión                                                                                                                                                                                                        |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metodoloxía**      | **Incremental-iterativa** (Scrum “ligero”). <br>– Entregas pequenas cada 2-3 semanas.<br>– Permite mostrar versións funcionais.<br>– Reduce risco á hora de integrar IA e exportación. |
| **Duración total**   | 8 semanas.                                                                                                                                                                                   |
| **Recursos humanos** | 1 desenvolvedor.                                                                                                                               |
| **Ferramentas**      | VS Code, GitLab, SQLite, Tailwind, DeepSeek API.                                                                                                                               |


## Metodoloxía

### Fases planificadas

#### Fase 1: Estudo de necesidades e modelo de negocio

| Tarefa                    | Descrición                                           | HW/SW                  | Recursos humanos | Duración |
| ------------------------- | ---------------------------------------------------- | ---------------------- | ---------------- | -------- |
| 1.1 Investigación usuario | análise PDFs HSK | Portátil, Google Forms            | Portátil               | Víctor           | 2 h      |
| 1.2 Análise competidores  | Apps HSK existentes, prezos, carencias               | Navegador              | Víctor           | 1 h      |

#### Fase 2: Deseño técnico

| Tarefa                        | Descrición                            | HW/SW                 | Recursos | Dur. |
| ----------------------------- | ------------------------------------- | --------------------- | -------- | ---- |
| 2.1 Diagramas UML             | Casos de uso, modelo BD, secuencia IA | Draw\.io              | Víctor   | 2 h  |
| 2.2 Prototipo UI wireframe    | Navegación, mockups Tailwind          | VS Code               | Víctor   | 5 h  |
| 2.3 Config inicial repo       | GitLab, `.venv`                       | VS Code               | Víctor   | 2 h  |
| 2.4 Def. API DeepSeek         | Especificar prompts, límite tokens    | Postman               | Víctor   | 2 h  |
| 2.5 Plan seguridade & back-up | backups BD                            | Markdown              | Víctor   | 2 h  |
| 2.6 Plan probas               | Matriz de test unit + funcional       | pytest                | Víctor   | 4 h  |

#### Fase 3: Construcción incremental

| Sprint | Funcionalidade principal                                             | Horas ciclo |
| ------ | -------------------------------------------------------------------- | ----------- |
| S1     | **Autenticación + modelo Vocabulario** <br>CRUD, import manual       | 10          |
| S2     | **Integración Tailwind + UI básica** <br>Listado, filtro nivel       | 10          |
| S3     | **IA DeepSeek** <br>Alta automática, xeración exercicios simples     | 10          |
| S4     | **Exportación Excel/PDF** <br>Formato con cores por categoría        | 10          |

### Diagrama de Gantt
![Diagrama de Gantt do proxecto](doc/img/diagramagant.png)

## Orzamento

### Orzamento por actividade - Proxecto Mínimo Viable

| ACTIVIDADE                        | DURACIÓN ESTIMADA | PERSOAS (€/hora) | RECURSOS MATERIAIS (€) | CUSTO TOTAL ACTIVIDADE (€) |
| --------------------------------- | ----------------- | ---------------- | ---------------------- | -------------------------- |
| Investigación e análise           | 3 h               | 15 €/h           | 0 €                    | 45 €                       |
| Deseño técnico (UML, UI)          | 7 h               | 15 €/h           | 0 €                    | 105 €                      |
| Configuración inicial do proxecto | 2 h               | 15 €/h           | 0 €                    | 30 €                       |
| Integración API DeepSeek          | 4 h               | 15 €/h           | 0 €                    | 60 €                       |
| Desenvolvemento CRUD + UI básica  | 10 h              | 15 €/h           | 0 €                    | 150 €                      |
| Exportación Excel/PDF             | 5 h               | 15 €/h           | 0 €                    | 75 €                       |
| Probado e documentación           | 4 h               | 15 €/h           | 0 €                    | 60 €                       |

### Orzamento por actividade - Versión Profesional Futura

| ACTIVIDADE                         | DURACIÓN ESTIMADA | PERSOAS (€/hora) | RECURSOS MATERIAIS (€) | CUSTO TOTAL ACTIVIDADE (€) |
| ---------------------------------- | ----------------- | ---------------- | ---------------------- | -------------------------- |
| Análise de mercado e usuarios      | 5 h               | 25 €/h           | 0 €                    | 125 €                      |
| Deseño UI/UX profesional           | 10 h              | 30 €/h           | 0 €                    | 300 €                      |
| Backend API REST + base de datos   | 15 h              | 30 €/h           | 0 €                    | 450 €                      |
| Frontend web responsive            | 15 h              | 30 €/h           | 0 €                    | 450 €                      |
| Integración avanzada con IA        | 10 h              | 35 €/h           | 20 € (API)             | 370 €                      |
| Panel de usuario e docente         | 10 h              | 30 €/h           | 0 €                    | 300 €                      |
| Sistema de subscrición             | 6 h               | 30 €/h           | 0 €                    | 180 €                      |
| Despregue dockerizado              | 6 h               | 30 €/h           | 0 €                    | 180 €                      |
| Probas, documentación e lanzamento | 8 h               | 25 €/h           | 0 €                    | 200 €                      |

### Orzamento por partidas de inversión / gasto:

| CONCEPTO                                                        | IMPORTE (€) |
| --------------------------------------------------------------- | ----------- |
| **A) INVERSIÓNS**                                               |             |
| Equipos informáticos (ordenador persoal utilizado)              | 800 €       |
| Mobiliario e instalacións (mesa de traballo, cadeira)           | 150 €       |
| Software empregado (VS Code, SQLite, bibliotecas – open source) | 0 €         |
| Total inmobilizacións materiais                                 | **950 €**   |
|                                                                 |             |
| **B) GASTOS**                                                   |             |
| Materiais funxibles (libreta, bolígrafos, folios...)            | 10 €        |
| Internet (prorrata 2 meses do custo mensual: 40 €/mes)          | 80 €        |
| Electricidade (uso estimado 20 €/mes durante o desenvolvemento) | 40 €        |
| Persoal (35 h × 15 €/h, como desenvolvedor individual)          | 525 €       |
| Publicidade e promoción (difusión orgánica en redes)            | 20 €        |
| Outros gastos xerais (copias, imprevistos menores)              | 15 €        |
| Total gastos                                                    | **690 €**   |
