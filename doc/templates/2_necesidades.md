# ESTUDO DE NECESIDADES E MODELO DE NEGOCIO

## Xustificación das necesidades detectadas que cubre o sistema a desenvolver
1.	Describe o problema ou a necesidade.

Os estudantes de chinés, especialmente nos primeiros niveis de HSK, non dispoñen de ferramentas flexibles para organizar, clasificar e estudar vocabulario de forma personalizada. As listas oficiais adoitan vir en PDF ou formatos ríxidos, sen opción de filtrado, clasificación por categorías gramaticais ou integración con exemplos dinámicos. Isto fai que a aprendizaxe sexa máis desordenada e menos eficiente.

2.	Por que é necesaria a posta en marcha dun proxecto que aborde dita necesidade?

Porque resolvería unha carencia concreta no ámbito do estudo de idiomas, ofrecendo unha ferramenta útil tanto para estudantes individuais como para academias. Unha aplicación así permitiría personalizar a aprendizaxe, mellorar a retención de vocabulario e abriría a porta a funcionalidades innovadoras como a integración con IA para xerar exercicios, exemplos e traducións automáticas.

3.	Cal é o obxectivo xeral que persegue o proxecto?

O obxectivo xeral é desenvolver unha aplicación funcional que permita aos estudantes organizar, clasificar e practicar vocabulario chinés dun xeito eficiente, personalizado e apoiado en tecnoloxía moderna como a intelixencia artificial.

4.	Responde a estas preguntas concretas:

    4.1.Como se pode responder a esta necesidade? 
    
    Creando unha aplicación que centralice o vocabulario por niveis e categorías, permita filtrado avanzado, e ofreza apoio da IA para cubrir lagoas de contido (como pinyin, exemplos ou exercicios).

    4.2. Que pode facerse para cambiar este estado de cousas? 

    Desenvolver unha ferramenta flexible, accesible e adaptable ás necesidades do estudante, superando as limitacións das listas estáticas e dos materiais tradicionais.
    
    4.3. Como podemos contribuír desde a nosa situación a que o problema se resolva?

    Aplicando os coñecementos adquiridos no ciclo DAM (programación, bases de datos, interfaces gráficas) para crear unha aplicación que dea resposta real ás necesidades detectadas.
    
    4.4. Que medios, actividades e recursos van poñer en xogo? 

    -Ordenador persoal con entorno Python instalado.

    -API de DeepSeek para integración con IA.

    -Base de datos SQLite para xestionar a información.

    -Bibliotecas como CustomTkinter e openpyxl.

    -Actividades de deseño, programación, probas e documentación.
    
    4.5. Que actividades se van realizar?

    -Deseño da base de datos e modelo de datos.
    -Programación da interfaz gráfica.
    -Integración co API da IA.
    -Implementación das funcións de filtrado e exportación.
    -Probado de funcionalidades e corrección de erros.
    -Documentación do proxecto e elaboración do entregable.
    
    4.6. Que metodoloxía se vai empregar para levar a cabo o traballo?

    Metodoloxía iterativa, centrada en ciclos curtos de deseño → desenvolvemento → proba, que permitan axustar as funcionalidades segundo se vaia avanzando no proxecto, garantizando que a versión entregable funcione correctamente antes de engadir melloras.
    
    4.7. Que persoas serían precisas para realizar o proxecto con éxito? 
    
    -Nun contexto persoal, só eu como desenvolvedor. Nunha versión profesional, sería recomendable contar con:
    -Desenvolvedor backend
    -Deseñador UI/UX
    -Especialista en IA/ML
    -Persoa de contidos académicos para deseño de exercicios

    4.8 Con canto tempo se conta? 
    
    Conto co tempo establecido polo calendario do proxecto de fin de ciclo, aproximadamente uns 2 meses de traballo efectivo.

    4.9 Canto tempo se necesita?

    Para o entregable funcional, estimo unhas 40-50 horas distribuídas en análise, deseño, desenvolvemento, probas e documentación. Unha versión máis completa e pulida podería requirir máis tempo, especialmente se se decide levala á web ou incluír máis funcionalidades.



## Posibilidades de comercialización (viabilidade, competidores…).
1.	Viabilidade.

    1.1	Viabilidade técnica.
    
        1.1.a) Será posible dispoñer dos recursos humanos e medios de produción necesarios (materias primas, maquinaria, instalacións…)?

        O proxecto pode ser desenvolvido inicialmente por unha única persoa cun ordenador persoal e conexión a internet. As ferramentas principais (Python, SQLite, CustomTkinter, openpyxl) son de código aberto, e a integración con IA require unicamente o acceso á API de DeepSeek, que para uso personal podese conseguir de maneira gratuíta.
        
        1.1.b) Existe algún impedimento técnico que dificulte o proceso produtivo?
        Non hai impedimentos técnicos graves. O principal reto será o control dos custos da API se o número de usuarios medra, pero inicialmente o uso está pensado para ser local/persoal polo que non existe ese problema
        
    1.2	Viabilidade económica
    
        1.2.a) Os beneficios do proyecto son superiores aos costes?
        
        Si, a longo prazo. O proxecto é viable porque, unha vez desenvolvido, os custos principais virán do mantemento da infraestrutura (no caso dunha versión web) e do pago pola API de IA, que pode cubrirse mediante modelos de subscrición ou pagos premium. O desenvolvemento inicial require só tempo e coñecemento, sen investimento material importante. Probablemente, para manter os beneficios habería que poñer un límite ao uso da API dependendo do tipo de subscripción

        1.2.b) As perdas poden cubrirse vía financiamento (por parte da administración pública, con subvencións, etc)?

        Probablemente non, descoñezo os requerimentos para estas subvencións pero non creo que este proxecto cumpla os requerimentos.

        
2.	Competencia.

    2.1. Identificación da competencia, as súas características e a súa posición no mercado.

    Existen aplicacións como Pleco, HelloChinese ou Anki que permiten estudar chinés, pero ningunha combina especificamente:
    -Organización personalizada de vocabulario por nivel e tipo gramatical
    -Integración flexible cun asistente IA para explicar, traducir e xerar exercicios
    -Exportación visual ordenada para estudo externo (como Excel personalizado)
    -Estes competidores están moi ben posicionados no mercado global, pero o nicho específico do proxecto ofrece diferenciación clara.

    2.2. Existencia de productos/servizos substitutivos.

    Si, os usuarios poden usar actualmente:
    -PDFs oficiais de vocabulario (de xeito manual)
    -Apps de flashcards (Anki)
    -Diccionarios online (Pleco)

    Pero estes non permiten a mesma personalización, organización e apoio dinámico de IA, o que dá unha vantaxe competitiva ao proxecto.

## Ideas para a súa comercialización.
1.	Promoción.

    1.1.	Técnicas elixidas (redes sociais, plataformas multimedia, páxina web, posicionamento web SEO, patrocinios, participación en eventos, prácticas de responsabilidade social corporativa, outras).

    Redes sociais (Instagram, TikTok, Twitter/X) para chegar a estudantes novos

    -Páxina web con presentación do produto, capturas e acceso á descarga/demo
    -Posicionamento web SEO para termos como “aprender chinés”, “organizar vocabulario HSK”
    -Participación en comunidades online (Discords, foros de estudantes de chinés)
    -Posible colaboración con academias ou profesores de chinés para difusión
    
    1.2.	Xustifica a elección.
    
    Redes sociais e SEO permiten baixo custo e alta difusión orgánica, chegando directamente ao público obxectivo (estudantes autodidactas, alumnos de escolas, curiosos de linguas). Colaborar con profesionais do ensino de chinés daría credibilidade e visibilidade.
    
2.	Modelo de negocio.

    2.1.Modelo elixido (Modelo de pago / Freemium (é de balde pero as funcionalidades extras son de pago) / In house (desenvolvementos a medida para contornos empresariais / De subscrición / Por publicidade / Outros)
    
    Modelo Freemium + Subscrición.

    -Versión gratuíta básica para uso persoal (local, código aberto).
    -Versión premium (web) con acceso a funcionalidades avanzadas: exercicios automáticos, progreso, exportación masiva, máis chamadas á API, e posiblemente versións para academias.

    2.2. Xustifica a elección.

    O modelo freemium permite atraer usuarios sen barreiras iniciais e xerar comunidade. A subscrición sostén os custos do mantemento (servidor, API) e permite monetizar sen depender de publicidade nin comprometer a experiencia de usuario.