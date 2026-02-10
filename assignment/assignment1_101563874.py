"""
Author: Adeniyan Ayooluwa David
Assignment: #1
"""

# Variable: string
gym_member = "Alex Alliton"

# Variable: float
preferred_weight_kg = 20.5

# Variable: integer
highest_reps = 25

# Variable: boolean
membership_active = True


# Dictionary data type storing friends and their workout minutes
workout_stats = {
    "Alex": (30, 45, 20),     # yoga, running, weightlifting
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 40)
}

# Calculate total workout minutes for each friend
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes


# 2D list (nested list) containing workout minutes for each friend
workout_list = [
    workout_stats["Alex"],
    workout_stats["Jamie"],
    workout_stats["Taylor"]
]

# Extract and print yoga and running minutes for all friends
print("Yoga and Running minutes for all friends:")
for workouts in workout_list:
    print(workouts[0:2])

# Extract and print weightlifting minutes for the last two friends
print("\nWeightlifting minutes for the last two friends:")
for workouts in workout_list[-2:]:
    print(workouts[2])


# Check if any friend has total workout minutes >= 120
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")


# User input feature
friend_name = input("\nEnter a friend's name: ")

if friend_name in workout_stats:
    if not friend_name.endswith("_Total"):
        minutes = workout_stats[friend_name]
        total = workout_stats[f"{friend_name}_Total"]
        print(f"\nWorkout details for {friend_name}:")
        print(f"Yoga: {minutes[0]} minutes")
        print(f"Running: {minutes[1]} minutes")
        print(f"Weightlifting: {minutes[2]} minutes")
        print(f"Total: {total} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")


# Determine highest and lowest total workout minutes
totals = {
    "Alex": workout_stats["Alex_Total"],
    "Jamie": workout_stats["Jamie_Total"],
    "Taylor": workout_stats["Taylor_Total"]
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"\nFriend with the highest total workout minutes: {highest_friend}")
print(f"Friend with the lowest total workout minutes: {lowest_friend}")
