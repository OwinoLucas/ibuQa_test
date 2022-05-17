from django.test import TestCase
from .models import *
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.
class OrderTests(APITestCase):
    def post_order(self):
        url = reverse("create-order-item")
        data = {
            "item" : "lemon chilli peppers",
            "amount" : "35000",
        }
        response = self.client.post(url, data)
        return response
    
    def test_post_order_item(self):
        response = self.post_order()
        assert response.status_code == status.HTTP_201_CREATED
        assert Order.objects.count() == 1

    def test_update_order_item(self):
        response = self.post_order()
        data = {"item" : "lemon chilli peppers"}
        url_1 = reverse("order", kwargs={"pk": response.data["id"]})
        put_response= self.client.put(url_1, data)
        assert put_response.status_code  == status.HTTP_200_OK
        assert put_response.data["item"]  == data["item"]
        put_response_2 = self.client.put(url_1)
        assert put_response_2.status_code == status.HTTP_400_BAD_REQUEST
        url_2 = reverse("order", kwargs={"pk": 100})
        put_response_3= self.client.put(url_2)
        assert put_response_3.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_order(self):
        response_1 = self.post_order()
        url_1 = reverse("order", kwargs={"pk" : response_1.data["id"]})
        response_2 = self.client.delete(url_1)
        assert response_2.status_code == status.HTTP_204_NO_CONTENT
        response_3 = self.client.delete(url_1)
        assert response_3.status_code == status.HTTP_404_NOT_FOUND