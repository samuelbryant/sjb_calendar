import os


def get_credential_path():
  return os.path.join(
    _get_default_data_dir(), 'calendar-python-quickstart.json')


def get_client_secret_path():
  return os.path.join(
    _get_default_data_dir(), 'client_secret_alpha.json')


def _get_default_data_dir():
  if 'XDG_DATA_HOME' in os.environ:
    return os.environ['XDG_DATA_HOME']+'/'+'sjb/calendar/'
  return os.environ['HOME']+'/.local/share/sjb/calendar/'


def _get_default_config_file():
  if 'XDG_CONFIG_HOME' in os.environ:
    return os.environ['XDG_CONFIG_HOME']+'/'+'sjb/calendar/'
  return os.environ['HOME']+'/.config/sjb/calendar/'

