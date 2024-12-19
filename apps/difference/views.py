from django.http import JsonResponse
from django.utils import timezone
from .models import DifferenceRequest
from .tasks import calculate_difference_task


def difference_view(request) -> JsonResponse:
    try:
        n = int(request.GET.get("number", ""))
        if not (1 <= n <= 100):
            return JsonResponse({"error": "n must be between 1 and 100"}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid number format"}, status=400)

    obj, created = DifferenceRequest.objects.get_or_create(number=n)
    
    if not created:
        obj.occurrences += 1
        obj.save()

    # Call the Celery task to calc the difference between (sum of squares) and (square of sums)
    result = calculate_difference_task.apply_async(args=[n])

    current_datetime = timezone.now()

    response_data = {
        "datetime": current_datetime,
        "value": result.get(timeout=10),
        "number": n,
        "occurrences": obj.occurrences,
        "last_datetime": obj.last_datetime,
    }

    return JsonResponse(response_data)
