# -------------------------------
# Quiz Game Project
# Purpose: A multiple-choice quiz game that gives users up to 5 attempts per question.
# Features: Input, looping, decision-making, functions, lists, and scoring.
# -------------------------------

# Function to ask a quiz question
def ask_question(question_text, options_list, correct_answer):
    """
    Displays a question and options, checks the user's answer, 
    and returns 1 if correct or 0 if all attempts are used.
    """
    score_increase = 0
    max_attempts = 5
    attempt_number = 1

    # Loop through attempts
    while attempt_number <= max_attempts:
        print(f"\nAttempt {attempt_number}")
        print("Question:")
        print(question_text)
        print()

        # Display options from list
        for option in options_list:
            print(option)

        # Get user answer
        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        print()

        # Decision structure to check correctness
        if user_answer == correct_answer:
            print("✅ Correct!")
            score_increase = 1
            break
        else:
            if attempt_number < max_attempts:
                print("❌ That is not correct. Please try again.")
            attempt_number += 1

    # If out of attempts
    if score_increase == 0:
        print(f"You are out of chances! The correct answer was {correct_answer}.")

    return score_increase


# -------------------------------
# Main Program
# -------------------------------

print("Please enter a username:")
username = input()

print(f"\nWelcome, {username}!")
print("\nYou will get 5 chances for each question.\n")

# Initialize score (integer type)
total_score = 0

# -------------------------------
# Questions (8 Total)
# -------------------------------

question_1_text = "What vegetable was once considered poisonous in Europe?"
question_1_options = ["A) Tomato", "B) Eggplant", "C) Carrot", "D) Broccoli"]
correct_answer_1 = "A"

question_2_text = "What planet is known as the Red Planet?"
question_2_options = ["A) Venus", "B) Earth", "C) Mars", "D) Jupiter"]
correct_answer_2 = "C"

question_3_text = "Which ocean is the largest on Earth?"
question_3_options = ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"]
correct_answer_3 = "D"

question_4_text = "What gas do plants absorb from the atmosphere?"
question_4_options = ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"]
correct_answer_4 = "B"

question_5_text = "Which animal is known as the King of the Jungle?"
question_5_options = ["A) Elephant", "B) Lion", "C) Tiger", "D) Gorilla"]
correct_answer_5 = "B"

question_6_text = "What is the capital city of France?"
question_6_options = ["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"]
correct_answer_6 = "A"

question_7_text = "Which element has the chemical symbol 'O'?"
question_7_options = ["A) Gold", "B) Oxygen", "C) Silver", "D) Iron"]
correct_answer_7 = "B"

question_8_text = "How many continents are there on Earth?"
question_8_options = ["A) Five", "B) Six", "C) Seven", "D) Eight"]
correct_answer_8 = "C"

# -------------------------------
# Ask all questions
# -------------------------------
total_score += ask_question(question_1_text, question_1_options, correct_answer_1)
total_score += ask_question(question_2_text, question_2_options, correct_answer_2)
total_score += ask_question(question_3_text, question_3_options, correct_answer_3)
total_score += ask_question(question_4_text, question_4_options, correct_answer_4)
total_score += ask_question(question_5_text, question_5_options, correct_answer_5)
total_score += ask_question(question_6_text, question_6_options, correct_answer_6)
total_score += ask_question(question_7_text, question_7_options, correct_answer_7)
total_score += ask_question(question_8_text, question_8_options, correct_answer_8)

# -------------------------------
# Final Output
# -------------------------------
print(f"\nFinal Score for {username}: {total_score}/8")

# Optional grade percentage
percentage = (total_score / 8) * 100
print(f"Your grade: {percentage:.1f}%")

if percentage == 100:
    print("🌟 Perfect score! Amazing job!")
elif percentage >= 75:
    print("👍 Great work! You really know your stuff.")
elif percentage >= 50:
    print("🙂 Not bad — keep practicing!")
else:
    print("💪 Don’t give up! Try again to improve your score.")

print("\n🎉 Thanks for playing the quiz!")
