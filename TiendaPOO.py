import customtkinter as kc
from time import strftime
from PIL import Image


class VentanaSecundaria(kc.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.tienda = parent

        self.geometry("300x200")
        self.attributes("-topmost", True)
        self.title("Confirmación")

        self.LabelPregunta = kc.CTkLabel(
            self, text="¿Seguro que quieres comprar este poder?", font=("Arial", 13)
        )
        self.LabelPregunta.pack(pady=20)

        self.BotonSI = kc.CTkButton(
            self,
            text="Sí",
            command=self.confirmar_compra,
            fg_color="green",
            hover_color="darkgreen",
        )
        self.BotonSI.pack(pady=10)

        self.BotonNo = kc.CTkButton(
            self, text="No", command=self.destroy, fg_color="red", hover_color="darkred"
        )
        self.BotonNo.pack(pady=10)
    def CambioLabel(self):
        self.tienda.labelDinero.configure(text=f"Saldo: {self.tienda.Dinero}$")    

    def confirmar_compra(self):
       

        

        if self.tienda.Dinero >= 10:
            self.tienda.Dinero -= 10
            self.tienda.labelDinero.configure(text=f"Saldo: {self.tienda.Dinero}$")
            print("Compra realizada con éxito")
        else:
            print("Saldo insuficiente")
            self.tienda.labelDinero.configure(text="No tienes dinero chat")
            self.tienda.labelDinero.after(2000,self.CambioLabel)

        self.destroy()


class Tienda(kc.CTk):

    def __init__(self):
        super().__init__()
        self.Dinero = 100
        self.ventana_abierta = None

        try:
            imagenFuerza = Image.open("Fuerza.png")
            self.ImagenParaFuerza = kc.CTkImage(
                light_image=imagenFuerza, dark_image=imagenFuerza, size=(120, 120)
            )
            imagenResistencia = Image.open("Resistencia.png")
            self.ImagenParaResistencia = kc.CTkImage(
                light_image=imagenResistencia,
                dark_image=imagenResistencia,
                size=(120, 120),
            )
            imagenRegeneracion = Image.open("Regeneracion.png")
            self.ImagenParaRegeneracion = kc.CTkImage(
                light_image=imagenRegeneracion,
                dark_image=imagenRegeneracion,
                size=(120, 120),
            )
        except FileNotFoundError:

            self.ImagenParaFuerza = None
            self.ImagenParaResistencia = None
            self.ImagenParaRegeneracion = None

        self.fuente_reloj = ("Segoe UI", 14, "bold")
        self.fuente_titulo = ("Helvetica", 24, "bold")
        self.fuente_botones = ("Arial", 12, "bold")
        self.fuente_labels = ("Arial", 13, "normal")
        self.fuente_dinero = ("Segoe UI", 15, "bold")
       

        self.after(0, lambda: self.state("zoomed"))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.FrameTienda = kc.CTkFrame(
            self,
            width=400,
            height=700,
            corner_radius=20,
            border_width=5,
            border_color="#000000",
        )
        self.FrameTienda.grid(row=0, column=0, pady=20)
        self.FrameTienda.grid_columnconfigure(0, weight=1)

        self.FrameSuperior = kc.CTkFrame(self.FrameTienda, height=50, corner_radius=15)
        self.FrameSuperior.grid(row=0, column=0, sticky="nwe", padx=10, pady=10)
        self.FrameSuperior.grid_propagate(False)
        self.FrameSuperior.grid_columnconfigure(1, weight=1)

        self.LabelTiempo = kc.CTkLabel(
            self.FrameSuperior, text="", font=self.fuente_reloj
        )
        self.LabelTiempo.grid(row=0, column=0, sticky="w", padx=(15, 0), pady=10)

        self.labelDinero = kc.CTkLabel(
            self.FrameSuperior,
            text=f"Saldo: {self.Dinero}$",
            font=self.fuente_dinero,
            text_color="#2e63cc",
        )
        self.labelDinero.grid(row=0, column=1, sticky="e", padx=(0, 15), pady=10)

        self.Tiempo()

        self.LabelEncabezado = kc.CTkLabel(
            self.FrameTienda,
            text="Tienda Poderes",
            font=self.fuente_titulo,
            text_color="#1f538d",
        )
        self.LabelEncabezado.grid(row=1, column=0, sticky="N", pady=(10, 0))

        self.FrameFuerza = kc.CTkFrame(self.FrameTienda, width=360, height=160)
        self.FrameFuerza.grid(row=2, column=0, pady=15, padx=20)
        self.FrameFuerza.grid_propagate(False)
        self.FrameFuerza.grid_columnconfigure(1, weight=1)

        self.LabelImagenCarlos = kc.CTkLabel(
            self.FrameFuerza, text="", image=self.ImagenParaFuerza
        )
        self.LabelImagenCarlos.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.LabelNombrePoder = kc.CTkLabel(
            self.FrameFuerza,
            text="Super Fuerza",
            font=("Arial", 16, "bold"),
            anchor="w",
        )
        self.LabelNombrePoder.grid(row=0, column=1, sticky="w", padx=10, pady=(15, 0))

        self.LabelDescPoder = kc.CTkLabel(
            self.FrameFuerza,
            text="Multiplica tu fuerza física\npara derribar cualquier obstáculo.",
            font=self.fuente_labels,
            justify="left",
            anchor="w",
        )
        self.LabelDescPoder.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.BotonComprar = kc.CTkButton(
            self.FrameFuerza,
            text="Comprar",
            font=self.fuente_botones,
            width=100,
            height=30,
            command=self.VSecu,
        )
        self.BotonComprar.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 15))

        self.FrameResistencia = kc.CTkFrame(self.FrameTienda, width=360, height=160)
        self.FrameResistencia.grid(row=3, column=0, pady=15, padx=20)
        self.FrameResistencia.grid_propagate(False)
        self.FrameResistencia.grid_columnconfigure(1, weight=1)

        self.LabelImagenCarlos2 = kc.CTkLabel(
            self.FrameResistencia, text="", image=self.ImagenParaResistencia
        )
        self.LabelImagenCarlos2.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.LabelNombrePoder2 = kc.CTkLabel(
            self.FrameResistencia,
            text="Super Resistencia",
            font=("Arial", 16, "bold"),
            anchor="w",
        )
        self.LabelNombrePoder2.grid(row=0, column=1, sticky="w", padx=10, pady=(15, 0))

        self.LabelDescPoder2 = kc.CTkLabel(
            self.FrameResistencia,
            text="Desarrolla una piel indestructible \ny una dureza inquebrantable.",
            font=self.fuente_labels,
            justify="left",
            anchor="w",
        )
        self.LabelDescPoder2.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.BotonComprar2 = kc.CTkButton(
            self.FrameResistencia,
            text="Comprar",
            font=self.fuente_botones,
            width=100,
            height=30,
            command=self.VSecu,
        )
        self.BotonComprar2.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 15))

        self.FrameRegeneracion = kc.CTkFrame(self.FrameTienda, width=360, height=160)
        self.FrameRegeneracion.grid(row=4, column=0, pady=15, padx=20)
        self.FrameRegeneracion.grid_propagate(False)
        self.FrameRegeneracion.grid_columnconfigure(1, weight=1)

        self.LabelImagenCarlos3 = kc.CTkLabel(
            self.FrameRegeneracion, text="", image=self.ImagenParaRegeneracion
        )
        self.LabelImagenCarlos3.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        self.LabelNombrePoder3 = kc.CTkLabel(
            self.FrameRegeneracion,
            text="Regeneración Divina",
            font=("Arial", 16, "bold"),
            anchor="w",
        )
        self.LabelNombrePoder3.grid(row=0, column=1, sticky="w", padx=10, pady=(15, 0))

        self.LabelDescPoder3 = kc.CTkLabel(
            self.FrameRegeneracion,
            text="Sana cualquier herida o daño\nrecibido de forma inmediata.",
            font=self.fuente_labels,
            justify="left",
            anchor="w",
        )
        self.LabelDescPoder3.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        self.BotonComprar3 = kc.CTkButton(
            self.FrameRegeneracion,
            text="Comprar",
            font=self.fuente_botones,
            width=100,
            height=30,
            command=self.VSecu,
        )
        self.BotonComprar3.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 15))
        
        self.precioLabel = kc.CTkLabel(self.FrameRegeneracion,text="10$",text_color="#006aff")
        self.precioLabel.grid(row=3,column=1,sticky="E",padx=(0,10),pady=(0,2))
        self.precioLabel = kc.CTkLabel(self.FrameFuerza,text="10$",text_color="#006aff")
        self.precioLabel.grid(row=3,column=1,sticky="E",padx=(0,10),pady=(0,2))
        self.precioLabel = kc.CTkLabel(self.FrameResistencia,text="10$",text_color="#006aff")
        self.precioLabel.grid(row=3,column=1,sticky="E",padx=(0,10),pady=(0,2))

    def Tiempo(self):
        TiempoText_12h = strftime("%I:%M:%S %p")
        self.LabelTiempo.configure(text=TiempoText_12h)
        self.LabelTiempo.after(1000, self.Tiempo)

    def VSecu(self):

        if self.ventana_abierta is None or not self.ventana_abierta.winfo_exists():
            self.ventana_abierta = VentanaSecundaria(self)
        else:

            self.ventana_abierta.focus()

       


if __name__ == "__main__":
    App = Tienda()
    App.mainloop()
