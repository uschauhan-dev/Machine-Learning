import numpy as np

group_a_heights = np.array([65, 68, 70, 72, 64, 67, 71, 66, 68, 69]) 
group_b_heights = np.array([62, 64, 67, 68, 63, 65, 66, 61, 64, 67])

print("difference between group a height and group b heights: ")
print(np.mean(group_a_heights)-np.mean(group_b_heights))