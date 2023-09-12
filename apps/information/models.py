from django.db import models
from django.core.validators import MaxValueValidator


from localflavor.us.models import USStateField

class UniType(models.TextChoices):
    private = "private", "Частный"
    public = "public", "Государственный"


class Category(models.Model):
    name = models.CharField("Название", max_length=255)
    slug = models.SlugField(max_length=255)
    icon = models.ImageField(upload_to="category/icons/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def  __str__(self):
        return self.name


class Major(models.Model):  
    class HardType(models.TextChoices):
        easy = "easy", "Легкий"
        hard = "hard", "Тяжело"
    name = models.CharField("Название факультета", max_length=255)
    hard_or_easy = models.CharField("Легко или сложно", max_length=10, choices=HardType.choices)
    popularity = models.BooleanField("Популярный факультет", default=False)
    description = models.TextField("Описание факультета", null=True, default="Информация об факультете")
    img = models.ImageField("Фото", upload_to="majors/images", default="location/default_image.png")


    def __str__(self):
        return self.name
    
class FamousPeople(models.Model):
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, related_name="famous")
    first_name = models.CharField("Название", max_length=255)
    last_name = models.CharField("Название", max_length=255)
    description = models.TextField("Информация об известном человеке", default="Подробная информация об известном человеке будет доступна здесь.")
    action = models.TextField("Знаменитые их действия в сторону этой профессии", default="Подробная информация об известном человеке будет доступна здесь")
    image = models.ImageField("Фото", upload_to="majors/images", default="location/default_image.png")
     



class University(models.Model):
    majors = models.ManyToManyField(Major,related_name="university")
    name = models.CharField("Название", max_length=255)
    location = USStateField()
    type = models.CharField("Тип университета", max_length=100, choices=UniType.choices)
    dorm = models.BooleanField("Жилые помещения", default=False)
    price_out = models.DecimalField("Цена", max_digits=10, decimal_places=2) # 
    cost_of_living = models.DecimalField("Средняя цена", max_digits=10, decimal_places=2)
    latitude = models.FloatField("Широта", default=0)
    longitude = models.FloatField("Долгота", default=0)
    icon = models.ImageField("Иконка", upload_to="university/icons/", default="location/default_icon.png")
    detail = models.TextField("Рассказ об университете", default="Подробная информация о нашем университете будет доступна здесь.")
    image = models.ImageField("Фото", upload_to="university/images/", default="location/default_image.png")
    link = models.URLField(max_length=200, default="https://example.com")



    def __str__(self):
        return self.name
    
    
class Admission(models.Model):
    class CompetitionType(models.TextChoices):
        easy = "easy", "Легко"
        normal = "normal", "Нормальный"
        high = "high", "Высокий"
        extreme_high = "extreme_high", "Очень высокая"

    uni_id = models.OneToOneField(University, on_delete=models.CASCADE)
    type_of_grades = models.CharField("Тип оценок", max_length=50)
    applicant_competition = models.CharField("Конкуренция", max_length=20, choices=CompetitionType.choices)
    sat_range = models.PositiveSmallIntegerField("SAT результаты", validators=[MaxValueValidator(1600)])
    ielts = models.DecimalField("IELTS результаты", max_digits=2, decimal_places=1, validators=[MaxValueValidator(9.0)])
    acceptance_rate = models.PositiveSmallIntegerField("Процент зачисления", validators=[MaxValueValidator(100)])
    avg_gpa = models.DecimalField("GPA", max_digits=3, decimal_places=2, validators=[MaxValueValidator(4.0)])
    deadline = models.DateField("Дедлайн")
    
    def __str__(self):
        return self.uni_id.name

class About(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name


class  Professor(models.Model):
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, related_name="professors")
    fist_name = models.CharField("Название", max_length=255)
    last_name = models.CharField("Название", max_length=255)
    description = models.TextField("Информация об профессоре", default="Подробная информация о профессоре будет доступна здесь.")
    degree = models.TextField("Какая степень", default="Здесь степень профессора")


# university.professors.all

class UniversityRating(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    # Другие поля, если нужно

class Amina(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.ImageField("Фото",
          upload_to="amina/images/", 
          null=True,blank=True
          )
    

class Review(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
    

