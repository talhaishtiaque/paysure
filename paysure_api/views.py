from .models import Policy, Payment
from .serializers import PolicySerializer, PaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum


class PolicyView(APIView):
    """
    API endpoint that allows policies to be viewed or updated.
    """
    def get(self, request, format=None):
        """
        Return a list of all policies.
        """
        policies = Policy.objects.all()
        serializer = PolicySerializer(policies, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Upload policies.
        """
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentView(APIView):
    """
    API endpoint that allows payments to be viewed or updated.
    """
    def get(self, request, format=None):
        """
        Return a list of all policies.
        """
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Upload payments.
        """
        serializer = PaymentSerializer(data=request.data)
        payment = request.data
        try:
            policy = Policy.objects.filter(external_user_id = payment['external_user_id'],
                                            benefit = payment['benefit'],
                                            currency__iexact = payment['currency'])
            if len(policy) != 0:
                already_paid = Payment.objects.filter(external_user_id = payment['external_user_id'],
                                                        benefit = payment['benefit'],
                                                        currency__iexact = payment['currency'],
                                                        authorized = True).aggregate(Sum('amount'))
                if already_paid['amount__sum'] is None:
                    already_paid['amount__sum'] = 0
                if (already_paid['amount__sum'] + int(payment['amount'])) <= policy[0].total_max_amount:
                    payment['authorized'] = True
                    payment['reason'] = 'null'
                else:
                    payment['authorized'] = False
                    payment['reason'] = 'POLICY_AMOUNT_EXCEEDED'
                serializer = PaymentSerializer(data=payment)
            else:
                payment['authorized'] = False
                payment['reason'] = 'POLICY_NOT_FOUND'
            if serializer.is_valid():
                serializer.save()
                return Response({"authorized": payment['authorized'], "reason": payment['reason']}, status=status.HTTP_200_OK)
            return Response({"authorized": False, "reason": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"authorized": False, "reason": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
