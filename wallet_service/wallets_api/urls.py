from django.urls import path
from .views import WalletOperation, WalletDetail

urlpatterns = [
    path('api/v1/wallets/<uuid:WALLET_UUID>/operation', WalletOperation.as_view(), name='wallet_operation'),
    path('api/v1/wallets/<uuid:WALLET_UUID>', WalletDetail.as_view(), name='wallet_detail'),
]