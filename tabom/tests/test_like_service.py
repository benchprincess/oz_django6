from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        like = do_like(user.id, article.id)

        # then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    # def test_a_user_can_like_an_article_only_once(self) -> None:
    #     # given
    #     user = User.objects.create(name="test")
    #     article = Article.objects.create(title="test_title")
    #
    #     # Except
    #     like1 = do_like(user.id, article.id)
    #     with self.assertRaises(Exception):
    #         lik2 = do_like(user.id, article.id)