from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from project.api.serializers.registration import RegistrationSerializer, RegistrationValidationSerializer
from project.api.serializers.users import UserSerializer


class RegistrationView(GenericAPIView):
    permission_classes = []
    serializer_class = RegistrationSerializer
    output_serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = serializer.register_user(
            email=serializer.validated_data.get("email"))
        return Response(self.output_serializer_class(new_user).data)


class RegistrationValidationView(GenericAPIView):
    permission_classes = []
    serializer_class = RegistrationValidationSerializer
    output_serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(
            serializer.validated_data,
        )
        return Response(self.output_serializer_class(user).data)
