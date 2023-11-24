def check_is_seller(user):
    try:
        _ = user.seller
        return True
    except Exception:
        return False


def check_is_operator(user):
    try:
        _ = user.operator
        return True
    except Exception:
        return False
