from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wallet
from .serializers import OperationSerializer, WalletSerializer

class WalletOperation(APIView):
    def post(self, request, WALLET_UUID):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operation_type = serializer.validated_data['operationType']
            amount = serializer.validated_data['amount']
            try:
                wallet = Wallet.objects.get(uuid=WALLET_UUID)
            except Wallet.DoesNotExist:
                return Response({'error': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)

            if operation_type == 'DEPOSIT':
                wallet.balance += amount
            elif operation_type == 'WITHDRAW':
                if wallet.balance < amount:
                    return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
                wallet.balance -= amount

            wallet.save()
            return Response({'balance': wallet.balance}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletDetail(APIView):
    def get(self, request, WALLET_UUID):
        try:
            wallet = Wallet.objects.get(uuid=WALLET_UUID)
            serializer = WalletSerializer(wallet)
            return Response(serializer.data)
        except Wallet.DoesNotExist:
            return Response({'error': 'Wallet not found'}, status=status.HTTP_404_NOT_FOUND)


