from string import Template
from fabric.operations import prompt, put
from fabric.api import env, local, run, cd, sudo, require


def _replace_in_template(template_location, filename):
    with open(template_location) as f:
        template = Template(f.read())
    with open(filename, 'w') as f:
        f.write(template.substitute(**env))


def replace_sudoers():
    sudo('cp /etc/sudoers /etc/sudoers.bak')
    _replace_in_template('sudoers.template', 'sudoers')
    put('sudoers', '/tmp', mode=0440)
    sudo('chown root:root /tmp/sudoers')
    sudo('mv /tmp/sudoers /etc/sudoers')


def generate_celery_defaults():
    _replace_in_template('celeryd.defaults.template', 'celeryd.defaults')


def setup():
    if not 'app_user' in env:
        env.app_user = prompt("User to run the application", default='vagrant')
    require('app_user')
    generate_celery_defaults()
    replace_sudoers()
    pip_install()
    syncdb()


def vagrant():
    # change from the default user to 'vagrant'
    env.user = 'vagrant'
    # connect to the port-forwarded ssh
    hostname = local('vagrant ssh-config | grep HostName', capture=True)
    port = local('vagrant ssh-config | grep Port', capture=True)
    env.hosts = ['{0}:{1}'.format(hostname.split()[1], port.split()[1]), ]

    # use vagrant ssh key
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


def pip_install():
    with cd('/vagrant'):
        sudo('pip install -r requirements.txt')


def syncdb():
    with cd('/vagrant'):
        run('python manage.py syncdb --noinput', pty=True)


def start_celery():
    with cd('/vagrant'):
        run('./celeryd start')

def stop_celery():
    with cd('/vagrant'):
        run('./celeryd stop')

def restart_celery():
    with cd('/vagrant'):
        run('./celeryd restart')


def runserver():
    #restart_celery()
    with cd('/vagrant'):
        run('python manage.py runserver [::]:8000')

def reload_server():
    stop_celery()
    runserver()
