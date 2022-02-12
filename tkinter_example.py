from tkinter import *

class Bagels:


    def capturaDadosEntry(self):
            nome = self.palp.get() 
            self.msg['text'] = nome
            self.msg['fg'] = 'red'
            self.msg['font'] = '20'
            self.msg['width'] = 20

    def __init__(self, toplevel):
        self.frame1 = Frame(toplevel)
        self.frame2 = Frame(toplevel)
        self.frame3 = Frame(toplevel)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack(expand=True)

        self.font1 = ('verdana', '14', 'bold')
        Label(master = self.frame1, text='Tkinter Project', font= self.font1, fg='blue', height = 3).pack()

        
        #passo o pai do input

        self.font2 = ('verdana', '10', 'bold')

        self.palp = Entry(self.frame2, width= 20, text='', font = self.font2)
        self.palp.pack(side= LEFT)

        self.mostrar = Button(self.frame2, text='Mostra', width=10, font = self.font2, command=self.capturaDadosEntry)
        self.mostrar.pack(side = RIGHT)


        self.msg = Label(self.frame3, width= 10, text='')
        
        self.msg.pack()




instancia = Tk()

Bagels(instancia)
instancia.title('Jogo Bagels')
instancia.geometry('800x600')

instancia.mainloop()
