from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.api.serializers.password_reset import PasswordResetSerializer, PasswordResetValidationSerializer


class PasswordResetView(GenericAPIView):
    permission_classes = []
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.update_user(
            email=serializer.validated_data.get("email")
        )
        return Response(self.get_serializer(user).data)


class PasswordResetValidationView(GenericAPIView):
    permission_classes = []
    serializer_class = PasswordResetValidationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(
            serializer.validated_data,
        )
        return Response(self.get_serializer(user).data)
