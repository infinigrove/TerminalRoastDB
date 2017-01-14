#!/usr/bin/python
# -*- coding: utf-8 -*-
# TerminalRoastDB, released under GPLv3

import pymysql


class Recipe(object):
    def __init__(self):
        #self.currentRecipeStep = 1
        self.currentRecipeID = 1
        self.target_temp = 200
        self.fan_speed = 5
        self.time_remaining = 10

        # Stores recipe
        self.recipe = {}

        # Tells if a recipe has been loaded
        self.recipeLoaded = False
        self.db = pymysql.connect(host="localhost",    # your host, usually localhost
                             user="terminalroaster",         # your username
                             passwd="terminalroasterpasswd",  # your password
                             db="terminalroastDB")        # name of the data base
        self.currentRecipeID = self.get_roast_recipe_id()

    def get_num_recipe_sections(self):
        #return len(self.recipe["steps"])
        stepsCur = self.db.cursor()
        stepsSql = "SELECT * FROM recipe_steps WHERE recipe_id = %s ORDER BY seqNum"
        stepsCur.execute(stepsSql, (self.currentRecipeID,))
        return stepsCur.rowcount - 1

    def get_current_step_number(self):
        curStepCur = self.db.cursor()
        curStepSql = "SELECT * FROM recipe_steps WHERE recipe_id = %s AND seqNum = %s"
        curStepCur.execute(curStepSql, (self.currentRecipeID, self.currentRecipeStep))
        for row in curStepCur.fetchall():
            # Assign new state based on rom 0 -5
            self.currentRecipeStep = row[5]
            self.target_temp = row[4]
            self.fan_speed = row[3]
            self.time_remaining = row[2]
            print("set roaster time = ",row[2]," fan speed = ",row[3]," temp = ",row[4])
        self.currentRecipeStep += 1
        self.set_roast_recipe_step(self.currentRecipeStep)
        return self.currentRecipeStep

    def get_roast_recipe_id(self):
        recCur = self.db.cursor()
        recSql = "SELECT * FROM roaster_recipe WHERE id = 1"
        recCur.execute(recSql)
        for row in recCur.fetchall():
            Cur_Recipe_ID = row[1]
        return Cur_Recipe_ID

    def set_roast_recipe_id(self, recipeID):
        recCur = self.db.cursor()
        recSql = "UPDATE roaster_recipe SET recipe_id=%s WHERE id=1"
        recCur.execute(recSql, (recipeID,))
        self.db.commit()

    def get_roast_recipe_step(self):
        recCur = self.db.cursor()
        recSql = "SELECT * FROM roaster_recipe_step WHERE id = 1"
        recCur.execute(recSql)
        for row in recCur.fetchall():
            Cur_Recipe_Step = row[1]
        return Cur_Recipe_Step

    def set_roast_recipe_step(self, recipeStep):
        recCur = self.db.cursor()
        recSql = "UPDATE roaster_recipe_step SET recipe_step=%s WHERE id=1"
        recCur.execute(recSql, (recipeStep,))
        self.db.commit()

