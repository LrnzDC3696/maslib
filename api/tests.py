from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Show


class ShowAPITestCase(APITestCase):
    def setUp(self):
        self.show_data = {
            "title": "Example Show",
            "description": "This is an example show.",
            "format": "tv_show",
            "status": "finished",
            "episode_count": 12,
            "episode_duration": 30,
            "title_in_english": "Example Show",
            "title_in_native": "Examplo Show",
        }
        self.show = Show.objects.create(**self.show_data)

    def test_list_shows(self):
        url = reverse("api-v1:listcreate")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], self.show_data["title"])

    def test_create_show(self):
        url = reverse("api-v1:listcreate")
        response = self.client.post(url, data=self.show_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Show.objects.count(), 2)  # Check that a new show is added

    def test_retrieve_show(self):
        url = reverse("api-v1:detailcreate", kwargs={"pk": self.show.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.show_data["title"])

    def test_update_show(self):
        updated_data = self.show_data.copy()
        updated_data["title"] = "Updated Show"
        url = reverse("api-v1:detailcreate", kwargs={"pk": self.show.id})
        response = self.client.put(url, data=updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Show")
        self.show.refresh_from_db()  # Refresh the object from the database
        self.assertEqual(self.show.title, "Updated Show")

    def test_delete_show(self):
        url = reverse("api-v1:detailcreate", kwargs={"pk": self.show.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Show.objects.count(), 0)  # Check that the show is deleted
