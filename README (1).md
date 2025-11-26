# Método de Euler y solución analítica de una Ecuación Diferencial Separable

Este repositorio contiene un ejemplo donde resolvemos la ecuación diferencial separable:

\[
\frac{dy}{dt} = y, \quad y(0) = 1
\]

La solución analítica es:

\[
y(t) = e^{t}
\]

Luego se aplica el método de Euler en el intervalo \([0,1]\) con paso \(h = 0.2\) para aproximar la solución y comparar ambas.

## Archivos incluidos

- **euler_separable.py** — Implementación en Python del método de Euler y comparación con la solución exacta.
- **README.md** — Explicación del problema, métodos y uso.

## Ejecución

```bash
python euler_separable.py
```
