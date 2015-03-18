import re
from subprocess import Popen, PIPE
from fabric.api import local


def update():
    local('rm jquery.min.js')
    output = Popen(["bower", "info", "jquery"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '([2-9]\.\d+\.\d+)',", output)[0]
    print 'latest version: {0}'.format(latest_version)
    local('wget http://code.jquery.com/jquery-{0}.min.js'.format(latest_version))
    local('mv jquery-{0}.min.js jquery.min.js'.format(latest_version))
