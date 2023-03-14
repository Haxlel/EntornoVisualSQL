from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk
from pymysql import *
from consultasSQL import consultas

class MainFrame(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.frameHome()
        
#Datos
    def fill_in_data(self):
        data = consultas().consulta_datos()
        totalRow = len(self.lstColumn)-1 
        for row in data:
            self.grid.insert('',END,text=row[0],values=tuple(row[1+i] for i in range(totalRow)))

# Limpiadores

    def clean_box(self):
        self.NombreCompleto.delete(0,END)
        self.FechaDeNacimiento.delete(0,END)
        self.Direccion.delete(0,END)
        self.LocalidadyCodigoPostal.delete(0,END)
        self.Telefono.delete(0,END)
        self.CorreoElectronico.delete(0,END)
        self.FechaDeAlta.delete(0,END)
        self.GrupoDeClientes.delete(0,END)

    def clean_grid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def box_clean_home(self):
        self.host.delete(0,END)
        self.user.delete(0,END)
        self.password.delete(0,END)
        self.dataBase.delete(0,END)
        self.table.delete(0,END)

# Habilitadores
    def box_enabler(self,estado):
        self.NombreCompleto.configure(state=estado)
        self.FechaDeNacimiento.configure(state=estado)
        self.Direccion.configure(state=estado)
        self.LocalidadyCodigoPostal.configure(state=estado)
        self.Telefono.configure(state=estado)
        self.CorreoElectronico.configure(state=estado)
        self.FechaDeAlta.configure(state=estado)
        self.GrupoDeClientes.configure(state=estado)

    def box_enabler_home(self,estado):   
        self.host.configure(state=estado)
        self.user.configure(state=estado)
        self.password.configure(state=estado)
        self.dataBase.configure(state=estado)
        self.table.configure(state=estado)

    def button_operation_enabler(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def button_save_enabler(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

#Frames Principales
    def frameHome(self):

        def signin():
            if self.host.get() == '' or self.user.get() == '' or self.dataBase.get() == '' or self.table.get() == '':
                messagebox.showerror('Error','Faltan campos por completar')
            else:
                rpt = messagebox.askquestion('Continuar', 'Desea continuar')
                if rpt == messagebox.YES:
                    self.frameWindgets()
                else:
                    pass

        frame = Frame(self.master,width=365,height=430,bg='white')
        frame.place(x=480,y=40)

        heading = Label(frame, text='MySQL',fg='#54a1f8',bg='white',font=('Microsoft YaHei UI Light',25,'bold'))
        heading.place(x=120,y=15)

        Label(frame,text='Host :',bg='#54a1f8',fg='white',font=('Microsoft YaHei UI Light',12),width=11).place(x=5,y=80)
        self.host = Entry(frame,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15))
        self.host.place(x=120,y=80)
        self.host.insert(0,'localhost')
        Frame(frame,width=220,height=2,bg='black').place(x=122,y=107)

        Label(frame,text='User :',bg='#54a1f8',fg='white',font=('Microsoft YaHei UI Light',12),width=11).place(x=5,y=130)
        self.user = Entry(frame,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15))
        self.user.place(x=120,y=130)
        self.user.insert(0,'root')
        Frame(frame,width=220,height=2,bg='black').place(x=122,y=157)

        Label(frame,text='Password :',bg='#54a1f8',fg='white',font=('Microsoft YaHei UI Light',12),width=11).place(x=5,y=180)
        self.password = Entry(frame,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15))
        self.password.place(x=120,y=180)
        Frame(frame,width=220,height=2,bg='black').place(x=122,y=207)

        Label(frame,text='Data base:',bg='#54a1f8',fg='white',font=('Microsoft YaHei UI Light',12),width=11).place(x=5,y=230)
        self.dataBase = Entry(frame,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15))
        self.dataBase.place(x=120,y=230)
        self.dataBase.insert(0,'clientes')
        Frame(frame,width=220,height=2,bg='black').place(x=122,y=257)

        Label(frame,text='Table:',bg='#54a1f8',fg='white',font=('Microsoft YaHei UI Light',12),width=11).place(x=5,y=280)
        self.table = Entry(frame,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',15))
        self.table.place(x=120,y=280)
        self.table.insert(0,'hoja1')
        Frame(frame,width=220,height=2,bg='black').place(x=122,y=307)

        self.box_enabler_home('disable')

        self.bttSingIn= Button(frame,width=20,pady=7,text='Sing in', bg='#57a1f8', fg='white',border=0, command=signin, font=('Microsoft YaHei UI Light',15)).place(x=80,y=350)

    def frameWindgets(self):
        self.mainFrame = Toplevel(self)
        self.mainFrame.title('Crud Python MySQL')
        self.mainFrame.minsize(width=1200, height=500)
        self.mainFrame.resizable(False,False)
        self.id = int(-1)

        #Frames principales
        self.lstColumn = consultas().column()

        self.first_frame()
        self.second_frame()
        self.third_frame()

        self.fill_in_data()
        self.box_enabler('disabled')
        self.button_save_enabler('disabled')

#Frames Secundarios
    def first_frame(self):

        BG = '#7B7D7D'
        FG = 'white'
        WIDTH = 140
        HEIGHT = 30

        fontStyle = tkFont.Font(family="Lucida Grande", size=14)

        def fNuevo():
            self.box_enabler('normal')
            self.button_operation_enabler('disabled')
            self.button_save_enabler('normal')
            self.NombreCompleto.focus()
              
        def fModificar():
            selected = self.grid.focus()
            values = self.grid.item(selected,'values')
            clave =  self.grid.item(selected,'text')

            if values == '':
                messagebox.showwarning("Modificar",'Debe seleccionar un elemento')
            else:
                self.id =int(clave)
                self.box_enabler('normal')
                self.clean_box()
                self.button_operation_enabler('disabled')
                self.button_save_enabler('normal')

                self.NombreCompleto.insert(0,values[0]),
                self.FechaDeNacimiento.insert(0,values[1]),
                self.Direccion.insert(0,values[2]),
                self.LocalidadyCodigoPostal.insert(0,values[3]),
                self.Telefono.insert(0,values[4]),
                self.CorreoElectronico.insert(0,values[5]),
                self.FechaDeAlta.insert(0,values[6]),
                self.GrupoDeClientes.insert(0,values[7]),

        def fEliminar():
            selected = self.grid.focus()
            values = self.grid.item(selected,'values')
            clave  =  self.grid.item(selected,'text')

            if values == '':
                messagebox.showwarning("Eliminar",'Debe seleccionar un elemento')
            else:
                self.box_enabler('normal')
                self.clean_box()
                self.NombreCompleto.insert(0,values[0]),
                self.FechaDeNacimiento.insert(0,values[1]),
                self.Direccion.insert(0,values[2]),
                self.LocalidadyCodigoPostal.insert(0,values[3]),
                self.Telefono.insert(0,values[4]),
                self.CorreoElectronico.insert(0,values[5]),
                self.FechaDeAlta.insert(0,values[6]),
                self.GrupoDeClientes.insert(0,values[7]),

                rpt = messagebox.askquestion('Eliminar',f'Deseas eliminar el registro seleccionado\nID:{clave}  ISO3:{values[0]}  Contry:{values[1]}')
                if rpt == messagebox.YES:
                    consultas().eliminar_datos(clave)
                    self.clean_grid()
                    self.clean_box()
                    self.fill_in_data()
                    self.box_enabler('disabled')
                    messagebox.showinfo('Eliminar','El elemento se elimino correctamente')
                else:
                    self.clean_box()
                    self.box_enabler('disabled')

        def fGuardar():
            if self.id == -1:
                consultas().insertar_datos(
                    self.NombreCompleto.get(),
                    self.FechaDeNacimiento.get(),
                    self.Direccion.get(),
                    self.LocalidadyCodigoPostal.get(),
                    self.Telefono.get(),
                    self.CorreoElectronico.get(),
                    self.FechaDeAlta.get(),
                    self.GrupoDeClientes.get()
                )
                self.clean_grid()
                self.clean_box()
                self.fill_in_data()
                self.box_enabler('disabled')
                self.button_save_enabler('disabled')
                self.button_operation_enabler('normal')
            else:
                rpt = messagebox.askquestion('Eliminar','Deseas modificar el registro seleccionado')
                if rpt == messagebox.YES:
                    consultas().modificar_datos(
                        self.id,
                        self.NombreCompleto.get(),
                        self.FechaDeNacimiento.get(),
                        self.Direccion.get(),
                        self.LocalidadyCodigoPostal.get(),
                        self.Telefono.get(),
                        self.CorreoElectronico.get(),
                        self.FechaDeAlta.get(),
                        self.GrupoDeClientes.get()
                    )
                    self.clean_grid()
                    self.clean_box()
                    self.fill_in_data()
                    self.box_enabler('disabled')
                    self.button_save_enabler('disabled')
                    self.button_operation_enabler('normal')
                    self.id = -1
                    messagebox.showinfo('Modificar','El elemento se modifico correctamente')
                else:
                    self.id = -1
                    self.clean_box()
                    self.button_save_enabler('disabled')
                    self.button_operation_enabler('normal')
                    self.box_enabler('disabled')
          
        def fCancelar():
            rpt = messagebox.askquestion('Cancelar','Esta seguro que desea cancelar')
            if rpt == messagebox.YES:
                self.clean_box()
                self.box_enabler('disabled')
                self.button_save_enabler('disabled')
                self.button_operation_enabler('normal')
            else:
                pass    

        frame = Frame(self.mainFrame,bg='#17202A')
        frame.place(x=2,y=0,width=150,height=500)
        
        self.btnNuevo=Button(frame,text='Nuevo',command=fNuevo, bg=BG, fg =FG, font=fontStyle,border=0)
        self.btnNuevo.place(x=5,y=15,width=WIDTH, height=HEIGHT)

        self.btnModificar=Button(frame,text='Modificar',command=fModificar, bg=BG, fg =FG,font=fontStyle,border=0)
        self.btnModificar.place(x=5,y=55,width=WIDTH, height=HEIGHT)

        self.btnEliminar=Button(frame,text='Eliminar',command=fEliminar,  bg=BG, fg =FG,font=fontStyle,border=0)
        self.btnEliminar.place(x=5,y=95,width=WIDTH, height=HEIGHT)

        self.btnGuardar = Button (frame,text='Guardar',command=fGuardar,bg='#2ECC71',fg='white',font=fontStyle,border=0)
        self.btnGuardar.place(x=5,y=415,width=WIDTH, height=HEIGHT)

        self.btnCancelar = Button (frame,text='Cancelar',command=fCancelar,bg='#E74C3C',fg='white',font=fontStyle,border=0)
        self.btnCancelar.place(x=5,y=455,width=WIDTH, height=HEIGHT)
   
    def second_frame(self):   
        BG = '#17202A'
        FG = 'white'

        fontStyle1 = tkFont.Font(family="Lucida Grande", size=12)
        fontStyle2 = tkFont.Font(family='Microsoft YaHei UI Light', size=14)

        frame = Frame(self.mainFrame,bg=BG)
        frame.place(x=152,y=0,width=240,height=500)

        Label(frame,text='Nombre Completo:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=15)
        self.NombreCompleto = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.NombreCompleto.place(x=5,y=40)

        Label(frame,text='Fecha de nacimiento:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=70)
        self.FechaDeNacimiento = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.FechaDeNacimiento.place(x=5,y=95)

        Label(frame,text='Dirección:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=125)
        self.Direccion = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.Direccion.place(x=5,y=150)

        Label(frame,text='Localidad y Código postal:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=180)
        self.LocalidadyCodigoPostal = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.LocalidadyCodigoPostal.place(x=5,y=205)
        
        Label(frame,text='Teléfono:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=235)
        self.Telefono = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.Telefono.place(x=5,y=260)

        Label(frame,text='Correo electrónico:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=290)
        self.CorreoElectronico = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.CorreoElectronico.place(x=5,y=315)
        
        Label(frame,text='Fecha de alta:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=345)
        self.FechaDeAlta = Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.FechaDeAlta.place(x=5,y=370)

        Label(frame,text='Grupo de clientes:',font=fontStyle1,bg=BG,fg=FG).place(x=5,y=400)
        self.GrupoDeClientes= Entry(frame,fg='black',border=1,bg='white',font=fontStyle2)
        self.GrupoDeClientes.place(x=5,y=425)        

    def third_frame(self): 

        frame = Frame(self.mainFrame)
        frame.place(x=394,y=0,width=800,height=500)

        self.grid = ttk.Treeview(frame,columns=tuple([ f'col{i+1}'for i in range(len(self.lstColumn)-1)]))

        self.grid.column('#0', width=60)    
        for i in range(len(self.lstColumn)-1):
            self.grid.column(f'col{i+1}', width=180, anchor=CENTER)

        self.grid.heading('#0', text=f'{self.lstColumn[0]}',anchor=CENTER ) 
        for i in range(len(self.lstColumn)-1):
            self.grid.heading(f'col{i+1}', text=f'{self.lstColumn[i+1]}', anchor=CENTER)    

        sb1 = Scrollbar(frame,orient=HORIZONTAL)
        sb1.pack(side=BOTTOM,fill=X)
        
        sb = Scrollbar(frame,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)

        self.grid.pack(side=LEFT, fill = Y)

        self.grid.config(yscrollcommand=sb.set)
        self.grid.config(xscrollcommand=sb1.set)
        sb.config(command=self.grid.yview)
        sb1.config(command=self.grid.xview)
        self.grid['selectmode']='browse'