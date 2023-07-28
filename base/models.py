# movies/models.py
from django.db import models


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
