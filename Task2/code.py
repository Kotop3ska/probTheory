import random
import matplotlib.pyplot as plt
from math import comb

# Классическое определение

total_ways = comb(50, 25)
favorable = 2 * comb(40, 15)
classical_prob = favorable / total_ways

print(f"Классическая вероятность: {classical_prob:.6f}")

# Частотное определение

num_experiments = 100000
dogs = ['border collie'] * 10 + ['X'] * 40
success_count = 0

for _ in range(num_experiments):
    random.shuffle(dogs)
    day1 = dogs[:25]
    day2 = dogs[25:]
    if day1.count('border collie') == 10 or day1.count('border collie') == 0:
        success_count += 1

experimental_freq = success_count / num_experiments

print(f"Количество экспериментов: {num_experiments}")
print(f"Успехов: {success_count}")
print(f"Частотная вероятность: {experimental_freq:.6f}" )

diff = abs(classical_prob - experimental_freq)
print(f"Разница: {diff:.6f}")

print("\n" + "-" * 32)
print(f"{'Метод':<15} | {'Вероятность':<12} ")
print("-" * 32)
print(f"{'Классический':<15} | {classical_prob:<12.6f} ")
print(f"{'Частотный':<15} | {experimental_freq:<12.6f} ")
print("-" * 32)

methods = ['Классический', 'Частотный']
probs = [classical_prob, experimental_freq]
colors = ['blue', 'red']

plt.figure(figsize=(8, 5))
bars = plt.bar(methods, probs, color=colors, edgecolor='black', alpha=0.8)

for bar, prob in zip(bars, probs):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + max(probs) * 0.02,
        f'{prob:.6f}',
        ha='center',
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

plt.title('Сравнение классической и частотной вероятностей\n(все 10 собак породы бордер колли в один день)', fontsize=14)
plt.ylabel('Вероятность', fontsize=12)
plt.ylim(0, max(probs) * 1.3)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
