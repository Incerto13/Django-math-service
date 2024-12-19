from celery import shared_task
from typing import Tuple, Optional

@shared_task
def check_pythagorean_triplet(a: int, b: int, c: int) -> Optional[Tuple[bool, int]]:
    """
    Check if a, b, c form a Pythagorean triplet and return the product.
    If they form a valid triplet, return True and the product.
    Otherwise, return False and None.
    """
    if a**2 + b**2 == c**2:
        return True, a * b * c
    return False, None
