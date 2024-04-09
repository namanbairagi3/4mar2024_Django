import base64
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ImageUploadView(APIView):
    def post(self, request, format=None):
        try:
            # Decode Base64 image data from request
            image_data = base64.b64decode(request.data.get('image'))

            # Save image to file
            with open('/.000.png', 'wb') as f:
                f.write(image_data)

            return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
