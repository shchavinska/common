import unittest
from homework import Rectangle


class TestRectangle(unittest.TestCase):

    def test_get_rectangle_perimeter(self):
        self.assertEqual(Rectangle(10, 20).get_rectangle_perimeter(), 60)

    def test_get_rectangle_square(self):
        self.assertEqual(Rectangle(10, 20).get_rectangle_square(), 200)

    def test_get_sum_of_corners_valid(self):
        self.assertEqual(Rectangle(10, 20).get_sum_of_corners(4), 360)

    def test_get_sum_of_corners_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 5).get_sum_of_corners(5)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(Rectangle(3, 4).get_rectangle_diagonal(), 5)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(Rectangle(3, 4).get_radius_of_circumscribed_circle(), 2.5)

    def test_get_radius_of_inscribed_circle_valid(self):
        self.assertEqual(Rectangle(5, 5).get_radius_of_inscribed_circle(), 2.5)

    def test_get_radius_of_inscribed_circle_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 4).get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
