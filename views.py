from django.shortcuts import get_object_or_404, redirect, render
from .models import Choice, Course, Enrollment, Question, Submission


def extract_answers(request):
    submitted_answers = []
    for key in request.POST:
        if key.startswith("choice"):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)
    return submitted_answers


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
    submission = Submission.objects.create(enrollment=enrollment)
    choice_ids = extract_answers(request)
    submission.choices.set(choice_ids)
    submission.save()
    return redirect("onlinecourse:show_exam_result", course_id=course.id, submission_id=submission.id)


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_ids = submission.choices.values_list("id", flat=True)

    total_score = 0
    earned_score = 0
    for question in course.question_set.all():
        total_score += question.grade
        if question.is_get_score(selected_ids):
            earned_score += question.grade

    grade = int((earned_score / total_score) * 100) if total_score > 0 else 0
    context = {
        "course": course,
        "submission": submission,
        "selected_ids": list(selected_ids),
        "grade": grade,
        "earned_score": earned_score,
        "total_score": total_score,
    }
    return render(request, "onlinecourse/exam_result_bootstrap.html", context)
