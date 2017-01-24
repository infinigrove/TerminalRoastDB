# -*- coding: utf-8 -*-
# Copyright (c) 2015-2016 Jeff Stevens
# TerminalRoastDB, released under GPLv3

import time
import sys
import freshroastsr700
import logging
import recipe
import Pyro4


@Pyro4.expose
class Roaster(object):
    def __init__(self):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        self.recipes = recipe.Recipe()
        self.roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)
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
        self.recipes.currentRecipeID = self.recipes.get_roast_recipe_id()
        self.recipes.currentRecipeStep = self.recipes.get_roast_recipe_step()
        if(self.recipes.currentRecipeStep <= self.recipes.get_num_recipe_sections()):
            self.recipes.get_current_step_number()
            if(self.recipes.target_temp > 149):
                self.roaster.target_temp = self.recipes.target_temp
                if(self.roaster.get_roaster_state() == 'cooling'):
                    self.roaster.roast()
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

    def run_roast(self, recipeID):
        if(self.roaster.get_roaster_state() == 'idle'):
            new_recipeID = int(recipeID)
            self.recipes.set_roast_recipe_id(new_recipeID)
            self.recipes.currentRecipeID = new_recipeID
            self.total_steps = self.recipes.get_num_recipe_sections()
            print("Running Roast ", self.recipes.currentRecipeID)
            self.recipes.currentRecipeStep = 0
            self.recipes.set_roast_recipe_step(self.recipes.currentRecipeStep)
            self.recipes.get_current_step_number()
            if(self.recipes.target_temp > 149):
                self.roaster.target_temp = self.recipes.target_temp
            else:
                print("Roaster set to cool")
            self.roaster.fan_speed = self.recipes.fan_speed
            self.roaster.time_remaining = self.recipes.time_remaining
            print(self.recipes.currentRecipeStep)
            time.sleep(5)
            #self.roaster.roast()
            # Comment code bellow when running for real
            # next_state function will replace this loop
            self.recipes.currentRecipeStep = self.recipes.get_roast_recipe_step()
            while(self.recipes.currentRecipeStep <= self.recipes.get_num_recipe_sections()):
                self.recipes.get_current_step_number()
                if(self.recipes.target_temp > 149):
                    self.roaster.target_temp = self.recipes.target_temp
                else:
                    #self.roaster.cool()
                    print("Roaster set to cool")
                self.roaster.fan_speed = self.recipes.fan_speed
                self.roaster.time_remaining = self.recipes.time_remaining
                print(self.recipes.currentRecipeStep)
                time.sleep(5)

    def set_fan_speed(self, speed):
        new_speed = int(speed)
        self.roaster.fan_speed = new_speed

    def set_temperature(self, temperature):
        new_temperature = int(temperature)
        self.roaster.target_temp = new_temperature

    def set_time(self, time):
        new_time = int(time)
        self.roaster.time_remaining = new_time

    def output_current_state(self):
        cur_state = self.roaster.get_roaster_state()
        cur_temp = str(self.roaster.current_temp)
        ret_state = cur_temp + cur_state
        return ret_state


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

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()
uri = daemon.register(r)

print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
ns.register("roaster.sr700", uri)
daemon.requestLoop()                   # start the event loop of the server to wait for calls
