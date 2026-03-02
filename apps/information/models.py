from django.db import models
from django.core.validators import MaxValueValidator


from localflavor.us.models import USStateField

class UniType(models.TextChoices):
    private = "private", "Private"
    public = "public", "Public"


class Category(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField(max_length=255)
    icon = models.ImageField(upload_to="category/icons/")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def  __str__(self):
        return self.name


class Major(models.Model):
    class HardType(models.TextChoices):
        easy = "easy", "Easy"
        hard = "hard", "Hard"
    name = models.CharField("Major name", max_length=255)
    hard_or_easy = models.CharField("Difficulty", max_length=10, choices=HardType.choices)
    popularity = models.BooleanField("Popular major", default=False)
    description = models.TextField("Major description", null=True, default="Information about the major")
    img = models.ImageField("Photo", upload_to="majors/images", default="location/default_image.png")


    def __str__(self):
        return self.name
    
class FamousPeople(models.Model):
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, related_name="famous")
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    description = models.TextField("Information about this person", default="Detailed information will be available here.")
    action = models.TextField("Notable actions in this field", default="Detailed information will be available here.")
    image = models.ImageField("Photo", upload_to="majors/images", default="location/default_image.png")
     



class University(models.Model):
    majors = models.ManyToManyField(Major,related_name="university")
    name = models.CharField("Name", max_length=255)
    location = USStateField()
    type = models.CharField("University type", max_length=100, choices=UniType.choices)
    dorm = models.BooleanField("Dormitory", default=False)
    price_out = models.DecimalField("Price", max_digits=10, decimal_places=2) #
    cost_of_living = models.DecimalField("Average cost", max_digits=10, decimal_places=2)
    latitude = models.FloatField("Latitude", default=0)
    longitude = models.FloatField("Longitude", default=0)
    icon = models.ImageField("Icon", upload_to="university/icons/", default="location/default_icon.png")
    detail = models.TextField("University story", default="Detailed information about our university will be available here.")
    image = models.ImageField("Photo", upload_to="university/images/", default="location/default_image.png")
    link = models.URLField(max_length=200, default="https://example.com")
    theme_color = models.CharField(
        "Theme color (hex)",
        max_length=7,
        default="#722F37",
        blank=True,
        help_text="Hex color for this university's detail page (e.g. #722F37 burgundy, #0f766e teal).",
    )


    def __str__(self):
        return self.name
    

    @property
    def geomap_longitude(self):
        return '' if self.longitude is None else str(self.longitude)
    
    @property
    def geomap_latitude(self):
        return '' if self.latitude is None else str(self.latitude)

    
    
class Admission(models.Model):
    class CompetitionType(models.TextChoices):
        easy = "easy", "Easy"
        normal = "normal", "Normal"
        high = "high", "High"
        extreme_high = "extreme_high", "Very high"

    uni_id = models.OneToOneField(University, on_delete=models.CASCADE)
    type_of_grades = models.CharField("Grade type", max_length=50)
    applicant_competition = models.CharField("Competition", max_length=20, choices=CompetitionType.choices)
    sat_range = models.PositiveSmallIntegerField("SAT score", validators=[MaxValueValidator(1600)])
    ielts = models.DecimalField("IELTS score", max_digits=2, decimal_places=1, validators=[MaxValueValidator(9.0)])
    acceptance_rate = models.PositiveSmallIntegerField("Acceptance rate", validators=[MaxValueValidator(100)])
    avg_gpa = models.DecimalField("GPA", max_digits=3, decimal_places=2, validators=[MaxValueValidator(4.0)])
    deadline = models.DateField("Deadline")
    
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
    fist_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    description = models.TextField("Professor information", default="Detailed information about the professor will be available here.")
    degree = models.TextField("Degree", default="Professor degree information")

    @property
    def first_name(self):
        """Display first name (model field is fist_name due to historical typo)."""
        return self.fist_name


# university.professors.all

class UniversityRating(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    # Other fields if needed

class Amina(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.ImageField("Photo",
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
    
class News(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    source = models.URLField(max_length=200, default="https://example.com")


