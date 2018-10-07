# TeletonHack

Sistema de monitoreo de donaciones en tiempo real que permite conocer el estado actual de las donaciones, 
permitiéndote conocer ¿Qué pasa con tus Donaciones?

## Problemática
En 2016 Teletón sufre la peor crisis económica en su historia, teniendo como resultado un recorte de aproximadamente 14000 empleados, 
traducido a la desaparición del turno vespertino, debido a la poca respuesta de los donantes.

En 2017 Teletón lanza la campaña "Visita un Teletón" con la finalidad de minimizar estos niveles de incertidumbres creados a partir de 
campañas extrañas en contra de Teletón.

Para Septiembre del 2017 con la situación del Terremoto del 19/09/2017 Teletón decide donar todo lo recaudado durante ese año en pro de 
hospitales, clínicas y espacios de rehabilitación afectados. 

Incrementando los números rojos dentro del presupuesto proyectado para el 2017.

## Planteamiento de la propuesta

Comenzamos con la limpieza y normalización de los datasets proporcionados, continuamos con un analisis estadístico que nos permió conocer 
a detalle el proceso de fondeo anual del Sistema Teletón.

La parte más interesante fue la interpretación de los datos la cuál pudimos corroborar con Roxana:

  * Teletón recibe donaciones en 2016 sin saber que el presupuesto proyectado de ese periodo sería hasta 2018.
  * De acuerdo al volumen de información proporcionada y analizada: Banamex es el medio más común para realizar una donación.
  ![Gráfica Entidades](https://user-images.githubusercontent.com/9124597/46584165-88a64980-ca25-11e8-968f-1b3f3982a247.png)
  * Nuestro público objetivo son Millenials.
  
 ## Propuesta
 
 Tomando en cuenta que actualmente ya se cuenta con distintos mecanismos de Transparencia en la página oficial de Teletón, tales como:
  * 5 Pasos para la Transparencia
  * Estados Financieros Combinados
  * Informe por Centro Teletón
  * Portal de Transparencia
  * Cuentas Claras 
 
 Tomando en cuenta que estos esfuerzos siguen sin despertar el interés del público objetivo proponemos un sistema de monitoreo, procesamiento y 
 análisis en Tiempo Real de todo el flujo de efectivo, desde el momento en que una perosna realiza su donativo hasta que se ve reflejado en 
 bienes/aparatos/tratamientos/salarios/etc. Esto existe actualmente en los esfuerzos mencionados anteriormente, sin embargo no han resultado ser
 el canal de comunicación efectivo, por ello más alla de mostrar las estadísticas, datos duros, que pudieran resultar complicados de interpretar
 optamos por un asistente inteligente capaz de mostrar exactamente lo mismo de una manera breve, clara y sencilla.
 
 Este asistente se encarga de ir a consultar la información directamente a los registros de las instancias proporcionados, consultar los estados
 financieros para conocer su trazabilidad, además de ayudarse de Qlik para interpretar en estadísticas reales y entendibles que le permitirá 
 proporcionar respuestas concretas, correctas y sin tener que instalar, abrir, descargar nada.  A partir de lo que el usuario/millenial ya conoce,
 ya tiene instalado, debido a que el asistente funge como una "interfaz" interactiva multiplataforma, puede operar en distintos canales simultaneamente.
 
 Pueden revisar el diagrama de funcionamiento de nuestra propuesta.
 
![diagramateleton](https://user-images.githubusercontent.com/9124597/46584171-9a87ec80-ca25-11e8-9b49-b40459f745fc.png)

## Esto hicimos en el hackatón...

Bueno llegamos y tardamos en entender la problemática y la solución que de verdad podría resolver el problema, más alla de hacer proyecciones de supuestos, presentar una herramienta que si bien la interfaz es sencilla, ha dado resultados comprobados para el mismo sector en distintas empresas tales como (Telmex, Dominos Pizza, Profeco, ect).

Hicimos:
 * Limpieza y Análisis de la Información proporcionada por Teletón (Python).
 * Normalización de la Información y comienzo de trabajo con Qlik.
 * Replanteamos los requerimientos que nos llevaran a una solución más alla de un dashboard.
 * Trabajo de Información con Qlik y Representación Gráfica.
 * Análisis del Target y las tecnologías que utilizan.
 * Diseño e Implementación de un API propia, la cuál ya está en Heroku, realizada con Flask.
 * Desarrollo de la "Interfaz Multiplataforma", Asistente Inteligente (Chatbot)
   * Implementación en DialogFlow.
   * Implementación de Firebase Functions (Para el API, Scrapping y Stripe)
   * Vinculación de Qlik con Firebase (Aun en eso)
   * Despliegue del Asistente en Multiples Plataformas (Fb Messenger y Assistant)
   
Decidimos utilizar DialogFlow ya que tiene mecanismos de aprendizaje continuo integrado, lo que nos permite ofrecer una ventana de "Pregunta lo que quieras" a los usuarios y aprender de cada una de las interacciones que tienen con él. 

De manera tal que podemos obtener de primera mano las inquietudes de nuestro target específico y diseñar estrategias puntuales.
   
## A futuro...
 * Nos gustaría mucho poder realizar donaciones desde el asistente aunque entendemos el lío que todo conlleva.
 * Estadísticas full RT 
 * Que fuera una solución REAL 
 
