from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    # get을 할 필요가 없는 이유
    #     - Foriegn key contraint가 있기 때문에
    #  user_id:
    #       _ 이 id의 user가 실제로 있는 경우
    #       -실제로 없는 경우

    return Like.objects.create(user_id=user_id, article_id=article_id)
