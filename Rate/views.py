from django.shortcuts import render
from rest_framework.views import APIView
from Personal.models import Personal
from Personal.serializers import PersonalMinForCashBoxSerializer
from BaseSetting.get_setting import get_options
from rest_framework.response import Response
from Cashbox.models import Cashbox
from Cashbox.serializers import CashboxSerializer
from datetime import datetime, timedelta
from Coming.models import Coming
from Coming.serializers import ComingMinForRateSerializer
import uuid
from Agreement.models import Agreement
from Agreement.serializers import AgreementMinFromRateSerializer


class GetRate(APIView):
  #permission_classes = (IsAuthenticated, )

  def get(self, request, *args, **kwargs):
    base_settings = get_options([
      'fk_status_working',
      'fk_department_upp',
      'type_payment_fk_agreement_status',
      'type_payment_fk_transport_status',
    ])

    persons_obj = Personal.objects.filter(
      department_fk=base_settings['fk_department_upp'],
      status_fk=base_settings['fk_status_working'],
    ).values('pk', 'name', 'pin')

    persons_serializer = PersonalMinForCashBoxSerializer(persons_obj, many=True).data
    today = datetime.today().date()
    fifteen_days_ago = today - timedelta(days=15)

    # cashboxes_obj = Cashbox.objects.filter(
    #   create_date_time__date__lte=today,
    #   create_date_time__date__gte=fifteen_days_ago,
    #   type_payment_fk=base_settings['type_payment_fk_agreement_status'],
    #     #base_settings['type_payment_fk_agreement_status'],
    #     #base_settings['type_payment_fk_transport_status'],
    #   #],
    # )
  
    comings_obj = Coming.objects.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago,
    )
    
    #cashboxes_serializer = CashboxSerializer(cashboxes_obj, many=True).data
    comings_serializer = ComingMinForRateSerializer(comings_obj, many=True).data
    #agreements_serializer = Agre
    agreements_obj = Agreement.objects.filter(
      cashboxes__create_date_time__date__lte=today,
      cashboxes__create_date_time__date__gte=fifteen_days_ago,
    ).distinct()

    agreements_serializer = AgreementMinFromRateSerializer(agreements_obj, many=True).data
    
    rate_result = []
    salary_percent = 0.2

    for persone_key in persons_serializer:
      persone = {
        'pk': persone_key['pk'],
        'name': persone_key['name'],
        'pin': persone_key['pin'],
        'comings': 0,
        'agreements': 0,
        'agreements_money': 0,
        'cashbox_agreements_money': 0,
        'salary': 0,
        'price_transport': 0,
      }

      for coming in comings_serializer:
        if uuid.UUID(persone_key['pk']) in coming['upp']:
          persone['comings'] += 1

      agreement_payment_fk = uuid.UUID(base_settings['type_payment_fk_agreement_status'])
      persone_pk = uuid.UUID(persone_key['pk'])
      for agreement in agreements_serializer:
        if persone_pk in agreement['coming']['upp']:
          persone['agreements'] += 1
          persone['agreements_money'] += agreement['price']
          persone['price_transport'] += agreement['price_transport']
          for cashbox in agreement['cashboxes']:
            if cashbox['type_payment_fk'] == agreement_payment_fk:
              persone['cashbox_agreements_money'] += cashbox['money']

      salary = (persone['cashbox_agreements_money'] - persone['price_transport']) * salary_percent
      persone['salary'] = 0 if salary < 0 else salary
      del persone['price_transport']

      rate_result.append(persone)

    return Response(rate_result)