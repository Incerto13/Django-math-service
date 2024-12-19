from django.http import JsonResponse
from django.utils import timezone
from .tasks import check_pythagorean_triplet
from typing import Dict

def triplet_view(request) -> JsonResponse:
    try:
        a = int(request.GET.get('a', ''))
        b = int(request.GET.get('b', ''))
        c = int(request.GET.get('c', ''))
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid input. Please provide integer values for a, b, and c."}, status=400)
    
    # Call the Celery task to check if it's a Pythagorean triplet and calculate the product
    result = check_pythagorean_triplet.apply_async(args=[a, b, c])

    current_datetime = timezone.now()

    is_triplet, product = result.get(timeout=10)  # adjust timeout as needed

    if is_triplet:
        response_data = {
            "datetime": current_datetime,
            "a": a,
            "b": b,
            "c": c,
            "is_triplet": True,
            "product": product,
        }
    else:
        response_data = {
            "datetime": current_datetime,
            "a": a,
            "b": b,
            "c": c,
            "is_triplet": False,
            "message": "The numbers do not form a Pythagorean triplet.",
        }

    return JsonResponse(response_data)
