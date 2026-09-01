Descripcion del proyecto
Este proyecto implementa un sistema en Python para clasificar acciones de un jugador segun su tipo y duracion. Las categorias principales son Combate, Exploracion e Interaccion social, cada una con subclasificaciones basadas en tiempo y resultados.

Caracteristicas principales
Combate: Diferencia entre combates rapidos (< 100 seg) y combates de larga duracion (≥ 100 seg), clasificando ademas por resultado (Victoria o Derrota).

Exploracion: Clasifica entre exploracion con hallazgos o sin hallazgos, distinguiendo si fue breve (≤ 200 seg) o prolongada (> 200 seg).

Interaccion social: Evalua la duracion de la interaccion y la clasifica como leve, moderada o alta.

Historial: Guarda cada registro en un archivo historial.txt con informacion del usuario, accion, tiempo y clasificacion.

Estadisticas: Incluye una funcion para contar el numero de victorias de un jugador en el historial.

Uso
El programa solicita al usuario su nombre, la accion realizada y la duracion en segundos.

Segun la accion, pide informacion adicional (resultado del combate o hallazgos en exploracion).

Clasifica la accion y guarda el registro en historial.txt.

Permite consultar cuantas victorias tiene un jugador registrado.
