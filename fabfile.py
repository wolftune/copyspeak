from fnpdjango.deploy import *

env.project_name = 'copyspeak'
env.hosts = ['giewont.icm.edu.pl']
env.user = 'copyspeak'
env.app_path = '/srv/copyspeak.org'
env.services = [
    DebianGunicorn('copyspeak'),
]
env.django_root_path = 'src'

