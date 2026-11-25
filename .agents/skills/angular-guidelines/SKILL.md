---
name: angular-guidelines
description: 'Use when designing, implementing, reviewing, or refactoring Angular 21 applications with standalone components, Signals, dependency injection, Router, Reactive Forms, strict TypeScript, or modern Angular control flow.'
when_to_use: 'Aplícala a tareas pertinentes dentro del alcance aprobado; no inicia agentes ni autoriza cambios.'
metadata:
  version: 0.1.0
---

# Angular Guidelines

Lee primero las instrucciones del repositorio y `project-profile.md` si existe. Respeta las decisiones del proyecto y la asignación de tu rol; esta skill aporta criterios técnicos, no inicia otro workflow ni amplía el alcance aprobado. Si hay conflicto, devuélvelo al coordinador.

## Cuándo utilizar esta skill

Actívala para cualquier cambio de arquitectura, componente, página, servicio, formulario, ruta, estado o prueba en Angular 21. Antes de editar, inspecciona la versión de Angular, `tsconfig`, configuración de tests y estructura de la aplicación.

Esta guía está preparada para Angular 21. En versiones distintas, no apliques las APIs modernas automáticamente: verifica compatibilidad y convenciones en la documentación de la versión instalada. No migres Angular, formularios ni arquitectura como parte de aplicar la skill. Los ejemplos de incidencias son ilustrativos y no definen reglas del proyecto.

## Procedimiento

1. Identifica la responsabilidad de la pieza y sus consumidores antes de crearla.
2. Busca implementaciones, tipos y servicios existentes que puedan reutilizarse.
3. Decide dónde debe vivir la lógica: presentación en componentes, reglas reutilizables en servicios o funciones de dominio, y acceso externo en servicios de infraestructura.
4. Implementa el cambio con APIs compatibles con Angular 21.
5. Comprueba tipos, plantilla, navegación y pruebas del comportamiento afectado.

## Componentes standalone

- Crea componentes standalone y declara explícitamente sus `imports`.
- Mantén cada componente enfocado en una tarea visible y evita componentes contenedores gigantes.
- Usa `ChangeDetectionStrategy.OnPush` cuando el componente lo permita.
- Prefiere `input()` y `output()` para nuevas APIs de comunicación; usa decoradores existentes solo cuando el código del proyecto los requiera.
- No uses Signals como sustituto de `input()`/`output()`: las Signals representan estado reactivo; inputs y outputs expresan contratos entre componentes.

```ts
readonly issue = input.required<Issue>();
readonly removed = output<string>();
```

## Signals y estado

- Mantén el estado mutable encapsulado en una Signal privada y expón solo lecturas o valores derivados.
- Usa `computed()` para filtros, totales y cualquier valor que pueda calcularse a partir de otras Signals.
- Usa `effect()` únicamente para efectos externos inevitables, como persistencia o integración con APIs; no para propagar estado derivable.
- Evita duplicar el mismo estado en componentes y servicios.
- Para estado local de una vista, usa Signals locales; para estado compartido, usa un servicio con una responsabilidad clara.

```ts
private readonly issues = signal<Issue[]>([]);
readonly openIssues = computed(() =>
  this.issues().filter((issue) => issue.status === 'open')
);
```

No introduzcas una librería de estado global si Signals y servicios resuelven el caso.

## Servicios e inyección de dependencias

- Usa `@Injectable({ providedIn: 'root' })` para servicios compartidos por toda la aplicación.
- Inyecta dependencias con `inject()` en código nuevo cuando mejore la claridad.
- Separa el servicio que coordina reglas de negocio del que accede a almacenamiento, red o APIs del navegador.
- No accedas a `localStorage`, `HttpClient` o `Router` directamente desde componentes salvo que sea una necesidad explícita de presentación.
- Valida y tipa los datos recibidos de fuentes externas antes de incorporarlos al estado. Aplica los criterios de la skill `clean-code-architecture`, especialmente «Validación de objetos y reglas del modelo».

## Router

- Define rutas standalone cercanas a la funcionalidad que cargan.
- Usa rutas lazy cuando reduzcan el coste inicial sin añadir complejidad innecesaria.
- Trata parámetros ausentes, inválidos y recursos inexistentes explícitamente.
- Usa guards o resolvers solo para requisitos reales de acceso o carga; no los conviertas en una capa general de negocio.
- La navegación debe ser una decisión de la página o contenedor, no de un componente visual reutilizable.

## Reactive Forms

- Usa `ReactiveFormsModule` y formularios tipados para formularios no triviales.
- Centraliza validadores y reglas compartidas; el template solo presenta el estado.
- Marca controles como tocados al enviar para revelar errores de forma consistente.
- No confíes únicamente en la validación del formulario: el servicio debe proteger sus operaciones.
- Evita leer y escribir controles dispersos por múltiples componentes; crea un formulario reutilizable cuando el flujo de alta y edición comparta contrato.

## Template y comunicación

- Usa el control flow moderno: `@if`, `@for` y `@switch`.
- En `@for`, proporciona una clave estable con `track`, no el índice si los elementos pueden reordenarse o eliminarse.
- Mantén los templates declarativos; extrae condiciones complejas a `computed()` o funciones pequeñas y puras.
- Usa inputs para datos descendentes y outputs para eventos ascendentes.
- No uses eventos globales ni estado mutable compartido como atajo de comunicación.

## TypeScript estricto y rendimiento

- Conserva `strict`, evita `any` y no ocultes errores con casts innecesarios.
- Usa tipos unión para estados cerrados y guards para datos desconocidos.
- Evita suscripciones manuales cuando una Signal o `async` pipe resuelva el caso.
- Libera recursos de observables manuales con las APIs de ciclo de vida apropiadas.
- Evita trabajo costoso en cada render: calcula una vez con `computed()` o memoiza la transformación adecuada.
- Renderiza listas con `track`, usa imágenes optimizadas y carga diferida cuando el tamaño de la funcionalidad lo justifique.

## Revisión final

Confirma que el cambio mantiene una sola fuente de verdad, no duplica reglas, no mezcla presentación con infraestructura, funciona con navegación y estados vacíos, y tiene pruebas para el comportamiento nuevo o modificado.
