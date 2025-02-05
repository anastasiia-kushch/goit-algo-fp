import random
import matplotlib.pyplot as plt

num_rolls = 100000
sums_count = {i: 0 for i in range(2, 13)}

for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll_sum = die1 + die2
    sums_count[roll_sum] += 1

probabilities = {sum_value: count / num_rolls * 100 for sum_value, count in sums_count.items()}


print("Ймовірності кожної суми за методом Монте-Карло:")
print(f"{'Сума':<8} {'Ймовірність (%)':<10}")
print("-" * 25)

for sum_value, prob in probabilities.items():
    print(f"{sum_value:<8} {prob:<15.2f}")

theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89,
    9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

x = list(probabilities.keys())
monte_carlo_probs = list(probabilities.values())
theoretical_probs = [theoretical_probabilities[sum_value] for sum_value in x]

plt.figure(figsize=(10, 6))
plt.bar(x, monte_carlo_probs, width=0.4, label="Метод Монте-Карло", align='center', color='blue', alpha=0.6)
plt.bar(x, theoretical_probs, width=0.4, label="Аналітичні ймовірності", align='edge', color='red', alpha=0.6)
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння ймовірностей сум при киданні двох кубиків")
plt.legend()
plt.show()
