#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TerminalRoastDB, released under GPLv3
# Roaster Run Recipe

import Pyro4
import sys

new_roaster_recipe = sys.argv[1]

roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")
if int(new_roaster_recipe) > 0:
    roast_control.run_roast(new_roaster_recipe)
