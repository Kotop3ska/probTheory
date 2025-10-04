import random
import plotly.graph_objects as go
import numpy as np
from math import comb

# Классическая вероятность
total_ways = comb(50, 25)
favorable = 2 * comb(40, 15)
classical_prob = favorable / total_ways

print(f"Классическая вероятность: {classical_prob:.6f}")

# Частотное моделирование
max_N = 100000
step = 500  
N_values = list(range(step, max_N + 1, step))
freq_values = []

dogs_template = ['border collie'] * 10 + ['X'] * 40
success_count = 0


for i in range(1, max_N + 1):
    dogs = dogs_template[:]
    random.shuffle(dogs)
    day1 = dogs[:25]
    if day1.count('border collie') == 10 or day1.count('border collie') == 0:
        success_count += 1
    
    if i % step == 0:
        freq = success_count / i
        freq_values.append(freq)

final_freq = success_count / max_N
print(f"Количество экспериментов: {max_N}")
print(f"Успехов: {success_count}")
print(f"Частотная вероятность: {final_freq:.6f}")

diff = abs(classical_prob - final_freq)
print(f"Разница: {diff:.6f}")

print("\n" + "-" * 32)
print(f"{'Метод':<15} | {'Вероятность':<12}")
print("-" * 32)
print(f"{'Классический':<15} | {classical_prob:<12.6f}")
print(f"{'Частотный':<15} | {final_freq:<12.6f}")
print("-" * 32)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=N_values,
    y=freq_values,
    mode='lines',
    name='Частота',
    line=dict(color='blue', width=2)
))

fig.add_trace(go.Scatter(
    x=N_values,
    y=[classical_prob] * len(N_values),
    mode='lines',
    name='Вероятность',
    line=dict(color='red', width=2, dash='dash')
))

fig.update_layout(
    title='Сходимость частоты к теоретической вероятности',
    xaxis_title='N (количество экспериментов)',
    yaxis_title='P(A)',
    width=700,
    height=400,
    legend=dict(
        x=0.95,
        y=0.95,
        bgcolor='rgba(255,255,255,0.8)',
        bordercolor='black',
        borderwidth=1
    ),
    margin=dict(l=0, r=0, t=30, b=0)
)

fig.show()
