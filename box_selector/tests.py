from django.test import TestCase
from .models import Product, Box
from .services import product_fits_box, recommend_box


class BoxSelectionTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2
        )

        self.small_box = Box.objects.create(
            name="Small Box",
            length=20,
            width=20,
            height=10,
            max_weight=5,
            cost=50
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            length=35,
            width=25,
            height=10,
            max_weight=5,
            cost=70
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            length=50,
            width=40,
            height=20,
            max_weight=10,
            cost=100
        )

    def test_product_fits_suitable_box(self):
        self.assertTrue(
            product_fits_box(self.product, self.medium_box)
        )

    def test_product_does_not_fit_small_box(self):
        self.assertFalse(
            product_fits_box(self.product, self.small_box)
        )

    def test_reject_box_when_weight_exceeds_capacity(self):
        heavy_product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=8
        )

        self.assertFalse(
            product_fits_box(heavy_product, self.medium_box)
        )

    def test_recommend_smallest_suitable_box(self):
        result = recommend_box(
            self.product,
            Box.objects.all()
        )

        self.assertEqual(result, self.medium_box)

    def test_no_suitable_box(self):
        oversized_product = Product.objects.create(
            name="Oversized Product",
            length=100,
            width=100,
            height=100,
            weight=50
        )

        result = recommend_box(
            oversized_product,
            Box.objects.all()
        )

        self.assertIsNone(result)