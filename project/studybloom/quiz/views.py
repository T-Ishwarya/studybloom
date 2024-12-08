from django.shortcuts import render, redirect
from .models import Quiz, Question, Answer
from .forms import AnswerForm


def quiz_list(request):
    # This view will show a list of available quizzes.
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    # This view will show the quiz questions and handle form submission.
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        # Check the answers
        for question in questions:
            selected_answer = request.POST.get(f"question_{question.id}")
            correct_answer = question.answers.filter(is_correct=True).first()
            if selected_answer == str(correct_answer.id):
                score += 1

        # Redirect to the results page
        return redirect('quiz_results', quiz_id=quiz.id, score=score)

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})


def quiz_results(request, quiz_id, score):
    # This view will show the score after quiz submission.
    quiz = Quiz.objects.get(id=quiz_id)
    return render(request, 'quiz/quiz_results.html', {'quiz': quiz, 'score': score})
