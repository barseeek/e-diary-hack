import random
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from django.db import connection, reset_queries


PHRASES = [
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


def num_queries(reset=True):
    print(len(connection.queries))
    if reset:
        reset_queries()


def get_schoolkid(fullname: str):
    try:
        return Schoolkid.objects.get(full_name__contains=fullname)
    except Schoolkid.DoesNotExist:
        raise Exception(
            "Не нашел ученика, проверьте корректность данных"
        )
    except Schoolkid.MultipleObjectsReturned:
        raise Exception(
            "Нашел больше одного ученика, проверьте корректность данных"
        )


def fix_marks(schoolkid: Schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    if bad_marks.exists():
        return bad_marks.update(points=5)
    else:
        raise Exception(
            "Не нашел плохих оценок для ученика, проверьте корректность данных"
        )


def remove_chastisements(schoolkid: Schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    if chastisements.exists():
        return chastisements.delete()
    else:
        raise Exception(
            "Не нашел замечаний для ученика, проверьте корректность данных"
        )


def create_commendation(fullname: str, subject_name: str):
    kid = get_schoolkid(fullname)
    random_subject_lesson = Lesson.objects.filter(
        subject__title=subject_name,
        group_letter=kid.group_letter,
        year_of_study=kid.year_of_study
    ).order_by('?').first()
    if random_subject_lesson:
        return Commendation.objects.create(
            text=random.choice(PHRASES),
            created=random_subject_lesson.date,
            schoolkid=kid,
            subject=random_subject_lesson.subject,
            teacher=random_subject_lesson.teacher
        )
    else:
        raise Exception(
            "Не могу найти урок по предмету, проверьте корректность ввода"
        )
