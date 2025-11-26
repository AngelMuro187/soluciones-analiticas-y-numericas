import math

def f(t, y):
    """Ecuación diferencial: dy/dt = y"""
    return y

def exact_solution(t):
    """Solución analítica de dy/dt = y, y(0)=1 → y(t)=e^t"""
    return math.exp(t)

def euler(f, y0, t0, h, n_steps):
    """Método de Euler explícito"""
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0

    for _ in range(n_steps):
        y = y + h * f(t, y)
        t = t + h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values

def main():
    t0 = 0.0
    y0 = 1.0
    h = 0.2
    t_final = 1.0

    n_steps = int((t_final - t0) / h)

    t_vals, y_euler = euler(f, y0, t0, h, n_steps)

    print("Aproximación con método de Euler para dy/dt = y, y(0)=1")
    print(f"h = {h}, intervalo t ∈ [{t0}, {t_final}]")
    print("-" * 60)
    print(f"{'t':>6} | {'y_euler':>15} | {'y_exacta':>15} | {'error':>15}")
    print("-" * 60)

    for t, y_num in zip(t_vals, y_euler):
        y_ex = exact_solution(t)
        error = abs(y_ex - y_num)
        print(f"{t:6.2f} | {y_num:15.8f} | {y_ex:15.8f} | {error:15.8f}")

if __name__ == "__main__":
    main()
