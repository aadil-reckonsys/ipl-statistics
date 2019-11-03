from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
import pandas as pd
from rest_framework.response import Response
from storage.tasks import upload_matches, upload_deliveries


class MatchUploadAPI(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        for chunk in pd.read_csv(self.request.FILES['match_file'], chunksize=100):
            upload_matches.delay(chunk.to_dict(orient='records'))
        return Response({'msg': 'File Uploaded'}, status=status.HTTP_201_CREATED)


class DeliveryUploadAPI(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        for chunk in pd.read_csv(self.request.FILES['delivery_file'], chunksize=100):
            upload_deliveries.delay(chunk.to_dict(orient='records'))
        return Response({'msg': 'File Uploaded'}, status=status.HTTP_201_CREATED)
