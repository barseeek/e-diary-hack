# e-diary-hack
Скрипт предназначен для работы с электронным дневником. Он позволяет менять оценки ученика, удалять замечания и создавать похвалы.
Перед использованием скрипта настройте и запустите [сайт электронного дневника](https://github.com/devmanorg/e-diary/), скрипт положите в корневую папку с проектом сайта.

Ниже представлены сценарии использования.

## 1. Исправить оценки ученика
Поможет исправить плохие оценки у выбранного ученика, улучшив его успеваемость по журналу.
- Импортируйте необходимые модули и функции:
```python
from datacenter.models import Schoolkid
from datacenter.models import Mark
from functions import fix_marks
```
- Получите объект модели ученика, чьи оценки требуется исправить:
```python
pupil = Schoolkid.objects.get(full_name__contains="Фамилия Имя")
```
- Используйте функцию `fix_marks` для исправления оценок ученика:
```python
fix_marks(pupil)
```
Эта функция обработает все плохие оценки ученика (2 и 3) и изменит их на 5.
### Пример использования
Пример кода для исправления оценок ученика "Иванов Иван":
```python
from datacenter.models import Schoolkid
from functions import fix_marks

pupil_ivan = Schoolkid.objects.get(full_name__contains="Иванов Иван")
fix_marks(pupil_ivan)
```
## 2. Удалить замечания ученика
Позволит удалить замечания у выбранного ученика.
- Импортируйте необходимые модули и функции:
```python
from datacenter.models import Schoolkid
from datacenter.models import Chastisement
from functions import remove_chastisements
```
- Получите объект модели ученика, у которого нужно удалить замечания:
```python
pupil = Schoolkid.objects.get(full_name__contains="Фамилия Имя")
```
- Используйте функцию `remove_chastisements` для удаления замечаний ученика:
```python
remove_chastisements(pupil)
```
### Пример использования
Пример кода для исправления оценок ученика "Иванов Иван":
```python
from datacenter.models import Schoolkid
from functions import remove_chastisements

pupil_ivan = Schoolkid.objects.get(full_name__contains="Иванов Иван")
remove_chastisements(pupil_ivan)
```
## 3. Добавить похвалу для ученика
Позволит добавить похвалу по указанному предмету у выбранного ученика.
- Импортируйте необходимые модули и функции:
```python
from datacenter.models import Schoolkid
from datacenter.models import Commendation
from functions import create_commendation
```
- Получите объект модели ученика, для которого нужно добавить похвалу:
```python
pupil = Schoolkid.objects.get(full_name__contains="Фамилия Имя")
```
- Используйте функцию `create_commendation` для создания похвалы ученику::
```python
create_commendation("Фамилия Имя", "Название_предмета")
```
Эта функция создаст похвалу для выбранного ученика по выбранному предмету.

### Пример использования
Пример кода для создания похвалы у ученика "Иванов Иван" по предмету "Математика":
```python
from datacenter.models import Schoolkid
from functions import create_commendation

pupil_ivan = Schoolkid.objects.get(full_name__contains="Иванов Иван")
create_commendation(pupil_ivan.full_name, "Математика")
```
