---
name: accessibility
description: 'Use when designing, implementing, or reviewing accessible frontend interfaces, semantic HTML, WCAG, keyboard navigation, focus management, contrast, forms, ARIA, responsive usability, or accessible error messages.'
when_to_use: 'Aplícala a tareas pertinentes dentro del alcance aprobado; no inicia agentes ni autoriza cambios.'
metadata:
  version: 0.1.0
---

# Accessibility

Lee primero las instrucciones del repositorio y `project-profile.md` si existe. Respeta las decisiones del proyecto y la asignación de tu rol; esta skill aporta criterios técnicos, no inicia otro workflow ni amplía el alcance aprobado. Si hay conflicto, devuélvelo al coordinador.

## Cuándo utilizar esta skill

Actívala para cualquier pantalla, componente, formulario, modal, navegación o revisión visual. Inspecciona el HTML, estados interactivos, orden de foco y contenido real antes de añadir ARIA.

## Procedimiento

1. Identifica la estructura semántica y el flujo principal de teclado.
2. Comprueba que cada control tiene nombre accesible, estado y propósito claros.
3. Revisa foco, orden de tabulación, contraste, zoom y responsive.
4. Añade ARIA solo cuando HTML nativo no exprese la semántica o relación necesaria.
5. Prueba teclado y lector de pantalla cuando sea posible, además de validaciones automatizadas.
6. Revisa estados de carga, vacío, error y éxito, no solo el estado inicial.

## HTML semántico y navegación

- Usa `header`, `nav`, `main`, `section`, `article`, `footer`, headings jerárquicos, listas y botones según su significado.
- Usa `<button>` para acciones y `<a>` para navegación; no conviertas un `div` en control con eventos.
- Mantén un único `main` identificable y un orden de headings que permita recorrer la página.
- Proporciona un enlace “Saltar al contenido” cuando la navegación persistente lo justifique.
- El orden DOM debe coincidir con el orden lógico y de lectura.
- No ocultes contenido necesario del árbol de accesibilidad ni uses `tabindex` positivo.

## Teclado y foco

- Toda acción disponible con ratón debe funcionar con teclado.
- Conserva un indicador de foco visible con contraste suficiente; no elimines `outline` sin una alternativa equivalente.
- Usa `Enter` y `Space` solo con controles nativos o patrones equivalentes bien definidos.
- En diálogos, mueve el foco al título o primer control, manténlo dentro mientras están abiertos y devuélvelo al disparador al cerrar.
- Tras navegación o eliminación, coloca el foco en el destino lógico y anuncia cambios relevantes.
- Evita trampas de teclado, hover como única interacción y áreas interactivas diminutas.

## Formularios

- Cada input debe tener un `<label>` asociado por `for`/`id`; el placeholder no sustituye al label.
- Explica formato, obligatoriedad y restricciones antes o junto al campo.
- Mantén el valor y el foco cuando sea posible tras un error.
- Asocia el mensaje de error con `aria-describedby` y marca el campo inválido con `aria-invalid="true"`.
- Resume errores del formulario en un lugar detectable sin mover el foco de forma inesperada.
- No uses solo color para comunicar error, estado, prioridad o éxito.

```html
<label for="title">Título</label>
<input id="title" name="title" aria-describedby="title-error" aria-invalid="true" />
<p id="title-error" role="alert">Escribe un título.</p>
```

## ARIA

- Prefiere HTML nativo antes que roles, estados o propiedades ARIA.
- Añade `aria-label` solo cuando no exista un nombre visible apropiado.
- Usa `aria-live` o `role="alert"` para mensajes dinámicos que deban anunciarse, con moderación.
- Mantén sincronizados `aria-expanded`, `aria-selected`, `aria-current`, `aria-busy` y otros estados con el estado visual.
- No asignes roles incompatibles ni uses ARIA para corregir una estructura HTML inválida.

## Contraste y presentación

- Verifica contraste de texto, controles, bordes necesarios e indicadores de foco según WCAG aplicable.
- No dependas de color, iconos sin texto o posición para transmitir información.
- Respeta zoom y tamaños de texto aumentados sin pérdida de contenido o funcionalidad.
- Permite reflow en pantallas estrechas y evita scroll horizontal accidental.
- Usa movimiento mínimo y respeta `prefers-reduced-motion` cuando haya animaciones.

## Responsive y usabilidad

- Diseña primero una experiencia usable con teclado, tacto y pantalla pequeña.
- Mantén objetivos táctiles suficientemente grandes y separados.
- No ocultes la acción principal en responsive; reorganízala de forma predecible.
- Comprueba tablas, formularios, mensajes largos y estados vacíos en anchos intermedios.
- El contenido debe seguir siendo comprensible sin CSS, imágenes o hover.

## Revisión final

Verifica semántica, nombres accesibles, teclado, foco, contraste, zoom, reflow, mensajes dinámicos y errores. Combina revisión manual con herramientas automatizadas, pero no trates un resultado automático sin errores como prueba completa de accesibilidad.
