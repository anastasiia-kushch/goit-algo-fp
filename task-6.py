




items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    ratio_items = [(name, item['cost'], item['calories'], item['calories'] / item['cost']) for name, item in items.items()]

    ratio_items.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for name, cost, calories, ratio in ratio_items:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return chosen_items, total_calories


def dynamic_programming(budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    item_list = list(items.items())
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, item = item_list[i - 1]
            cost = item["cost"]
            calories = item["calories"]
            
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    chosen_items = []
    total_cost = budget
    for i in range(n, 0, -1):
        if dp[i][total_cost] != dp[i - 1][total_cost]:
            item_name, item = item_list[i - 1]
            chosen_items.append(item_name)
            total_cost -= item["cost"]
    
    return chosen_items, dp[n][budget]

budget = 100
print("\nGreedy algorithm:")
chosen_items_greedy, total_calories_greedy = greedy_algorithm(budget)
print(f"Chosen items: {chosen_items_greedy}")
print(f"Total calories: {total_calories_greedy}\n")

print("Dynamic programming:")
chosen_items_dp, total_calories_dp = dynamic_programming(budget)
print(f"Chosen items: {chosen_items_dp}")
print(f"Total calories: {total_calories_dp}\n")