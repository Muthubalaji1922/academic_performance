import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('academic_performance.csv')
print(df.head())
sns.set(style="whitegrid")

# CGPA distribution
plt.figure(figsize=(10,6))
sns.histplot(df['CGPA'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Final CGPA', fontsize=16)
plt.xlabel('CGPA')
plt.ylabel('Count')
plt.show()

# Boxplot: CGPA by Gender
plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='Gender', y='CGPA', palette='pastel')
plt.title('CGPA Distribution by Gender', fontsize=16)
plt.xlabel('Gender')
plt.ylabel('CGPA')
plt.show()

# Scatter Plot: SGPA vs Final CGPA
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='SGPA', y='CGPA', hue='Gender', palette='deep')
plt.title('Relationship Between Secondary School GPA and Final CGPA', fontsize=16)
plt.xlabel('Secondary School GPA (SGPA)')
plt.ylabel('Final CGPA')
plt.legend(title='Gender')
plt.show()

# 4. Lineplot
progression_df = df.melt(id_vars=['ID No'], 
                         value_vars=['CGPA100', 'CGPA200', 'CGPA300', 'CGPA400'],
                         var_name='Year', value_name='CGPA_Yearly')

plt.figure(figsize=(12,6))
sns.lineplot(data=progression_df, x='Year', y='CGPA_Yearly', estimator='mean', ci=None, marker='o')
plt.title('Average CGPA Progression Over 4 Years', fontsize=16)
plt.xlabel('Year of Study')
plt.ylabel('Average CGPA')
plt.show()

# Average CGPA per Program Code
plt.figure(figsize=(14,6))
program_avg = df.groupby('Prog Code')['CGPA'].mean().reset_index().sort_values('CGPA', ascending=False)
sns.barplot(data=program_avg, x='CGPA', y='Prog Code', palette='viridis')
plt.title('Average Final CGPA by Program', fontsize=16)
plt.xlabel('Average CGPA')
plt.ylabel('Program Code')
plt.show()
