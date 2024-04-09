from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
import json

@csrf_exempt
def get_balance(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            client_key = data.get('clientKey')
            if client_key:
                try:
                    customer = Customer.objects.get(client_key=client_key)
                    balance = customer.current_amount_user  # Updated attribute name
                    response_data = {
                        "errorId": 0,
                        "balance": balance
                    }
                    return JsonResponse(response_data)
                except Customer.DoesNotExist:
                    return JsonResponse({"errorId": 1, "message": "Customer not found."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"errorId": 1, "message": "Invalid JSON format."}, status=400)
    
    return JsonResponse({"errorId": 1, "message": "Invalid request method."}, status=405)

def createTask(request):
    pass