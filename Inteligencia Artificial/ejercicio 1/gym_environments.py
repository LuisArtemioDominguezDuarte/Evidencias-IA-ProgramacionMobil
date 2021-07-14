#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Autor: Luis Artemio Dominguez Duarte
"""

from gym import envs

env_names = [env.id for env in envs.registry.all()]

for name in sorted(env_names):
    print(name)

