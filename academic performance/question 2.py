import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("academic_performance.csv")  # Replace with your filename
sns.set(style="whitegrid")

#1. SGPA Comparison by Gender -----------
plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='SGPA', data=df, palette='pastel')
plt.title('SGPA (Secondary School GPA) by Gender')
plt.xlabel('Gender')
plt.ylabel('SGPA')
plt.show()

#  2. Final CGPA Comparison by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='CGPA', data=df, palette='Set2')
plt.title('Final CGPA by Gender')
plt.xlabel('Gender')
plt.ylabel('CGPA')
plt.show()

cgpa_long = df.melt(id_vars=['Gender'],
                    value_vars=['CGPA100', 'CGPA200', 'CGPA300', 'CGPA400'],
                    var_name='Year', value_name='CGPA')

cgpa_long['Year'] = cgpa_long['Year'].map({
    'CGPA100': 'Year 1',
    'CGPA200': 'Year 2',
    'CGPA300': 'Year 3',
    'CGPA400': 'Year 4'
})

plt.figure(figsize=(10, 6))
sns.lineplot(data=cgpa_long, x='Year', y='CGPA', hue='Gender', marker='o', linewidth=2.5)
plt.title('CGPA Progression Over 4 Years by Gender')
plt.xlabel('Academic Year')
plt.ylabel('CGPA')
plt.show()
