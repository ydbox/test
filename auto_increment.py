BM = 0


def auto_increment():
    """Return a sequentially incrementing number starting at 5,300,001."""
    global BM
    start = 5300001
    interval = 1
    if BM == 0:
        BM = start
    else:
        BM += interval
    return BM
