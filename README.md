# Loopsemble

Flujo coordinado de agentes y skills para Codex.

Pack 0.3.0 para proyectos nuevos o existentes. Incluye ocho skills, Planner, Developer,
Reviewer y dos especialistas opcionales: `security-reviewer` y `test-specialist`.

Las skills incluidas son `project-setup`, `team-workflow`, `clean-code-architecture`,
`frontend-design`, `testing`, `accessibility`, `angular-guidelines` y
`systematic-debugging`. El setup selecciona
las pertinentes y contrasta duplicidades y conflictos con el entorno. Angular está
orientada a versión 21; frontend y accesibilidad son para interfaces web; testing
usa el runner existente. Estar instalada no obliga a usarla en todas las tareas.

Si alguna ruta ya existe, el instalador se detiene para revisar cómo integrar las
versiones sin sobrescribirlas. Las skills de dominio son específicas de cada proyecto
y no se distribuyen con el pack: para crearlas hacen falta datos explícitos del
proyecto de destino.

Durante `$project-setup` puedes elegir crear una skill de dominio propia. El proceso
reutiliza requisitos existentes o recoge reglas y ejemplos por chat o mediante
`.agents/skills/project-setup/assets/domain-brief.example.md`. Te devuelve las reglas
para confirmar, propone nombre y ubicación, y usa `domain-skill.example.md` como modelo.
Comprueba fuentes, coherencia, activación, ejemplos válidos/rechazados/límite y límites
del rol. Los borradores incompletos no se activan; el perfil registra las validaciones
y las pruebas de comportamiento pendientes. La skill creada pertenece al proyecto y
se conserva al actualizar o retirar el pack.

## 1. Instalar

Descomprime el pack fuera del repositorio y crea o identifica la raíz del proyecto.
Requiere **Python 3.9+**; no instala dependencias ni configura permisos.

```sh
python3 /ruta/al/pack/scripts/install.py /ruta/absoluta/al/proyecto
```

En Linux, macOS o WSL con Bash también puedes usar:

```sh
bash /ruta/al/pack/install.sh /ruta/absoluta/al/proyecto
```

En Windows nativo usa `py -3` en lugar de `python3`. El instalador copia solo las skills y agentes declarados, sin instalar otras configuraciones
que pudieran existir en el paquete. Valida los archivos
obligatorios antes de copiar, rechaza destinos ocupados y enlaces, verifica la copia
y revierte lo creado ante errores normales o interrupciones capturables. No puede
revertir un corte eléctrico o SIGKILL: consulta la recuperación descrita más abajo.

| Destino relativo a la raíz      | Contenido                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| `.agents/skills/project-setup/` | Setup, modelos de brief y perfil, guías de mantenimiento.                               |
| `.agents/skills/team-workflow/` | Orquestación y workflows de pruebas y seguridad.                                        |
| `.codex/agents/`                | Cinco TOML, uno por rol; no se reemplazan agentes existentes.                           |
| `.agent-workflow-install.json`  | Versión, inventario con hashes y origen relativo si el pack estaba dentro del proyecto. |

Las seis skills técnicas también se copian a `.agents/skills/<nombre>/`, con sus metadatos y referencias.

## 2. Configurar en Codex

Abre la raíz del proyecto en una sesión nueva de Codex e invoca **`$project-setup`**.
Puedes responder por chat o copiar `.agents/skills/project-setup/assets/project-brief.example.md`
a `project-brief.md` en esa raíz y completarlo. El setup verifica la ubicación y revisa
los documentos, las tecnologías y las skills disponibles.

Necesita objetivo y usuarios, alcance inicial, límites y un criterio de éxito para la
primera tarea. Requisitos, arquitectura y roadmap pueden aportarse por chat o mediante
documentos existentes; lo que no sea necesario aún queda pendiente, sin inventarlo.

Si faltan, el setup ofrece crearlos como documentos opcionales a partir de los modelos
`requirements.example.md`, `architecture.example.md` y `roadmap.example.md`, incluidos
en `.agents/skills/project-setup/assets/`. Puedes elegir cualquiera o aplazarlos.
Propone `docs/requirements.md`, `docs/architecture.md` y `docs/roadmap.md`, comprueba
que no haya equivalentes ni conflictos y guarda las rutas acordadas en el perfil.

También incluye modelos opcionales de plan de trabajo, estado de ejecución, informe de
revisión, modelo de amenazas, estrategia de pruebas y decisión de arquitectura (ADR).
El setup recomienda solo los pertinentes y propone destinos adaptados al proyecto;
puedes elegir cualquiera, reutilizar equivalentes o aplazarlos. Guardar un plan o un
estado no aprueba su ejecución. Los documentos creados pertenecen al proyecto y se
conservan al retirar el pack.

El setup guarda `project-profile.md`, propone el bloque de integración de `AGENTS.md`
y solicita las decisiones de visibilidad: configuración versionada para el equipo o
local mediante `.git/info/exclude` (sin modificar reglas compartidas). Puede usarse
`.gitignore` si quieres que la exclusión se comparta. Ignorar un archivo ya versionado
no lo retira del índice: esa acción requiere otra decisión explícita.

Confirma que Codex carga las ocho skills y reconoce los **cinco agentes**. Si algo falta,
consulta `.agents/skills/project-setup/references/maintenance.md`. Que los archivos estén
en disco no prueba su carga. El setup también ofrece borrar, ignorar o conservar el
pack original si estaba dentro del proyecto, después de verificar las copias instaladas.

## 3. Trabajar

Con el bloque de `AGENTS.md` aprobado, pide una tarea en lenguaje natural:

```text
Añade exportación CSV. Usa trabajo paralelo si hay tareas independientes.
```

El coordinador inicia el flujo, Planner propone un plan y tú lo apruebas antes de editar.
Developer implementa, Reviewer inspecciona y los hallazgos aceptados se corrigen y vuelven
a revisar, con hasta dos rondas. Los agentes asignados no reinician la orquestación.
También puedes invocar `$team-workflow` explícitamente si no se activa.

Los especialistas se seleccionan por riesgo: pruebas para regresiones, cobertura o
integraciones; seguridad para datos sensibles, entradas externas o límites de confianza.
Si Reviewer descubre un riesgo, el coordinador solicita análisis especializado sin
necesitar que repitas la petición. Cambios de alcance o nuevas escrituras no aprobadas
vuelven a decisión humana. Las preguntas y explicaciones no arrancan implementación.

El paralelo requiere herramientas de delegación disponibles y habilitadas, y tareas
independientes. Cada agente recibe directorio y archivos asignados. Un worktree o clon
separa archivos; crear una rama en un checkout compartido no lo hace. También pueden
trabajar sobre archivos disjuntos, considerando salidas generadas y lockfiles. El setup
comprueba las claves admitidas por la versión de Codex; la documentación actual usa
`agents.enabled` y `agents.max_concurrent_threads_per_session`. No modifica esa
configuración sin aprobación. Los subagentes heredan los permisos de la sesión: los
TOML no crean un sandbox de solo lectura propio.

## Actualizar, recuperar o retirar

El instalador realiza primeras instalaciones; las actualizaciones siguen siendo manuales.
La desinstalación está automatizada con vista previa y aplicación explícita:

```sh
python3 /ruta/al/proyecto/.agents/agent-workflow/uninstall.py /ruta/absoluta/al/proyecto
python3 /ruta/al/proyecto/.agents/agent-workflow/uninstall.py /ruta/absoluta/al/proyecto --apply
```

La copia instalada funciona aunque se haya borrado el template original. Desde el pack
también puedes usar `bash uninstall.sh /ruta/absoluta/al/proyecto [--apply]`.
Se retiran solo archivos registrados sin cambios; se conservan los personalizados y
el registro para reintentar si la retirada es parcial. Revisa después las referencias
al flujo en `AGENTS.md` y las reglas de Git. No se modifican documentos ni skills propias.

El registro permite comparar hashes e identificar personalizaciones antes de combinar
una versión nueva o retirar archivos. Conserva perfil, brief y documentos del usuario.

Si una instalación quedó interrumpida de forma abrupta, revisa inventario y hashes con
Codex; elimina solo archivos parciales verificados tras elegir la recuperación y vuelve
a instalar. No borres carpetas completas de agentes o skills. Las instrucciones están
en `.agents/skills/project-setup/references/maintenance.md`.

Para reanudar una tarea, recupera el plan, la aprobación y la evidencia actual. Si no
puede acreditarse la aprobación, el flujo vuelve a presentar el plan. El perfil no
autoriza cambios por sí solo.

La activación de skills y los límites de roles son instrucciones dependientes del
cliente. El pack se dirige a Codex; su funcionamiento completo debe verificarse en la
interfaz donde se use. Los tests del instalador se ejecutan con:

```sh
python3 -m unittest discover -s tests -v
```

## Conexión entre agentes y skills

El coordinador asigna las skills relevantes en cada tarea siguiendo
`.agents/skills/team-workflow/references/skill-routing.md`: dominio y clean code para
planificación y lógica, frontend y accesibilidad para interfaces, Angular cuando sea
compatible, testing para pruebas y diagnóstico sistemático ante fallos. Reviewer usa
las mismas reglas aplicables al revisar; los especialistas conservan sus límites.
La verificación final vincula cada criterio con evidencia de la revisión definitiva.
