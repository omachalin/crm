from django.db.models.functions import Coalesce
from BaseSetting.get_setting import get_options
from datetime import datetime, timedelta
from django.db.models import Sum
from Cashbox.models import Cashbox


class CashBoxCounter():
  base_settings: dict
  result: dict

  def __init__(self) -> None:
    self.result = {}
    self.base_settings = get_options([
      'type_payment_fk_expenses_status',
      'type_money_fk_cash',
      'type_money_fk_cashless',
    ])

  def get(self):
    return self.result

  def get_current_date(self):
    today = datetime.today().date()
    fifteen_days_ago = today - timedelta(days=15)
    month_ago = today - timedelta(days=30)
    return today, fifteen_days_ago, month_ago

  def aggregate_sum_money(self, cashbox):
    today, fifteen_days_ago, month_ago = self.get_current_date()
    cashbox_today = cashbox.filter(create_date_time__date=today).aggregate(
      total=Coalesce(Sum('money'), 0)
    )['total']

    cashbox_15_days = cashbox.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=fifteen_days_ago
    ).aggregate(total=Coalesce(Sum('money'), 0))['total']

    cashbox_month = cashbox.filter(
      create_date_time__date__lte=today,
      create_date_time__date__gte=month_ago
    ).aggregate(total=Coalesce(Sum('money'), 0))['total']

    cashbox_expenses_cash_today = cashbox.filter( # Наличка type_money_fk_cash
      create_date_time__date=datetime.today().date(),
      type_money_fk=self.base_settings['type_money_fk_cash'],
    ).aggregate(
      total=Coalesce(Sum('money'), 0)
    )['total']

    cashbox_expenses_cashless_today = cashbox.filter( # Безнал type_money_fk_cashless
      create_date_time__date=datetime.today().date(),
      type_money_fk=self.base_settings['type_money_fk_cashless'],
    ).aggregate(
      total=Coalesce(Sum('money'), 0)
    )['total']

    return {
      'cashbox_today': cashbox_today,
      'cashbox_15_days': cashbox_15_days,
      'cashbox_month': cashbox_month,
      'cashbox_cash_today': cashbox_expenses_cash_today,
      'cashbox_cashless_today': cashbox_expenses_cashless_today,
    }

  def get_expenses(self):
    """Возвращает расходы"""
    cashbox = Cashbox.objects.filter(type_payment_fk=self.base_settings['type_payment_fk_expenses_status'])
    res = self.aggregate_sum_money(
      cashbox=cashbox
    )

    expenses = {
      'cashbox_expenses_today': {
        'name': 'Расход за день',
        'money': res['cashbox_today'],
      },
      'cashbox_expenses_15_days': {
        'name': 'Расход за период',
        'money': res['cashbox_month'],
      },
      'cashbox_expenses_month': {
        'name': 'Расход за месяц',
        'money': res['cashbox_15_days'],
      },
      'cashbox_expenses_cash_today': {
        'name': 'Расход за день (НАЛ)',
        'money': res['cashbox_cash_today'],
      },
      'cashbox_expenses_cashless_today': {
        'name': 'Расход за день (Безнал)',
        'money': res['cashbox_cashless_today'],
      }
    }

    self.result.update(expenses)

  def get_income(self):
    """Возвращает доходы"""
    cashbox = Cashbox.objects.exclude(type_payment_fk=self.base_settings['type_payment_fk_expenses_status'])
    res = self.aggregate_sum_money(cashbox=cashbox)

    income = {
      'cashbox_today': {
        'name': 'Доход за день',
        'money': res['cashbox_today'],
      },
      'cashbox_15_days': {
        'name': 'Доход за период',
        'money': res['cashbox_15_days'],
      },
      'cashbox_month': {
        'name': 'Доход за месяц',
        'money': res['cashbox_month'], 
      },
      'cashbox_cash_today': {
        'name': 'Доход за день (НАЛ)',
        'money': res['cashbox_cash_today'],
      },
      'cashbox_cashless_today': {
        'name': 'Доход за день (Безнал)',
        'money': res['cashbox_cashless_today'],
      }
    }
  
    self.result.update(income)

  def get_profit(self):
    self.result.update({
      'profit_today': {
        'name': 'Прибыль за день',
        'money': self.result['cashbox_today']['money'] - self.result['cashbox_expenses_today']['money'],
      },
      'profit__15_days': {
        'name': 'Прибыль за период',
        'money': self.result['cashbox_15_days']['money'] - self.result['cashbox_expenses_15_days']['money'],
      },
      'profit_month': {
        'name': 'Прибыль за месяц',
        'money': self.result['cashbox_month']['money'] - self.result['cashbox_expenses_month']['money'],
      },
      'profit_cash_today': {
        'name': 'Прибыль за день (НАЛ)',
        'money': self.result['cashbox_cash_today']['money'] - self.result['cashbox_expenses_cash_today']['money'],
      },
      'profit_cashless_today': {
        'name': 'Прибыль за день (Безнал)',
        'money': (
          self.result['cashbox_cashless_today']['money'] - self.result['cashbox_expenses_cashless_today']['money']
        ),
      }
    })
