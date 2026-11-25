# Estrategia de pruebas

Modelo opcional. Destino sugerido: `docs/testing/strategy.md`. Reutilizar la configuración y guías existentes. Describe las verificaciones; no instala herramientas ni constituye evidencia de ejecución.

- Alcance y fuentes: [comportamientos y riesgos relevantes.]
- Herramientas actuales: [configuración y versiones observadas; propuestas claramente separadas.]

| Riesgo o comportamiento | Nivel de prueba                                                   | Escenarios y resultado esperado                 | Comando y entorno                                |
| ----------------------- | ----------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------ |
| [Contrato observable]   | [Unidad, componente, integración o extremo a extremo justificado] | [Casos normales, errores y límites pertinentes] | [Comando verificado o pendiente; datos aislados] |

- Evidencia y cierre: [qué resultados se requieren y dónde se registran.]
- Fallos preexistentes y pruebas inestables: [evidencia y actuación acordada.]
- Límites y pendientes: [qué no se cubre y por qué.]

Evitar pruebas que solo reflejen la implementación, cobertura duplicada y dependencia de servicios o datos reales sin autorización.
