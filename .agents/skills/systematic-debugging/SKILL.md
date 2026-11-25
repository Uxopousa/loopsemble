---
name: systematic-debugging
description: Investigates bugs, regressions, failing tests, builds and unexpected behavior through reproduction, evidence, hypotheses and focused verification. Use before proposing a fix; respects the assigned role and approved change scope without restarting orchestration.
when_to_use: 'Use for diagnosis during planning, implementation failures, or review findings. Analysis does not authorize production edits.'
metadata:
  version: 0.1.0
---

# Diagnóstico de fallos

Lee las instrucciones del proyecto, su perfil y el alcance de la tarea. Si ya tienes una fase asignada, no inicies otro ciclo de agentes ni solicites de nuevo una aprobación acreditada. La investigación puede ser de solo lectura; modificar producción o pruebas requiere la autorización y propiedad de archivos correspondientes.

1. Describe el síntoma, el resultado esperado y cómo reproducirlo. Inspecciona errores completos, versiones, configuración y cambios recientes. Distingue fallos del producto, del entorno y preexistentes.
2. Intenta reproducir con la entrada mínima y comandos reales del proyecto. Registra resultado y condiciones. Si no puedes observar el fallo, informa de esa limitación y reúne evidencia antes de proponer un parche.
3. Sigue el flujo de datos hasta la frontera donde se rompe el contrato. Compara con un caso equivalente que funcione; no atribuyas una causa únicamente al último archivo modificado.
4. Formula una hipótesis comprobable y busca una observación que la confirme o descarte. Cambia una variable cada vez. Si necesitas instrumentación, mantenla dentro del alcance y evita registrar secretos o datos personales.
5. Propón una corrección ligada a la causa observada. Si cambia el alcance aprobado, vuelve al coordinador antes de editar. Una vez autorizado, aplica un cambio focalizado y una prueba de regresión cuando cubra un riesgo real.
6. Repite la reproducción y las comprobaciones afectadas. Comprueba que la prueba detecta el fallo cuando sea viable y que el arreglo no oculta otro error. No debilites validadores ni elimines pruebas para obtener un resultado positivo.

Ante intentos repetidos sin progreso, detén los parches especulativos y presenta evidencia, hipótesis descartadas y el dato o decisión que falta. Respeta el límite de rondas del workflow. No hagas cambios en sistemas externos ni operaciones destructivas para diagnosticar sin autorización.

Devuelve: síntoma y reproducción, evidencia de causa o hipótesis pendiente, archivos afectados, resultado real de cada comprobación y límites. «No reproducido» y «corregido pero no verificado» son resultados distintos de «resuelto».
