---
name: testing
description: 'Use when planning, writing, or reviewing behavior tests, regression coverage, error paths, and integration contracts in any project. Select the existing runner and language conventions; use Angular-specific guidance only for Angular projects.'
when_to_use: 'Aplícala a tareas pertinentes dentro del alcance aprobado; no inicia agentes ni autoriza cambios.'
metadata:
  version: 0.1.0
---

# Testing

Lee primero las instrucciones del repositorio y `project-profile.md` si existe. Respeta las decisiones del proyecto y la asignación de tu rol; esta skill aporta criterios técnicos, no inicia otro workflow ni amplía el alcance aprobado. Si hay conflicto, devuélvelo al coordinador.

## Cuándo utilizar esta skill

Actívala cuando una tarea requiera diseñar, escribir o revisar pruebas de comportamiento, regresiones, integraciones o errores. Inspecciona primero el runner y la configuración existentes; no instales una herramienta ni cambies el runner para una prueba aislada.

## Estrategia

1. Define el comportamiento observable y el riesgo que quieres cubrir.
2. Localiza la unidad más pequeña que pueda probarlo sin perder realismo.
3. Para regresiones o nuevo comportamiento comprobable, demuestra que la prueba detecta el fallo antes de corregirlo cuando sea viable. No exijas pruebas nuevas para cambios sin riesgo de comportamiento.
4. Implementa solo las pruebas asignadas; las correcciones de producción corresponden al responsable autorizado. Un análisis de pruebas no autoriza a editar.
5. Ejecuta primero el test focalizado y después la suite relevante.
6. Revisa que la prueba no dependa de detalles internos innecesarios.

Prioriza pruebas de reglas de negocio, transformaciones, persistencia, validaciones y flujos críticos. No persigas cobertura por sí misma: una prueba debe detectar un fallo útil.

## Pruebas unitarias

- Nombra cada prueba con condición y resultado esperado.
- Arrange, Act, Assert: prepara datos, ejecuta una acción y verifica el resultado.
- Usa datos mínimos pero representativos y agrega casos límite deliberadamente.
- Comprueba resultados y efectos observables, no la implementación privada.
- Aísla dependencias externas con dobles de prueba tipados y verifica sus contratos.
- Evita tests frágiles basados en orden incidental, clases CSS o snapshots extensos.

## Guía según tecnología

Aplica los apartados siguientes solo cuando existan esas capacidades en el sistema. Para Angular, lee `references/angular-testing.md`; no traslades DI, Signals o Vitest a proyectos de otra tecnología. Para otros lenguajes, consulta las convenciones y documentación del runner real antes de usar sus APIs.

## Formularios

Prueba por separado:

- valores iniciales de alta y valores cargados en edición;
- campos obligatorios, espacios en blanco, límites mínimo y máximo;
- valores de enumeraciones inválidos;
- envío bloqueado cuando el formulario no es válido;
- envío válido con payload normalizado;
- visualización de errores tras intentar enviar;
- conservación de identificadores y fechas cuando se edita.

No pruebes únicamente que existe un `Validators.required`: prueba que el usuario no puede completar la operación inválida.

## Casos límite y errores

Incluye cuando aplique:

- colección vacía;
- búsqueda sin coincidencias;
- filtros combinados;
- títulos y descripciones en los límites exactos;
- texto con espacios exteriores o solo espacios;
- identificador inexistente;
- JSON inválido o datos persistidos con forma incorrecta;
- `localStorage` no disponible, bloqueado o lleno;
- doble acción rápida y resultado de una operación fallida.

## Revisión final

Confirma que las pruebas cubren comportamiento real, estados de error y regresiones plausibles; que son deterministas, legibles y rápidas; y que no obligan a cambiar producción solo para hacerlas pasar.
