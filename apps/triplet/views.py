from django.http import JsonResponse, HttpRequest
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import TripletRequest
from .tasks import check_pythagorean_triplet



@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('a', openapi.IN_QUERY, description="The first number (a)", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('b', openapi.IN_QUERY, description="The second number (b)", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('c', openapi.IN_QUERY, description="The third number (c)", type=openapi.TYPE_INTEGER, required=True),
    ],
    responses={
        200: openapi.Response(description="Valid Pythagorean triplet response"),
        400: openapi.Response(description="Invalid input or error"),
    }
)
@api_view(['GET'])
def triplet_view(request: HttpRequest) -> JsonResponse:
    try:
        a: int = int(request.GET.get('a', ''))
        b: int = int(request.GET.get('b', ''))
        c: int = int(request.GET.get('c', ''))
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid input. Please provide integer values for a, b, and c."}, status=400)
    

    obj, created = TripletRequest.objects.get_or_create(a=a, b=b, c=c)

    if not created:
        obj.occurrences += 1
        obj.last_datetime = timezone.now()
        obj.save()

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
