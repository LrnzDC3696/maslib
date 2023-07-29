from django.test import TestCase
from .models import Genre, Tag, Studio, Producer, Country, Show


class ModelTestCase(TestCase):
    def setUp(self):
        # Create some instances of the BaseModel subclasses
        self.genre = Genre.objects.create(name="Action")
        self.tag = Tag.objects.create(name="Thriller")
        self.studio = Studio.objects.create(name="Warner Bros.")
        self.producer = Producer.objects.create(name="Steven Spielberg")
        self.country = Country.objects.create(name="USA")

        # Create a Show instance
        self.show = Show.objects.create(
            title="Example Show",
            description="This is an example show.",
            format="tv_show",
            status="finished",
            episode_count=12,
            episode_duration=30,
            title_in_english="Example Show",
            title_in_native="Examplo Show",
            country_of_origin=self.country,
        )
        self.show.genres.add(self.genre)
        self.show.tags.add(self.tag)
        self.show.producers.add(self.producer)
        self.show.studio.add(self.studio)

    def test_show_model(self):
        # Test the Show model fields and relationships
        self.assertEqual(self.show.title, "Example Show")
        self.assertEqual(self.show.description, "This is an example show.")
        self.assertEqual(self.show.format, "tv_show")
        self.assertEqual(self.show.status, "finished")
        self.assertEqual(self.show.episode_count, 12)
        self.assertEqual(self.show.episode_duration, 30)
        self.assertEqual(self.show.title_in_english, "Example Show")
        self.assertEqual(self.show.title_in_native, "Examplo Show")
        self.assertEqual(self.show.country_of_origin, self.country)
        self.assertIn(self.genre, self.show.genres.all())
        self.assertIn(self.tag, self.show.tags.all())
        self.assertIn(self.producer, self.show.producers.all())
        self.assertIn(self.studio, self.show.studio.all())

    def test_model_str_method(self):
        # Test __str__ method of the models
        self.assertEqual(str(self.genre), "Action")
        self.assertEqual(str(self.tag), "Thriller")
        self.assertEqual(str(self.studio), "Warner Bros.")
        self.assertEqual(str(self.producer), "Steven Spielberg")
        self.assertEqual(str(self.country), "USA")
        self.assertEqual(str(self.show), "Example Show")
