from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=50, inventory=50) 

        self.client = APIClient()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()

        # serialize queryset
        serializer = MenuSerializer(menu_items, many=True)

        # compare serialized data with response.data
        self.assertEqual(response.data, serializer.data)