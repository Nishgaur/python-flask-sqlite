import requests
import matplotlib.pyplot as plt

# Fetching the data from the API created in scoreapi.py
response = requests.get('http://127.0.0.1:5000/student_scores')
score_data = response.json()

# Extracting scores from the fetched data to perform further steps
scores = [score['Marks'] for score in score_data]

# Calculating the average score of the students
average_score = sum(scores) / len(scores)

print("The average score has been calculated as: ", average_score)

# Visualizing the data using a bar chart from the data
plt.figure(figsize=(8, 6))
plt.bar(range(len(scores)), scores, color='skyblue')
plt.axhline(average_score, color='red', linestyle='--', label=f'Average Score: {average_score:.2f}')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.title('Student Test Scores')
plt.legend()
plt.tight_layout()
plt.show()

print("The visulization has been performed successfully!")
