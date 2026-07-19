grade_book = {
    "Alice": 75,
    "Bob": 92,
    "Charlie": 85,
    "Diana": 89,
    "Ethan": 70,
    "Leslie": 95,
    "Fiona": 95
}


total_score = 0
for score in grade_book.values():
    total_score += score


class_average = total_score / len(grade_book)
print(f"Class average: {class_average}")

highest_score = max(grade_book.values())
lowest_score = min(grade_book.values())

top_scorers = [name for name, score in grade_book.items() if score == highest_score]
bottom_scorers = [name for name, score in grade_book.items() if score == lowest_score]

print(f"Top Scorer(s): {', '.join(top_scorers)} with a score of {highest_score}")
print(f"Bottom Scorer(s): {', '.join(bottom_scorers)} with a score of {lowest_score}")


search_name = input("\nEnter a student's name to check their score: ")

grade = grade_book.get(search_name)

if grade is not None:
    print(f"{search_name}'s score is: {grade}")
else:
    print(f"Student {search_name} is not found in the grade book.Thank you for searching. Please check the spelling and try again.")