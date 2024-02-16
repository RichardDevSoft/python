import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window("Formulário")
app.geometry("500x500")
style = Style(theme="cyborg")

label = ttk.Label(app, text="Formulário de Inscrição")
label.pack(pady=35)
label.config(font=("Arial", 20, "bold"))

nome = ttk.Frame(app)
nome.pack(pady=18, padx=10, fill="x")
ttk.Label(nome, text="Nome").pack(side=LEFT, padx=5)
ttk.Entry(nome).pack(side=LEFT, fill="x", expand=True, padx=5)


app.mainloop()