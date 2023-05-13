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

    cashboxes_obj = Cashbox.objects.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago,
      type_payment_fk__in=[
        base_settings['type_payment_fk_agreement_status'],
        base_settings['type_payment_fk_transport_status'],
      ],
      # agreement__create_date_time__date__lte=today,
      # agreement__create_date_time__date__gte=fifteen_days_ago,
    )
  
    comings_obj = Coming.objects.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago,
    )
    
    cashboxes_serializer = CashboxSerializer(cashboxes_obj, many=True).data

    comings_serializer = ComingMinForRateSerializer(comings_obj, many=True).data

    rate_result = []
    salary_percent = 0.2

    for persone_key in persons_serializer:
      persone = {
        'pk': persone_key['pk'],
        'pin': persone_key['pin'],
        'comings': 0,
        'agreements': 0,
        'agreements_money': 0,
        'cashbox_agreements_money': 0,
        'salary': 0,
      }

      for coming in comings_serializer:
        if uuid.UUID(persone_key['pk']) in coming['upp']:
          persone['comings'] += 1

      for cashbox in cashboxes_serializer:
        agreement_cashbox = cashbox['agreements'][0]
        for upp in agreement_cashbox['coming']['upp_readonly']:
          if persone_key['pk'] == upp['pk']:
            persone['agreements'] += 1
            persone['agreements_money'] += agreement_cashbox['price']
            persone['cashbox_agreements_money'] += cashbox['money']
            persone['salary'] += cashbox['money'] * salary_percent
      rate_result.append(persone)

    # for cashbox in cashboxes_serializer:
    #   for personal in persons_serializer:
    #     for upp in cashbox['agreements'][0]['coming']['upp_readonly']:
    #       if personal['pk'] == upp['pk']:
    #         if personal['pk'] not in rate_result:
    #           print('!!!!!!!')
    #           rate_result.append({
    #             'pk': personal['pk'],
    #             'pin': personal['pin'],
    #             'comings': 0,
    #             'agreements': 0,
    #             'agreement_money': 0,
    #             'cashbox_agreements_money': 0,
    #           })

            #rate_result[personal['pk']]['agreements'] += 1
        # print(cashbox['agreements'][0]['coming']['upp_readonly'])
          # if agreement['upp_readonly']['pk'] == personal['pk']:
          #   print('123')
    
    #print(rate_result['571ea069-2536-437d-bd76-4f0a8311ad83'])
    return Response(rate_result)