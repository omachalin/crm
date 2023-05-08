from datetime import datetime, date
from .models import Coming
from django.db.models import Count


class Counter:
  def __init__(self):
    pass

  def set_min_max_date(self):
    date_time_start = f"{str(date.today().strftime('%Y-%m-%d'))}T00:00:00"
    date_time_end = f"{str(date.today().strftime('%Y-%m-%d'))}T23:59:59"
    self.date_start = datetime.strptime(f'{date_time_start}', '%Y-%m-%dT%H:%M:%S').astimezone()
    self.date_end = datetime.strptime(f'{date_time_end}', '%Y-%m-%dT%H:%M:%S').astimezone()
  
  def get_counter(self):
    result = (Coming.objects
      .filter(create_date_time__range=[self.date_start, self.date_end])
      .values('status_fk__name')
      .annotate(dcount=Count('status_fk'))
      .order_by()
    )

    counter = {
      'first': 0,
      'second': 0,
      'agreement': 0,
      'bk': 0,
      'reject': 0,
    }

    for key in result:
      if key['status_fk__name'] == 'Первичка':
        counter['first'] = key['dcount']
      elif key['status_fk__name'] == 'Вторичка':
        counter['second'] = key['dcount']
      elif key['status_fk__name'] == 'Договор':
        counter['agreement'] = key['dcount']
      elif key['status_fk__name'] == 'БК':
        counter['bk'] = key['dcount']
      elif key['status_fk__name'] == 'Брак':
        counter['reject'] = key['dcount']

    return counter