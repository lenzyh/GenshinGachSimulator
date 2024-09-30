# %%
import random

# Simulates the capture mechanic after losing the 50/50 chance
def simulate_gacha_v1(num_draws, banner_chance=50, capture_chance=10):
    state_list = []
    for _ in range(num_draws):
        if random.choices([0, 1], [50, 50])[0] == 0:  # Lost the 50/50
            # Chance to capture the banner character
            result = random.choices([0, 1], [100 - capture_chance, capture_chance])[0]
            state_list.append(result)
        else:
            state_list.append(1)  # Won the 50/50
    return state_list

# Progressive pity where chance increases after losing multiple times
def simulate_gacha_v2(num_draws):
    state_list = []
    lose_streak = 0  # Tracks how many times we lost
    for _ in range(num_draws):
        if lose_streak == 0:
            # Base 50/50 chance
            result = random.choices([0, 1], [50, 50])[0]
        elif lose_streak == 1:
            # Second loss, still 50/50
            result = random.choices([0, 1], [50, 50])[0]
        elif lose_streak == 2:
            # Third loss, increased to 75% chance
            result = random.choices([0, 1], [25, 75])[0]
        else:
            # Fourth time, guaranteed banner
            result = 1
        
        if result == 1:
            lose_streak = 0  # Reset the lose streak if we win
        else:
            lose_streak += 1  # Increment the lose streak if we lose
        
        state_list.append(result)
    
    return state_list

# Helper function to calculate and print the percentage of getting the banner
def calculate_percentage(results):
    banner_count = sum(results)  # Count how many times we got the banner (1s)
    total_draws = len(results)   # Total number of draws
    percentage = (banner_count / total_draws) * 100  # Calculate percentage
    return percentage
# Run the simulator
num_draws = 1000000
results_v1 = simulate_gacha_v1(num_draws)
results_v2 = simulate_gacha_v2(num_draws)


# Print the results
##print("Version 1 Results:", results_v1)
print(f"Version 1: {calculate_percentage(results_v1):.2f}% banner 5-star rate")

##print("Version 2 Results:", results_v2)
print(f"Version 2: {calculate_percentage(results_v2):.2f}% banner 5-star rate")



# %%
import pandas as pd
# Count occurrences of 0 and 1 for both versions
count_v1 = pd.Series(results_v1).value_counts()
count_v2 = pd.Series(results_v2).value_counts()

# Create a DataFrame for the results
results_df = pd.DataFrame({
    'Version': ['Version 1', 'Version 2'],
    'Count of 0': [count_v1.get(0, 0), count_v2.get(0, 0)],
    'Count of 1': [count_v1.get(1, 0), count_v2.get(1, 0)]
})

results_df


