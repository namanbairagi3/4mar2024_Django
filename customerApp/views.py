from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this to exempt CSRF token requirement
from .models import Customer

from PIL import Image
import io, base64, os, json

@csrf_exempt  # Exempt CSRF token requirement for this view
def getBalance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            client_key = data.get('clientKey')
            if client_key:
                try:
                    customer = Customer.objects.get(client_key=client_key)
                    balance = customer.current_amount_usd
                    response_data = {
                        "errorId": 0,
                        "balance": balance
                    }
                    return JsonResponse(response_data)
                except Customer.DoesNotExist:
                    return JsonResponse({"errorId": 1, "message": "Invalid clientKey"})
            else:
                return JsonResponse({"errorId": 1, "message": "clientKey not provided"})
        except json.JSONDecodeError:
            return JsonResponse({"errorId": 1, "message": "Invalid JSON format"})
    else:
        return JsonResponse({"errorId": 1, "message": "Invalid request method"})

def base64_to_image(base64_string, output_file):
    try:
        # Extracting the base64 string without 'data:image/jpeg;base64,'
        base64_string = base64_string.split(',')[1]

        # Decoding the base64 string and saving it as an image
        with open(output_file, "wb") as fh:
            fh.write(base64.b64decode(base64_string))
    
        return True
    except Exception as e:
        print("Error:", e)
        return False
        
@csrf_exempt  # Exempt CSRF token requirement for this view
def createTask(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            client_key = data.get('clientKey')
            if client_key:
                try:
                    base64String = data['task']['body']
                    output_file = "image.jpg"  # Output file name (you can change the extension based on the image format)

                    # Convert base64 to image and save
                    if base64_to_image(base64String, output_file):
                        response_data = {
                            "errorId": 0,
                            "message": "Image saved successfully"
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({"errorId": 1, "message": "Failed to save image"})
                except KeyError:
                    return JsonResponse({"errorId": 1, "message": "Invalid task format"})
                except Customer.DoesNotExist:
                    return JsonResponse({"errorId": 1, "message": "Invalid clientKey"})
            else:
                return JsonResponse({"errorId": 1, "message": "clientKey not provided"})
        except json.JSONDecodeError:
            return JsonResponse({"errorId": 1, "message": "Invalid JSON format"})
    else:
        return JsonResponse({"errorId": 1, "message": "Invalid request method"})
