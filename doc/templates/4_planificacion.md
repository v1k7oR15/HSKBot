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


### Metodoloxía
Indica a metodoloxía que se utilizará para a elaboración do proxecto: ciclo en cascada, incremental, espiral... Xustifica a elección.

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
| 2.2 Prototipo UI wireframe    | Navegación, mockups Tailwind          | Figma                 | Víctor   | 5 h  |
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
Un diagrama de Gantt é unha representación gráfica da secuenciación que tes que seguir para realizar as tarefas planificadas. Pódese usar o software "Gantt project" ou calquera outro que permita representar nun cronograma a información relativa á planificación de tarefas. Neste diagrama plasmarás de forma gráfica e manexable as fases e tarefas anteriores.

## Orzamento
O orzamento do proxecto será a suma do importe dos materiais que necesites para realizar o proxecto máis o importe que corresponde ao traballo realizado. 
O importe relacionado co traballo no proxecto é relativamente fácil de obter se se elaboraron ben as etapas anteriores: definir as actividades necesarias e os recursos propios de cada actividade. Neste caso disporase dun custo por cada actividade e a suma do custo de todas as actividades será o custo total do traballo do proxecto. 
Para establecer os custos do proxecto debes ter en conta diferentes conceptos: 
- Materiais que se utilizan: material funxible, materias primas, materiais didácticos, roupa de traballo… 
- Custo horario das persoas que participan directamente na actividade. 
- Aluguer/compra de ferramentas, maquinaria, equipos informáticos e/ou audiovisuais… 
- Aluguer/compra de locais 
- Contratos de subministracións: auga, luz, electricidade, gas… Subcontrataciones 
- Gastos de publicidade… 
- Seguros ... 

O maior custo no proxecto case sempre corresponde ás persoas, polo que é importante controlar o número de horas que se invisten en cada actividade para que non se nos desequilibre o orzamento. Tamén hai que coidar as subcontratacións; convén que traballen cun orzamento establecido.
 A continuación preséntanse dúas opción de táboa para facilitar a creación do orzamento do proxecto:

### Orzamento por actividade

| ACTIVIDADE | DURACIÓN | CUSTO (EUROS) | | CUSTO TOTAL ACTIVIDADE |
|--|--|--|--|--|
|            |          | PERSOAS|RECURSOS MATERIAIS|
|||||
|||||
|||||
|||||

| TOTAL | PROXECTO | 
| -- | -- |

### Orzamento por partidas de inversión / gasto:

| CONCEPTO | IMPORTE|
|--|--|
|**A) INVERSIONS**
|Gastos de establecemento e gastos de constitución
|Total inmobilizacións inmateriais
|Terreos
|Construcións
|Instalacións técnicas
|Maquinaria
|Ferramentas
|Mobiliario e instalacións
|Equipos informáticos
|Elementos de transporte
|Outro inmobilizado material
|Total inmobilizacións materiais
|Outros gastos a distribuír en varios exercicios
|**TOTAL INVERSIÓNS:**
|**B) GASTOS**
|Compras de materiais
|Arrendamentos
|Publicidade, propaganda e relacións públicas
|Persoal
|Reparacións e conservación
|Servizos de profesionais independentes
|Outros gastos xerais
|Gastos financeiros
|Amortizacións
|Gastos de xestión e administración
|**TOTAL GASTOS:**

|TOTAL ORZAMENTO:
|--|

### WEBGRAFÍA
Guía para a elaboración de proyectos. Gobierno Vasco.
https://www.pluralismoyconvivencia.es/upload/19/71/guia_elaboracion_proyectos_c.pdf  (páxina 49 e seguintes)



