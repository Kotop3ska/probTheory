import numpy as np
from scipy.stats import hypergeom
import pandas as pd
import matplotlib.pyplot as plt

N = 40  
M = 9    
n = 12  

X = hypergeom(N, M, n)

x_values = np.arange(0, min(M, n) + 1) 

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

print("\n=== Числовые характеристики ===\n")
print(f"M(X) = {M:.4f}")
print(f"D(X) = {D:.4f}")
print(f"σ = {sqrt_D:.4f}")
print(f"Мода = {mode}")

plt.figure(figsize=(12, 6))
plt.plot(x_values, probabilities, marker='o', linestyle='-', color='g', label='P(X=k)')
plt.title('Гипергеометрическое распределение числа редких табличек')
plt.xlabel('k (число редких табличек в выборке)')
plt.ylabel('P(X=k)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
