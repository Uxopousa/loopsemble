# Pruebas Angular

Usa esta guía solo si Angular y las APIs mencionadas están en uso y son compatibles con la versión del proyecto.

## Servicios Angular

- Usa el mecanismo de testing de Angular ya configurado para crear el entorno de inyección cuando el servicio dependa de DI.
- Prueba creación, actualización, eliminación, cambio de estado y errores de cada servicio.
- Sustituye `localStorage`, reloj, router o APIs externas por dependencias controlables.
- Verifica que un fallo de persistencia no se presenta como éxito y que el estado permanece coherente.
- Comprueba que las reglas se ejecutan en el servicio y no solo a través de un componente.

## Signals

- Lee la Signal después de cada operación pública que deba cambiarla.
- Prueba valores derivados con colección vacía, un elemento y combinaciones que puedan confundirse.
- Comprueba recomputación tras altas, ediciones, eliminaciones y cambios de estado.
- Verifica que no se expone una vía pública para mutar directamente el estado.
- Prueba `effect()` solo mediante su efecto observable, aislando temporizadores o persistencia cuando sea necesario.

## Vitest y Angular

Usa Vitest si ya está configurado por el proyecto. Respeta sus APIs y configuración; no mezcles sintaxis de otro runner ni añadas dependencias sin necesidad. Ejecuta el comando definido por el repositorio y, si falla por configuración o entorno, informa del fallo concreto en lugar de suavizarlo.
