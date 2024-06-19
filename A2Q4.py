import numpy as np

scores = [[80,90,70,85,95],
          [75,85,95,70,80],
          [85,95,75,80,90],
          [90,80,85,75,70]]

scores_array = np.array(scores)

avg_scores_subjects = np.mean(scores_array, axis=0) #axis = 0 means column wise average
print("Average ", avg_scores_subjects)

avg_scores_student = np.mean(scores_array, axis=1) #axis = 1 means row wise average
print("Highest average score across all subjects: ", avg_scores_student)

highest_score_student= np.argmax([avg_scores_student])
print("Index of highest scoring student:",highest_score_student)

highest_score_student_min_marks= np.argmin([avg_scores_student])
print("Index of highest scoring student who has scored least subject:",highest_score_student_min_marks)

