from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Genre(BaseModel):
    pass


class Tag(BaseModel):
    pass


class Studio(BaseModel):
    pass


class Producer(BaseModel):
    pass


class Country(BaseModel):
    pass


class Show(models.Model):
    FORMAT_CHOICES = (
        ("movie", "Movie"),
        ("tv_show", "TV Show"),
    )

    STATUS_CHOICES = (
        ("finished", "Finished"),
        ("airing", "Airing"),
        ("not_yet_aired", "Not Yet Aired"),
        ("cancelled", "Cancelled"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    episode_count = models.PositiveIntegerField()
    episode_duration = models.PositiveIntegerField()  # In minutes

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title_in_english = models.CharField(max_length=100, null=True, blank=True)
    title_in_native = models.CharField(max_length=100, null=True, blank=True)
    title_synonyms = models.CharField(max_length=200, null=True, blank=True)

    genres = models.ManyToManyField(Genre, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    producers = models.ManyToManyField(Producer, blank=True)
    studio = models.ManyToManyField(Studio, blank=True)

    country_of_origin = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ("-title",)

    def __str__(self):
        return self.title


class UserShowList(models.Model):
    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("watching", "Watching"),
        ("planning", "Planning"),
        ("paused", "Paused"),
        ("dropped", "Dropped"),
    )

    NOT_SCORED = None  # Use None to represent "not scored"
    SCORE_CHOICES = [
        (NOT_SCORED, "Not Scored"),
        (1, "1 - Very Poor"),
        (2, "2 - Poor"),
        (3, "3 - Below Average"),
        (4, "4 - Average"),
        (5, "5 - Above Average"),
        (6, "6 - Good"),
        (7, "7 - Very Good"),
        (8, "8 - Great"),
        (9, "9 - Excellent"),
        (10, "10 - Masterpiece"),
    ]

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="show_list"
    )
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="planning")
    progress = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(
        null=True, blank=True, choices=SCORE_CHOICES, default=NOT_SCORED
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    start_date = models.DateField(null=True, blank=True)
    complete_date = models.DateField(null=True, blank=True)

    favorite = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user_id", "show_id")

    def __str__(self):
        return f"{self.user.username}'s Show List: {self.show.title}"
