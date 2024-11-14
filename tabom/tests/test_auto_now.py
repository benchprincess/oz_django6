from django.test import TestCase

from tabom.models import User


class TestAutoNow(TestCase):
    def test_auto_now_field_is_set_when_save(self) -> None:
        user = User(name="test")
        user.save()
        self.assertIsNotNone(user.updated_at)
        self.assertIsNotNone(user.created_at)
