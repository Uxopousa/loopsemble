# Perfil del flujo de trabajo del proyecto

Sustituye los campos entre corchetes por hechos observados, decisiones de la persona usuaria, «ninguno» o una decisión pendiente identificada. Guarda el perfil en la raíz del repositorio como `project-profile.md`. Un elemento pendiente solo bloquea las tareas que dependan de él.

- Propósito y alcance permitido: [descripción; enlaza los requisitos si existen]
- Modo y estado del setup: [proyecto nuevo o existente; listo o con decisiones pendientes identificadas]
- Fuentes de entrada: [decisiones del chat y rutas de documentos revisados; indica correcciones pendientes]
- Documentos canónicos del proyecto: [rutas de requisitos, arquitectura y roadmap, o herramientas existentes; decisiones sobre creación opcional y asuntos sin resolver]
- Documentos opcionales de coordinación y especialidad: [rutas elegidas para plan, estado de ejecución, informe de revisión, modelo de amenazas, estrategia de pruebas y ADR; responsables y mantenimiento, o si se aplazan/rechazan]
- Arquitectura y convenciones: [rutas a arquitectura, AGENTS.md u otras instrucciones]
- Tecnologías: [lenguaje, framework, estilos, runtime y herramientas de pruebas; marca cada una como observada con rutas de evidencia o prevista con la fuente de la decisión]
- Skills disponibles y procedencia: [nombre → fuente o ubicación → propósito pertinente → cómo invocarla]
- Skills de estilo seleccionadas: [nombre → tecnología o preocupación → cuándo aplicarla]
- Skill de dominio del proyecto: [nombre y ubicación existente/elegida, fuentes canónicas, decisiones confirmadas, estado de borrador o lista, controles de calidad y evaluación pendiente; o aplazada]
- Agentes especialistas opcionales: [disponibilidad de security-reviewer y test-specialist; disparadores de uso y restricciones propias del proyecto]
- Skills ausentes o propuestas: [tecnología o preocupación → guía necesaria → acción propuesta; no afirmes que están disponibles]
- Conflictos entre skills e instrucciones: [fuentes → reglas incompatibles → efecto práctico → decisión del desarrollador o pendiente]
- Seguimiento de tareas: [ruta e identificadores estables, o «ninguno»; explica cómo se registra el progreso]
- Criterios de finalización: [criterios observables de aceptación, revisión y evidencia]
- Contexto de seguridad: [política, modelo de amenazas, activos sensibles/límites de confianza o «no documentado»; no inventes]
- Comprobaciones: [comandos exactos para código, documentación y configuración; indica cuándo aplica cada uno]
- Archivos o sistemas que no deben modificarse: [lista o «ninguno»]
- Límites del trabajo en paralelo: [estrategia permitida con worktree/rama, reglas para archivos compartidos y máximo de desarrolladores concurrentes; usa «solo en serie» si no está disponible]
- Comprobación de capacidades del entorno: [cliente Codex, descubrimiento de agentes personalizados, delegación habilitada, soporte para checkout/worktree compartido y shell; evidencia o estado sin verificar]
- Valores predeterminados del flujo: [serie por defecto, paralelo optativo, permisos y límites de agentes solo si están disponibles y son necesarios]
- Decisiones opcionales de ajuste: [solo preferencias propias del proyecto solicitadas o necesarias; en otro caso, «valores predeterminados aceptados»]
- Responsable de integración: [coordinador o rol; indica quién resuelve conflictos y ejecuta las comprobaciones finales]
- Visibilidad del flujo instalado: [versionado o local; .git/info/exclude o .gitignore compartido; rutas afectadas y acciones Git pendientes]
- Ubicación y limpieza de la plantilla fuente: [ruta fuera del repositorio, eliminada, ignorada, conservada o pendiente de decisión]

No guardes secretos ni credenciales personales en este perfil.
