def calculate_mean(heights):
    return sum(heights) / len(heights)

group_a_heights = [65, 68, 70, 72, 64, 67, 71, 66, 68, 69]
group_b_heights = [62, 64, 67, 68, 63, 65, 66, 61, 64, 67]

mean_height_group_a = calculate_mean(group_a_heights)
mean_height_group_b = calculate_mean(group_b_heights)

difference = mean_height_group_a - mean_height_group_b

print("Mean height of Group A:", mean_height_group_a)
print("Mean height of Group B:", mean_height_group_b)
print("Difference in mean heights:", difference)