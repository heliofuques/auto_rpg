'''
Created on 3 de abr de 2017

@author: helio
'''
from Tkinter import *
from npc import NPC
from view.mobsview import MobsView
from PIL import ImageTk,Image
import json
'''

'''


TITLE_FONT = ("Helvetica", 18, "bold")


class rpgProject(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        Tk.minsize(self,1080, 700)
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MobsView, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller, background = 'gray'):
        Frame.__init__(self, parent, background = background)
        self.nameNPC, self.initNPC, self.sheetNPC = "teste","",""
        
        self.controller = controller
        self.label = Label(self, text="NPC",background = 'gray')
        self.labelInit = Label(self, text="Init",background = 'gray')
        self.labelSheet = Label(self, text="Sheet",background = 'gray')
        self.labelHP = Label(self, text="HP",background = 'gray')
        self.labelDES = Label(self, text = "DES", background = 'gray')
       
        self.entryNPC = Entry(self, width = 50, textvariable = self.nameNPC, background = 'gray')
        self.entryInit = Entry(self, width = 50, textvariable = self.initNPC, background = 'gray')
        self.entryHP = Entry(self, width = 5, background = 'gray')
        self.entryDES = Entry(self, width = 5, background = 'gray')
        self.entrySheet = Entry(self, width= 50, textvariable = self.sheetNPC, background = 'gray')
       
        self.button1 = Button(self, text = "click-me", command = self.save )
        self.listCreatures = Button( self, text = "Criaturas",borderwidth = 50 ,command=lambda: controller.show_frame("MobsView"))
        
        self.entryNPC.place  (x=360,y=200)
        self.label.place     (x=360,y=180) 
        
        self.labelInit.place (x=360,y=220)
        self.entryInit.place (x=360,y=240)
        
        self.labelSheet.place(x=360,y=260)
        self.entrySheet.place(x=360,y=280)
            
        self.labelHP.place(x=360, y=300)
        self.entryHP.place(x=360, y = 320 )
        self.labelDES.place( x = 420, y = 300 )
        self.entryDES.place( x = 420, y = 320) 
        
        self.button1.place   (x=360,y=670)
        self.listCreatures.place ( x = 0, y = 0)
        
        #C = Canvas(self, bg="gray", height=250, width=300)
        #backgroundPh = ImageTk.PhotoImage(file = "wallpaper.jpg")
        #background_label = Label(self, image=backgroundPh)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #background_label.pack()
    def save(self):
        
        # gera dicionario com as novas informacoes
        toSave = {"name": self.entryNPC.get(),"init" : self.entryInit.get(), "sheet" : self.entrySheet.get(), "hp" : self.entryHP.get(), "des": self.entryDES.get()}
        #toSave[self.entryNPC.get()] = dict( dict(("init", self.entryInit.get()), ("sheet", self.entrySheet.get(), ), ("hp",self.entryHP.get()), ("des", self.entryDES.get())  )) 
        print toSave
        for value in toSave:
            if toSave[value] == "" and value !="sheet":
                # CRIAR JANELA DE ERROR
                print 'saindo'
                return -1
        
        print toSave
        # carrega criaturas salvas
        jsonSave = json.loads(json.dumps(toSave))
        oldJson = open("data/npcs.json",'r')
        
        actualJson = json.loads( oldJson.read() )
        #verifica se nao existe
        if self.entryNPC.get() in actualJson['list'] :
            #CRIAR JANELA DE ERROR
            print 'existe'
            return -1
        oldJson.close()
        
        # escreve o novo json
        oldJson = open("data/npcs.json",'w')
        actualJson['list'].append(jsonSave)
        oldJson.write(json.dumps(actualJson))
        oldJson.close()
        



class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = rpgProject()
    app.mainloop()
