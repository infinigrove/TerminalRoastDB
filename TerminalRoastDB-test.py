# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Jeff Stevens
# Made available under the MIT license.

import time
import sys
import freshroastsr700
import logging
import recipe

run_this_recipe_ID = sys.argv[1]


class Roaster(object):
    def __init__(self):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        self.recipes = recipe.Recipe()
        self.roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)
        self.recipes.currentRecipeID = run_this_recipe_ID
        self.total_steps = self.recipes.get_num_recipe_sections()

    def update_data(self):
        """This is a method that will be called every time a packet is opened
        from the roaster."""
        cur_state = self.roaster.get_roaster_state()
        print("Current Temperature:", self.roaster.current_temp, cur_state)

    def next_state(self):
        """This is a method that will be called when the time remaining ends.
        The current state can be: roasting, cooling, idle, sleeping, connecting,
        or unkown."""
        if(self.recipes.currentRecipeStep <= self.recipes.get_num_recipe_sections()):
            self.recipes.get_current_step_number()
            if(self.recipes.target_temp > 149):
                self.roaster.target_temp = self.recipes.target_temp
            else:
                self.roaster.cool()
                print("Roaster set to cool")
            self.roaster.fan_speed = self.recipes.fan_speed
            self.roaster.time_remaining = self.recipes.time_remaining
            print(self.recipes.currentRecipeStep)
        elif(self.roaster.get_roaster_state() == 'roasting'):
            self.roaster.time_remaining = 20
            self.roaster.cool()
        elif(self.roaster.get_roaster_state() == 'cooling'):
            self.roaster.idle()


# Create a roaster object.
r = Roaster()

# Set logging
#logging.basicConfig(filename="RoastControl_debug_log.log",level=logging.DEBUG)

# Conenct to the roaster.
r.roaster.auto_connect()

# Wait for the roaster to be connected.
while(r.roaster.connected is False):
    print("Please connect your roaster...")
    time.sleep(1)

r.recipes.currentRecipeStep = 0
r.recipes.get_current_step_number()
if(r.recipes.target_temp > 149):
    r.roaster.target_temp = r.recipes.target_temp
else:
    print("Roaster set to cool")
r.roaster.fan_speed = r.recipes.fan_speed
r.roaster.time_remaining = r.recipes.time_remaining
print(r.recipes.currentRecipeStep)

time.sleep(5)

# Begin roasting.
#r.roaster.roast()

# This ensures the example script does not end before the roast.
#while(r.roaster.connected is True):
while(r.recipes.currentRecipeStep <= r.recipes.get_num_recipe_sections()):
    r.recipes.get_current_step_number()
    if(r.recipes.target_temp > 149):
        r.roaster.target_temp = r.recipes.target_temp
    else:
        #self.roaster.cool()
        print("Roaster set to cool")
    r.roaster.fan_speed = r.recipes.fan_speed
    r.roaster.time_remaining = r.recipes.time_remaining
    print(r.recipes.currentRecipeStep)
    time.sleep(5)

# Disconnect from the roaster.
r.roaster.disconnect()
