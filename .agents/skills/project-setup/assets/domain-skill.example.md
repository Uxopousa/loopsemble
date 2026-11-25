---
name: project-domain
description: 'Sustituye por el dominio concreto, las operaciones y reglas que activan esta skill, y las consultas que quedan fuera.'
metadata:
  version: 0.1.0
---

# [Nombre del dominio]

Modelo de autoría: completa y revisa antes de instalarlo como `SKILL.md` en el directorio de la skill elegida. Este archivo de ejemplo no es una skill de dominio activa.

## Activación y límites

[Acciones de implementación, análisis o revisión a las que aplica. Incluye ejemplos que no deben activarla. No autoriza cambios ni inicia agentes. Respeta el plan y la asignación del coordinador.]

## Fuentes canónicas

[Rutas desde la raíz del proyecto y apartados concretos. Resuelve esas rutas desde la raíz, no desde el directorio de la skill. No inventes rutas ni dupliques requisitos completos.]

## Contrato y reglas que proteger

[Entidades e invariantes confirmados, con fuente por regla. Resume solo lo necesario para orientar al agente; consulta la fuente para los detalles. Distingue reglas del negocio de decisiones técnicas.]

## Procedimiento

1. Lee las fuentes y el código afectado; identifica las reglas y los consumidores implicados.
2. Contrasta la operación con las invariantes, precondiciones y efectos confirmados.
3. Mantén las reglas en la capa que corresponda a la arquitectura real, sin imponer frameworks ni nuevas capas.
4. Revisa casos aceptados, rechazados y límites pertinentes; aplica la skill de testing seleccionada cuando proceda.
5. Informa de conflictos o requisitos ausentes; no resuelvas decisiones de producto por tu cuenta ni declares éxito ante un fallo.

## Ejemplos de aplicación

[Entrada o estado, acción, resultado esperado, regla y fuente. Usa ejemplos sintéticos confirmados que permitan detectar una interpretación incorrecta.]

## Incertidumbre y cambios

[Qué falta decidir y qué operaciones dependen de ello. Un requisito contradictorio bloquea solo el trabajo afectado. Ante cambios de requisitos, revisa esta guía y sus ejemplos; no cambies fuentes para hacerlas coincidir con la implementación.]

## Criterios de revisión

[Comprobaciones concretas de las reglas del dominio y evidencia esperada. Separa lo revisado en documentos de lo comprobado en código o mediante ejecución.]
