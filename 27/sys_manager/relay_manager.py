# -*- coding: UTF-8 -*-
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""


Authors: lirui23(lirui23@baidu.com)
Date:    2019-05-10 09:08
"""
from fabric.api import cd, env, prefix, run, task
from fabric.decorators import roles
from fabric.operations import local, put
from fabric.tasks import execute

env.roledefs = {

    'master': ['relay01'],

    'client': ['10.168.32.106',

               '10.168.32.110',

               '10.168.32.111'],

}

env.hosts = [

    'root@10.168.32.106',

    'root@10.168.32.110',

    'root@10.168.32.111',

]

env.passwords = {

    'root@10.168.32.106:22': 'passwd1',

    'root@10.168.32.110:22': 'passwd1',

    'root@10.168.32.111:22': 'passwd1',

}


@roles('master')
def get_sshkey_rsa():
    local("if [ ! -f ~/.ssh/id_rsa ]; then ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa;fi")


@roles('client')
def copy_id(file='~/.ssh/id_rsa.pub'):
    put(file, "/tmp/id_rsa.pub")

    try:

        run("if [ ! -d ~/.ssh ]; then mkdir -p ~/.ssh; fi")

        run(
            "if [ ! -f ~/.ssh/authorized_keys ]; then cp /tmp/id_rsa.pub ~/.ssh/authorized_keys && chmod 0600 ~/.ssh/authorized_keys; fi")

        run("cat ~/.ssh/authorized_keys >> /tmp/id_rsa.pub &&  sort -u /tmp/id_rsa.pub > ~/.ssh/authorized_keys")

    finally:

        run("rm -f /tmp/id_rsa.pub")


def allsshkey():
    execute(get_sshkey_rsa)

    execute(copy_id)
