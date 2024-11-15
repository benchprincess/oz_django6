from logging import raiseExceptions

from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    # get을 할 필요가 없는 이유
    #     - Foriegn key contraint가 있기 때문에
    #  user_id:
    #       _ 이 id의 user가 실제로 있는 경우
    #       -실제로 없는 경우
    # article_id:
    #       - 이 id의 article이
    likes = list(Like.objects.filter(user_id=user_id, article_id=article_id))
    if likes:
        raise Exception
    return Like.objects.create(user_id=user_id, article_id=article_id)
