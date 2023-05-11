from BaseSetting.models import BaseSetting


def get_option(key):
  return BaseSetting.objects.get(name=key).value

def get_options(params):
  settings = BaseSetting.objects.filter(name__in=params)
  result = {}
  for setting in settings:
    result[setting.sys_name] = setting.value
  return result
