from django.utils import timezone
from django.http import JsonResponse, HttpRequest
from django.utils.timezone import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import DifferenceRequest
from .tasks import calculate_difference_task



@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'number', openapi.IN_QUERY, 
            description="Number for the calculation", 
            type=openapi.TYPE_INTEGER
        )
    ],
    responses={200: openapi.Response("Successful calculation")}
)
@api_view(['GET'])
def difference_view(request: HttpRequest) -> JsonResponse:
    try:
        n = int(request.GET.get("number", ""))
        if not (1 <= n <= 100):
            return JsonResponse({"error": "n must be between 1 and 100"}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid number format"}, status=400)

    obj: DifferenceRequest
    created: bool
    obj, created = DifferenceRequest.objects.get_or_create(number=n)
    
    if not created:
        obj.occurrences += 1
        obj.save()

    # Call the Celery task to calc the difference between (sum of squares) and (square of sums)
    result = calculate_difference_task.apply_async(args=[n])

    current_datetime: datetime = timezone.now()

    response_data: dict[str, object] = {
        "datetime": current_datetime.isoformat(),
        "value": result.get(timeout=10),
        "number": n,
        "occurrences": obj.occurrences,
        "last_datetime": obj.last_datetime.isoformat() if obj.last_datetime else None,
    }

    return JsonResponse(response_data)
