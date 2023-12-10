import random
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Subject


def fix_marks(schoolkid: Schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    if bad_marks.count() == 0:
        raise Exception(
            "Не нашел плохих оценок для ученика, проверьте корректность данных"
        )
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    return bad_marks.count()


def remove_chastisements(schoolkid: Schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    if chastisements.count() == 0:
        raise Exception(
            "Не нашел замечаний для ученика, проверьте корректность данных"
        )
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(fullname: str, subject_name: str):
    phrases = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    try:
        kid = Schoolkid.objects.get(full_name__contains=fullname)
        subject = Subject.objects.get(
            title=subject_name,
            year_of_study=kid.year_of_study
        )
        subject_lessons = Lesson.objects.filter(
            subject=subject,
            group_letter=kid.group_letter,
            year_of_study=kid.year_of_study
        )
        return Commendation.objects.create(
            text=random.choice(phrases),
            created=subject_lessons.first().date,
            schoolkid=kid,
            subject=subject, teacher=subject_lessons.first().teacher
        )
    except Schoolkid.DoesNotExist:
        print("Не могу найти ученика, проверьте корректность ФИО")
    except Subject.DoesNotExist:
        print("Не могу найти предмет, проверьте корректность ввода")
