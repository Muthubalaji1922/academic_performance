#Classify students into academic success categories (e.g., high achievers, average, and struggling) based on their cumulative grade points (SGPA, CGPA100, CGPA200, CGPA300, CGPA400)? give the visualization code
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('academic_performance.csv')
def classify_student(row):
    if row['CGPA400'] >= 3.5:
        return 'High Achiever'
    elif 2.5 <= row['CGPA400'] < 3.5:
        return 'Average'
    else:
        return 'Struggling'
data['Category'] = data.apply(classify_student, axis=1)
category_counts = data['Category'].value_counts()

# Visualization
plt.figure(figsize=(8, 6))
category_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Academic Success Categories')
plt.xlabel('Category')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()