from django.test import SimpleTestCase
from django.urls import reverse

class Message_Page_Test(SimpleTestCase):
    
    def test_url_exist_at_corrent_location(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("message"))
        self.assertEqual(response.status_code, 200)
        
    def test_teplate_name(self):
        response = self.client.get(reverse("message"))
        self.assertTemplateUsed(response, "Home.html")
        
    # def test_teplate_content(self):
    #     response = self.client.get("/message/")
    #     self.assertContains(response, "<h1>JJ</h1>")
        