import numpy as np
from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt

n = 6
p = 0.1

X = binom(n, p)
x_values = np.arange(0, n + 1)

probabilities = X.pmf(x_values)

Z = {f'k={k}': [prob] for k, prob in zip(x_values, probabilities)}
distribution = pd.DataFrame.from_dict(Z, orient='index').T

print("=== Закон распределения ===\n")
pd.set_option('display.float_format', lambda x: f'{x:.6f}')
print(distribution)

M = X.mean()
D = X.var()
sqrt_D = np.sqrt(D)
max_prob = probabilities.max()
mode = [int(x) for x in x_values if round(probabilities[x], 6) == round(max_prob, 6)]

print("\n=== Числовые характеристики ===")
print(f"M = {M:.4f}")
print(f"D = {D:.4f}")
print(f"σ = {sqrt_D:.4f}")
print(f"Мода = {mode}")

plt.figure(figsize=(12, 6))
plt.plot(x_values, probabilities, marker='o', linestyle='-', color='b', label='P(X=k)')
plt.title('Многоугольник распределения Bin(6, 0.1)')
plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.xticks(range(0, min(21, n + 1), 2))
plt.xlim(0, 20)
plt.show()
