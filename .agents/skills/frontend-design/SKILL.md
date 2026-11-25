---
name: frontend-design
description: 'Use when designing or reviewing professional frontend interfaces, visual hierarchy, design systems, responsive layouts, Tailwind CSS, reusable components, or loading, empty, error, and feedback states.'
when_to_use: 'Aplícala a tareas pertinentes dentro del alcance aprobado; no inicia agentes ni autoriza cambios.'
metadata:
  version: 0.1.0
---

# Frontend Design

Lee primero las instrucciones del repositorio y `project-profile.md` si existe. Respeta las decisiones del proyecto y la asignación de tu rol; esta skill aporta criterios técnicos, no inicia otro workflow ni amplía el alcance aprobado. Si hay conflicto, devuélvelo al coordinador.

## Cuándo utilizar esta skill

Actívala antes de crear una pantalla, rediseñar un flujo, definir componentes visuales o revisar responsive design. Es reutilizable en cualquier frontend; inspecciona primero el producto, sus usuarios, contenido, restricciones visuales y sistema existente.

## Procedimiento

1. Define la tarea principal de la pantalla y la acción primaria.
2. Inventaría los estados realistas: inicial, cargando, vacío, error, éxito y datos completos.
3. Establece una jerarquía visual antes de elegir decoración.
4. Reutiliza tokens y componentes existentes; crea un nuevo patrón solo si resuelve una necesidad repetida.
5. Construye primero el layout responsive y después ajusta detalles visuales.
6. Revisa teclado, contraste, tamaños táctiles y legibilidad antes de dar el diseño por terminado.

## Jerarquía y composición

- Da a cada pantalla un título claro, contexto breve y una acción primaria reconocible.
- Usa agrupación, espacio y orden visual para comunicar relación; no dependas solo del color.
- Limita la cantidad de acciones simultáneamente prominentes.
- Diseña el flujo más frecuente primero y deja acciones destructivas o secundarias claramente diferenciadas.
- Evita llenar cada zona con tarjetas: usa tablas, listas, secciones y texto cuando expresen mejor la información.

## Tipografía y espaciado

- Define una escala pequeña y consistente de tamaños, pesos, alturas de línea y espaciado.
- Usa el peso tipográfico para jerarquía, no múltiples familias o estilos sin propósito.
- Mantén anchos de lectura razonables para texto largo.
- Alinea controles y contenidos con una retícula coherente.
- No reduzcas el texto ni el área táctil para encajar más contenido; reorganiza el layout.

## Sistema visual

- Define roles de color: superficie, texto, borde, acción, información, éxito, advertencia y error.
- Usa color con una función comunicativa clara y acompáñalo de texto, icono o estructura.
- Evita gradientes, sombras fuertes, bordes redondeados excesivos y adornos que no ayuden a la tarea.
- Mantén estados hover, focus, active, disabled y error consistentes en todo el producto.
- Si existe un sistema de diseño, extiéndelo en lugar de crear valores aislados.

## Tailwind CSS (solo si el proyecto lo utiliza)

- Compón las clases a partir de la escala y patrones del proyecto; no introduzcas valores arbitrarios repetidos.
- Extrae un componente o una variante cuando una combinación de clases se repita con el mismo significado.
- Mantén las clases cerca del elemento cuando mejoren la lectura y mueve patrones complejos a una abstracción justificada.
- No uses Tailwind para esconder una estructura semántica incorrecta ni para sustituir una decisión de layout.
- Verifica que las variantes responsive y de estado no generen interfaces contradictorias.

## Responsive design

- Diseña desde el contenido y el ancho mínimo real, no desde un dispositivo concreto.
- Prioriza contenido y acciones; apila o transforma tablas y barras de herramientas cuando falte espacio.
- Evita scroll horizontal accidental y elementos que dependan solo de hover.
- Comprueba zoom, textos largos, datos vacíos y pantallas intermedias.
- Conserva objetivos táctiles cómodos y foco visible en todos los tamaños.

## Componentes y feedback

- Reutiliza componentes con contratos claros: un componente visual no debe conocer reglas de negocio.
- El estado de carga debe explicar qué se está esperando sin bloquear innecesariamente la interfaz.
- El estado vacío debe explicar la situación y ofrecer una siguiente acción útil.
- El estado de error debe describir el problema sin culpar al usuario y ofrecer recuperación.
- El éxito debe confirmarse cerca de la acción sin interrumpir el flujo salvo que sea necesario.
- Usa microinteracciones breves y funcionales; no animes información crítica ni añadas movimiento ornamental.

## Evitar el aspecto genérico

- Empieza por el contexto y la tarea, no por una plantilla de dashboard.
- Elige una composición y una escala visual coherentes con el producto; no combines patrones de tendencias sin criterio.
- Reduce elementos decorativos hasta que cada uno justifique su función.
- Revisa la interfaz con contenido realista, títulos largos y estados de error; una pantalla que solo funciona con datos ideales no está terminada.

## Revisión final

Comprueba jerarquía en una lectura rápida, consistencia entre pantallas, responsive, contraste, foco, feedback y claridad de la acción primaria. Valida el resultado en los estados no ideales, no solo en la vista feliz.
