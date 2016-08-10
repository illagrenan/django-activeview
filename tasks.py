# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import shutil

from invoke import run, task


@task
def clean():
    """remove build artifacts"""
    shutil.rmtree('django_activeview.egg-info', ignore_errors=True)
    shutil.rmtree('build', ignore_errors=True)
    shutil.rmtree('dist', ignore_errors=True)
    shutil.rmtree('htmlcov', ignore_errors=True)
    shutil.rmtree('__pycache__', ignore_errors=True)


@task
def lint():
    """check style with flake8"""
    run("flake8 activeview test_project/tests")


@task
def test():
    """run tests quickly with the default Python"""
    run("python test_project/manage.py test")


@task
def test_all():
    """run tests on every Python version with tox"""
    run("tox")


@task
def coverage():
    """check code coverage quickly with the default Python"""
    run("coverage run --source activeview/templatetags test_project/manage.py test")
    run("coverage report -m")
    run("coverage html")


@task
def test_install():
    """try to install built package"""
    run("pip uninstall django_activeview --yes", warn=True)
    run("pip install --use-wheel --no-index --find-links dist django_activeview")
    run("pip uninstall django_activeview --yes")


@task
def build():
    """build package"""
    run("python setup.py check --verbose --strict --restructuredtext")

    run("python setup.py build")
    run("python setup.py sdist")
    run("python setup.py bdist_wheel")


@task
def publish():
    """publish package"""
    run('python setup.py sdist upload -r pypi')
    run('python setup.py bdist_wheel upload -r pypi')
