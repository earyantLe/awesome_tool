# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""


Authors: lirui23(lirui23@baidu.com)
Date:    2019-05-10 08:40
"""
from fabric.api import cd, env, prefix, run, task
import config

env.hosts = config.yinli_hosts
env.user = config.yinli_user
env.password = config.yinli_password
env.passwords = config.yinli_passwords


@task
def memory_usage():
    run('free -m')


@task
def cpu():
    run('top | grep java')


@task
def tom_32():
    run('ps -ef | grep tomcat-8032')


@task
def tom_50():
    run('ps -ef | grep tomcat-8032')


@task
def deploy():
    with cd('/var/www/project-env/project'):
        with prefix('. ../bin/activate'):
            run('git pull')
            run('touch app.wsgi')


@task
def restart():
    with cd('/usr/local'):
        run("sh run8050.sh restart")
        run("sh run8032.sh restart")


def hello():
    print ("Hello Fabric!")
