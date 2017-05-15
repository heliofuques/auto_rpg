'''
Created on 13 de mai de 2017

@author: helio
'''
from Tkinter import *
from utils import npcDecoder
import json
class MobsView(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.first = True
        self.controller = controller
        label = Label(self, text="Creature List")
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side= BOTTOM)
        self.loadCreatures()
        
        self.monsterList = Listbox(self)# yscrollcommand = self.setMonsterShow())
        self.monsterList.configure(yscrollcommand = self.setMonsterShow())
        for monster in self.npcList:
            self.monsterList.insert(0,monster.name)
            
        self.monsterList.place(x = 0, y = 0, height = 690)
        
        self.info = Frame(self, background = "white")
        
        self.labelName = Label(self.info, text=self.npcList[0].name)
        self.labelHp = Label(self.info, text=self.npcList[0].hp)
        self.labelName.pack()
        self.labelHp.pack()
        self.info.place( x = 360, y = 40, height = 500,width = 360)
        
    def setMonsterShow(self):
        print "chamado"
        if self.first:
            self.first = False
            return 0
        
        for monster in self.npcList:
            if monster.name == self.monsterList.selection_get():
                self.labelName.configure(text = monster.name)
                self.labelHp.configure( text = monster.hp)
        
    def loadCreatures(self):
        self.npcList = list()
        fileJ = open("data/npcs.json", 'r')
        npcsJson = json.loads(fileJ.read())
        for npc in npcsJson['list']:
            self.npcList.append( npcDecoder(npc))
        