from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, KYCForm
from .serializers import LoginSerializer, KYCFormSerializer

class LoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(phone=phone)
                if password == user.password:
                    return Response({'status': True, 'message': 'Login successful', 'data': {'user_id': user.id}}, status=200)
                else:
                    return Response({'status': False, 'message': 'Invalid credentials'}, status=401)
                
            except User.DoesNotExist:
                return Response({'status': False, 'message': 'User not found'}, status=404)
            
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        try:
            users = User.objects.all()

            if not users.exists():
                return Response({'error': 'No users exist'}, status=404)

            serializer = LoginSerializer(users, many=True)
            return Response(serializer.data, status=200)

        except Exception as e:
            return Response({'error': f'Something went wrong: {str(e)}'}, status=500)

class UploadKYCFormView(APIView):
    
    def post(self, request):
        serializer = KYCFormSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'KYC uploaded successfully'}, status=201)
        return Response(serializer.errors, status=400)
    


    def get(self, request):
        user_id  = request.query_params.get('user')
        if not user_id:
            return Response({'error': 'user ID is required in query params'}, status=400)

        try:
            kyc_records = KYCForm.objects.filter(user__id=user_id)
            
            if not kyc_records.exists():
                return Response({'error': 'No KYC found for this user'}, status=404)
            
            serializer = KYCFormSerializer(kyc_records, many=True)
            return Response(serializer.data, status=200)
        except KYCForm.DoesNotExist:
            return Response({'error': 'KYC not found for this user'}, status=404)