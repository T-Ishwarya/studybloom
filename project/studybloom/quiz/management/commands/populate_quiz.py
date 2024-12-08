# quiz/management/commands/populate_quiz.py
from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question, Answer

class Command(BaseCommand):
    help = 'Populate quiz with questions and answers'

    def handle(self, *args, **kwargs):
        # Create a quiz
        quiz = Quiz.objects.create(name="General Knowledge")

        # Add questions
        question1 = Question.objects.create(quiz=quiz, text="What is the capital of France?")
        question2 = Question.objects.create(quiz=quiz, text="Who is the inventor of Python language?")
        question3 = Question.objects.create(quiz=quiz, text="In which year was Python invented?")
        question4 = Question.objects.create(quiz=quiz, text="What are the molecules present in the air?")

        # Add answers for question 1
        Answer.objects.create(question=question1, text="Paris", is_correct=True)
        Answer.objects.create(question=question1, text="Berlin", is_correct=False)
        Answer.objects.create(question=question1, text="Madrid", is_correct=False)
        Answer.objects.create(question=question1, text="Lisbon", is_correct=False)

        # Add answers for question 2
        Answer.objects.create(question=question2, text="Guido van Rossum", is_correct=True)
        Answer.objects.create(question=question2, text="Dennis Ritchie", is_correct=False)
        Answer.objects.create(question=question2, text="James Gosling", is_correct=False)
        Answer.objects.create(question=question2, text="Bjarne Stroustrup", is_correct=False)

        # Add answers for question 3
        Answer.objects.create(question=question3, text="1991", is_correct=True)
        Answer.objects.create(question=question3, text="1989", is_correct=False)
        Answer.objects.create(question=question3, text="1995", is_correct=False)
        Answer.objects.create(question=question3, text="2000", is_correct=False)

        # Add answers for question 4
        Answer.objects.create(question=question4, text="Oxygen, Nitrogen, Carbon Dioxide", is_correct=True)
        Answer.objects.create(question=question4, text="Oxygen, Hydrogen, Neon", is_correct=False)
        Answer.objects.create(question=question4, text="Nitrogen, Argon, Methane", is_correct=False)
        Answer.objects.create(question=question4, text="Helium, Xenon, Krypton", is_correct=False)

        self.stdout.write(self.style.SUCCESS('Successfully populated the quiz with questions and answers'))
