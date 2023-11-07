import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os

from r1092 import Portfolio

from tkcalendar import DateEntry
import webbrowser
from tkinter import filedialog

brazilian_stocks = [
    'PETR4', 'VALE3', 'ITUB4', 'BBDC4', 'ABEV3',
    'WEGE3', 'BBAS3', 'MGLU3', 'SUZB3', 'ALPA4', 'ALUP11',
    'ALUP3', 'ALUP4', 'ANIM3', 'ARZZ3', 'ATMP3', 'ATOM3',
    'AZEV3', 'BIDI11', 'BIDI3', 'BIDI4', 'BOBR3', 'BOBR4',
    'BOVA11', 'BPAC3', 'BPAN4', 'BRAP4', 'BEEF3', 'BPAC11',
    'BRAP3', 'BRKM3', 'CCRO3', 'CGRA3',
    'COGN3', 'CPLE6', 'CSAN3', 'CVCB3', 'CYRE3', 'ECOR3',
    'EGIE3', 'ELET3', 'ELET6', 'EMBR3', 'ENBR3', 'EQTL3',
    'FLRY3', 'GGBR3', 'GOAU3', 'GOLL3', 'HAPV3', 'HGTX3',
    'IGTA3', 'IRBR3', 'ITSA3', 'JHSF3', 'KLBN4', 'LAME3',
    'LCAM3', 'LREN3', 'MGLU3', 'MRFG3', 'MRVE3', 'MULT3',
    'NATU3', 'PCAR4', 'PETR3', 'QUAL3', 'RADL3', 'RAIL3',
    'RENT3', 'SANB3', 'SAPR11', 'SBSP3', 'SMLS3', 'SUZB3',
    'TAEE3', 'TIMP3', 'TOTS3', 'UGPA3', 'USIM3', 'VIVT3',
    'VVAR3', 'WEGE3', 'YDUQ3', 'ABEV3', 'AZUL4', 'B3SA3',
    'BBAS3', 'BBDC3', 'BBDC4',
    'BBSE3', 'BRAP4', 'BRDT3', 'BRFS3', 'BRKM5', 'BRML3',
    'B3SA3', 'CCRO3', 'CIEL3', 'CMIG4', 'COGN3', 'CPFE3',
    'CRFB3', 'CSAN3', 'CSNA3', 'CVCB3', 'CYRE3', 'ECOR3',
    'EGIE3', 'ELET3', 'ELET6', 'EMBR3', 'ENBR3', 'EQTL3',
    'FLRY3', 'GGBR4', 'GOAU4', 'GOLL4', 'HAPV3', 'HGTX3',
    'IGTA3', 'IRBR3', 'ITSA4', 'ITUB3', 'ITUB4', 'JBSS3',
    'KLBN11', 'LAME4', 'LREN3', 'MGLU3', 'MRFG3', 'MRVE3',
    'MULT3', 'NATU3', 'PCAR3', 'PETR3', 'PETR4', 'QUAL3',
    'RADL3', 'RAIL3', 'RENT3', 'SANB11', 'SBSP3', 'SMLS3',
    'SUZB3', 'TAEE11', 'TIMP3', 'TOTS3', 'UGPA3', 'USIM5',
    'VALE3', 'VIVT3', 'VIVT4', 'VVAR3', 'WEGE3', 'YDUQ3',
    'BRFS3', 'BRKM5', 'BRML3', 'BRPR3', 'BRSR3', 'BRSR6',
    'BSEV3', 'CAMB3', 'CCPR3', 'CEAB3', 'CEAB5', 'CEAB6',
    'CESP3', 'CESP5', 'CESP6', 'CGAS3', 'CGAS5', 'CGRA3',
    'CGRA4', 'CIEL3', 'CLSC4', 'CMIG4', 'CMIG4', 'CMIGB4',
    'CMIGB6', 'CMIGC6', 'CNTO3', 'COGN3', 'CPFE3', 'CPLE3',
    'CPLE6', 'CPRE3', 'CRFB3', 'CSAB3', 'CSAB4', 'CSAN3',
    'CSRN3', 'CSRN5', 'CSRN6', 'CTKA3', 'CTKA4', 'CTNM3',
    'CTNM4', 'CVCB3', 'CYRE3', 'DASA3', 'DIRR3', 'DIRR6',
    'DMMO3', 'DMMO4', 'DOHL3', 'DOHL4', 'DTEX3', 'EALT4',
    'ECOR3', 'ECOR4', 'ECPG3', 'ECPG4', 'EEEL3', 'EEEL4',
    'EGIE3', 'ELEK3', 'ELEK4', 'ELET3', 'ELET6', 'ELPL3',
    'ELPL4', 'EMAE4', 'EMBR3', 'ENBR3', 'ENMA3', 'ENMA6',
    'ENMT3', 'ENMT4', 'EQPA3', 'EQPA5', 'EQPA6', 'EQTL3',
    'ESTR3', 'ESTR4', 'ETER3', 'EUCA4', 'EVEN3', 'EZZE',
    'FESA3', 'FESA4', 'FHER3', 'FJTA4', 'FLRY3', 'FRAS3',
    'FRIO3', 'GEPA3', 'GEPA4', 'GFSA3', 'GFSA3B', 'GGBR3',
    'GOAU3', 'GOAU4', 'GOGL34', 'GOLL3', 'GPAR3', 'GPIV33',
    'GPIV4', 'GRND3', 'GSHP3', 'GSHP4', 'GUAR3', 'GUAR4',
    'GUAR4B', 'HAGA4', 'HAPV3', 'HBTS5', 'HETA4', 'HGTX3',
    'HYPE3', 'IDNT3', 'IDVL3', 'IGBR3', 'IGBR5', 'IGBR6',
    'IGTA3', 'IGTA3B', 'INHA3', 'INHA4', 'INSC3', 'IRBR3',
    'IRBR3B', 'IRBR3C', 'ITSA3', 'ITSA4', 'ITSA4B', 'ITUB3',
    'ITUB3B', 'ITUB4', 'ITUB4B', 'JBSS3', 'JFEN3', 'JHSF3',
    'JOPA3', 'JOPA4', 'JSLG3', 'KEPL3', 'KEPL4', 'KLBN11',
    'KLBN3', 'KLBN4', 'LAME3', 'LAME4', 'LATM11', 'LBRN3',
    'LBRN5', 'LBRN6', 'LEVE3', 'LIGT3', 'LINX3', 'LLIS3',
    'LOGG3', 'LOGN3', 'LOGN11', 'LPSB3', 'LREN3', 'LUPA3',
    'LUPA4', 'LWSA3', 'LWSA3B', 'LXRE3', 'MACY34', 'MAGG3',
    'MAGS3', 'MALL11', 'MALL3', 'MALL4', 'MAPT3', 'MAPT4',
    'MDIA3', 'MDNE3', 'MDNE4', 'MGLU3', 'MILS3', 'MLAS3',
    'MMXM3', 'MMXM11', 'MOAR3', 'MOAR4', 'MOVI3', 'MRFG3',
    'MRVE3', 'MRVE3B', 'MTIG4', 'MTRE3', 'MTSA3', 'MTSA4',
    'MULT3', 'MYPK3', 'N1CE34', 'NEOE3', 'NEOE4', 'NEOE4B',
    'NORD3', 'NRTQ3', 'NUTR3', 'ODER3', 'ODER4', 'OMGE3',
    'OMGE3B', 'ORPD3', 'OSXB3', 'OSXB3B', 'OTRK3', 'P1GG34',
    'PAES3', 'PAES4', 'PARD3', 'PARD3B', 'PATI3', 'PATI4',
    'PATI4B', 'PCAR3', 'PCAR4', 'PCAR5', 'PCAR5B', 'PCAR6',
    'PCAR6B', 'PDGR3', 'PETR3', 'PETR4', 'PETR4B', 'PFIZ34',
    'PFRM3', 'PFRM3B', 'PINE4', 'PINE4B', 'PLAS3', 'PLAS3B',
    'PLPL3', 'PLPL4', 'PLPL4B', 'PLRI11', 'PMAM3', 'PMAM4',
    'PMAM4B', 'PNVL3', 'PNVL4', 'PNVL4B', 'POWE3', 'PPLA11',
    'PPLA3', 'PPLA4', 'PPLA4B', 'PPLA4C', 'PRBC3', 'PRBC4',
    'PRBC4B', 'PSSA3', 'PTBL3', 'PTBL3B', 'PTNT3', 'PTNT4',
    'PTNT4B', 'QUAL3', 'RADL3', 'RAIL3', 'RAIL4', 'RAIL4B',
    'RAPT3', 'RAPT4', 'RAPT4B', 'RCSL3', 'RCSL4', 'RCSL4B',
    'RDNI3', 'RDNI3B', 'RDOR3', 'RDOR4', 'RDOR4B', 'REDE3',
    'REDE4', 'REDE4B', 'RENT3', 'RNEW11', 'RNEW3', 'RNEW4',
    'RNEW4B', 'RSID3', 'RSID3B', 'RSPD3', 'RSPD4', 'RSPD4B',
    'RSUL4', 'S3SC3', 'SAPR3', 'SAPR4', 'SAPR4B', 'SAPR4C',
    'SBSP3', 'SEER3', 'SHOW3', 'SHOW4', 'SHUL4', 'SHUL4B',
    'SHUL4C', 'SLCE3', 'SLCE4', 'SLED3', 'SLED4', 'SLED4B',
    'SMLS3', 'SMLS3B', 'SMTO3', 'SOMA3', 'SOMA4', 'SOMA4B',
    'SPRI3', 'SPRI5', 'SPRI6', 'STBP3', 'STBP3B', 'STKF3',
    'STKF4', 'STKF4B', 'STTR3', 'STTR4', 'STTR4B', 'SULA11',
    'SULA3', 'SULA4', 'SULA4B', 'SULA4C', 'SULA4D', 'SULA4E',
    'TASA3', 'TASA4', 'TASA4B', 'TCNO3', 'TCNO4', 'TECN3',
    'TEKA3', 'TEKA4', 'TEKA4B', 'TEND3', 'TESA3', 'TESA4',
    'TESA4B', 'TGMA3', 'TGMA3B', 'TGMA4', 'TGMA4B', 'TORD3',
    'TORD3B', 'TOYB3', 'TOYB3B', 'TOYB4', 'TOYB4B', 'TPIS3',
    'TPIS3B', 'TRIS3', 'TRIS4', 'TRIS4B', 'TRPL3', 'TRPL4',
    'TRPL4B', 'TSLA34', 'TSLA35', 'TUPY3', 'TUPY4', 'TXRX3',
    'TXRX4', 'UCAS3', 'UCAS4', 'UGPA3', 'UGPA3B', 'UNIP3',
    'UNIP5', 'UNIP6', 'UPAC33', 'UPAC34', 'UPSS34', 'URPR11',
    'USIM3', 'USIM3B', 'USIM5', 'USIM5B', 'USIM6', 'USIM6B',
    'USIN11', 'USIN3', 'USIN4', 'USIN4B', 'UTEC34', 'VALE3',
    'VCPA3', 'VCPA4', 'VEVE3', 'VINE3', 'VIVO3', 'VIVO4',
    'VIVT3', 'VIVT4', 'VLID3', 'VLID4', 'VNET3', 'VNET4',
    'VPTA3', 'VPTA4', 'VPTA4B', 'VSPT3', 'VSPT4', 'VSPT4B',
    'VULC3', 'VULC4', 'VULC4B', 'VVAR11', 'WEGE3', 'WHRL3',
    'WHRL4', 'WHRL4B', 'WIZS3', 'WIZS3B', 'WSON33', 'WUNI11',
    'WUNI3', 'WUNI5', 'WUNI6', 'YBRA3', 'YBRA4']

print(len(brazilian_stocks))
brazilian_stocks = list(set(brazilian_stocks))
brazilian_stocks.sort()
print(len(brazilian_stocks))
for i in brazilian_stocks:
    brazilian_stocks[brazilian_stocks.index(i)] = [i, 10]
brazilian_stocks_dict = {}
for i in brazilian_stocks:
    brazilian_stocks_dict[i[0]] = i[1]

usr_portfolio = Portfolio(brazilian_stocks, "Meu portifolio")

print(brazilian_stocks_dict)
scrollslabelslist = []
editstocklabelslist=[]
varnotfill = "???"


def argumentedfunction():
    no_web_err(root=root)


def riskcalc_window():
    j = tk.Tk()

    def riskrun_btn():
        print("entrou na riskrun_btn")
        sel_var = risk_var.get()
        if sel_var == 1:
            pass
            #  chamar a risco aqui(dia)

        if sel_var == 2:
            pass
            #  chamar a risco aqui(mes)
        if sel_var == 3:
            pass
            #  chamar a risco aqui(ano)
        # pegar o resultado e pllottar
        j.destroy()

    j.geometry("300x200")
    j.title("Calcular risco")
    riskcalc_label = tk.Label(j, text="Selecione o periodo do risco:")
    riskcalc_label.place(x=50, y=20)
    risk_var = tk.IntVar()
    r1 = tk.Radiobutton(j, text="Dia", variable=risk_var, value=1)
    r1.place(x=50, y=50)
    r2 = tk.Radiobutton(j, text="Mes", variable=risk_var, value=2)
    r2.place(x=50, y=80)
    r3 = tk.Radiobutton(j, text="Ano", variable=risk_var, value=3)
    r3.place(x=50, y=110)
    r1.select()

    exitbtn = tk.Button(j, text="iniciar simulação", command=riskrun_btn)
    exitbtn.place(x=100, y=150)

    j.mainloop()


def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int(event.delta * 0.01), "units")


def no_web_err(root):
    root.destroy()
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Sem acesso a internet")

    tk.Label(root, text="Sem acesso a internet \n Reinicie o aplicativo ou tente mais tarde").place(relx=0.2, rely=0.5)
    tk.Button(root, text="OK", command=root.destroy).place(relx=0.45, rely=0.7)


def portfoloioedit_window():
    def adicionar_elemento():
        elemento = entry.get()
        lista.append({"nome": elemento, "selecionado": tk.BooleanVar()})
        update_lista()

    def save_changes():
        pass
        global usr_portfolio
        usr_portfolio.portfolio.clear()



    def on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_frame_configure(event):
        canvas.itemconfig(canvas_frame, width=canvas.winfo_width())

    def update_lista():
        for widget in lista_frame.winfo_children():
            widget.destroy()

        for idx, elemento in enumerate(lista):
            frame = tk.Frame(lista_frame)
            frame.pack(fill="x")

            label = tk.Label(frame, text=elemento["nome"])
            label.pack(side="left")

            entry = tk.Entry(frame)
            if label.cget("text") in usr_portfolio.portfolio:
                print(label.cget("text"))
                entry.insert(0, usr_portfolio.portfolio[label.cget('text')])
            entry.pack(side="left")

            checkbox = tk.Checkbutton(frame, variable=elemento["selecionado"])
            checkbox.place(relx=0.7)

        # Atualize o scrollregion do canvas para incluir todo o conteúdo
        canvas.update_idletasks()  # Garante que os widgets estejam totalmente atualizados
        canvas.configure(scrollregion=canvas.bbox("all"))

    lista = []

    root = tk.Tk()
    root.title("Editar portifolio")
    root.geometry("400x500")

    entry = tk.Entry(root)
    entry.pack(side="top", padx=100)

    adicionar_button = tk.Button(root, text="Adicionar", command=adicionar_elemento)
    adicionar_button.pack(side="top")

    remover_button = tk.Button(root, text="Salvar alterações")
    remover_button.pack(side="top")

    canvas = tk.Canvas(root)
    canvas.pack(side="top", fill="both", expand=True)
    canvas_frame = canvas.create_window((0, 0), window=None, anchor='nw')

    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=0.95, rely=+0.15, relheight=0.85)

    canvas.configure(yscrollcommand=scrollbar.set)

    lista_frame = tk.Frame(canvas)
    lista_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)
    canvas.itemconfig(canvas_frame, window=lista_frame)
    for key in usr_portfolio.portfolio:
        lista.append({"nome": key, "selecionado": tk.BooleanVar()})

    update_lista()

    root.mainloop()

def update_scrollbar_elements(selected_items):
    pass
def creditwindow():
    j = tk.Tk()
    j.geometry("300x300")
    j.title("creditos")

    credits_text = tk.Label(j,
                            text="Creditos: \n                          Graficos:Henrique Assis \n   Plotagem: \n                     Arquivos:Emilio Vital \n                                  API financeira:Leticia Aleixo \n                           Risco:Gabriella Morgado")
    credits_text.place(x=-90, y=20)
    gitcredittext = tk.Label(j, text="Github:")
    gitcredittext.place(x=0, y=135)
    gitcreditlink = tk.Label(j, text="https://github.com/emiliobrazil/portfolio_analysis", fg="blue")
    gitcreditlink.place(x=0, y=150)
    gitcreditlink.bind("<Button-1>",
                       lambda e: webbrowser.open_new_tab("https://github.com/emiliobrazil/portfolio_analysis"))
    tk.Label(j, text="Disponibilizado em Apache-2.0").place(x=0, y=175)
    tk.Label(j, text="Desenvolvido em: 2023").place(x=100, y=225)

    creditbtn = tk.Button(j, text="fechar", command=j.destroy)
    creditbtn.place(x=135, y=250)


def open_file():
    # Lógica para abrir um arquivo
    global usr_portfolio
    file_name = tk.filedialog.askopenfilename()
    file_name = file_name.replace("/", os.sep)
    file_name=file_name.replace("\\",os.sep)
    if file_name !="":
        usr_portfolio = usr_portfolio.load(file_name)


def period_selector():
    j = tk.Tk()
    j.geometry("270x380")
    j.title("selecionar periodo")

    tk.Label(j, text="Selecione o periodo", font=25).place(x=50, y=10)
    tk.Label(j, text="Inicio:").place(x=0, y=50)
    tk.Label(j, text="Fim:").place(x=0, y=130)

    inical = DateEntry(j, width=16, background="blue", foreground="white", bd=2, date_pattern='dd/mm/yyyy')
    inical.place(x=10, y=90)

    endcal = DateEntry(j, width=16, background="blue", foreground="white", bd=2, date_pattern='dd/mm/yyyy')
    endcal.place(x=10, y=170)

    def periodselctorbtn_command():
        inicalg = inical.get_date()
        endcalg = endcal.get_date()
        inicaldatalist = [inicalg.day, inicalg.month, inicalg.year]
        endcaldatalist = [endcalg.day, endcalg.month, endcalg.year]
        upareaperiod_label.config(
            text=f"periodo analisado:\nde: {inicaldatalist[0]}/{inicaldatalist[1]}/{inicaldatalist[2]} \nate: {endcaldatalist[0]}/{endcaldatalist[1]}/{endcaldatalist[2]}")

    period_fselbt = tk.Button(j, text="Selecionar", command=periodselctorbtn_command)
    period_fselbt.place(x=110, y=320)

    j.mainloop()


def save_file():
    # Lógica para salvar um arquivo

    file_name = tk.filedialog.asksaveasfilename( **{
        'defaultextension': ".jprt",
        'filetypes': [("Arquivo de portifolio", "*.jprt"),("Arquivos de Texto", "*.txt") ,("Todos os Arquivos", "*.*")]
    })
    file_name = file_name.replace("/", os.sep)
    file_name=file_name.replace("\\",os.sep)
    print(file_name)
    if file_name !="":
        usr_portfolio.save(file_name)


def change_label_color(event, label):
    for i in scrollslabelslist:
        i.config(bg="lightgray")
    label.config(bg="blue")
    stockname_label.config(text=label.cget("text"))
    stockarea_title.config(text=f'Analise da empresa {label.cget("text")}')
    stocknametext = stockname_label.cget("text").replace(" ", "")
    stocknumber_label.configure(text=f'Você possui {usr_portfolio[stocknametext]} ações nessa empresa')


def cut_text():
    # Lógica para recortar texto
    pass


def copy_text():
    # Lógica para copiar texto
    pass


def paste_text():
    # Lógica para colar texto
    pass


def update_tocks_scroll(p_window, scroll, stock_list):
    pass


root = tk.Tk()
root.geometry("800x600")
root.title("analise de portifolio")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)

setup_menu = tk.Menu(menu_bar, tearoff=0)
setup_menu.add_command(label="Recortar", command=cut_text)
setup_menu.add_command(label="Copiar", command=copy_text)
setup_menu.add_command(label="sem net", command=argumentedfunction)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Guia de uso", command=cut_text)
help_menu.add_command(label="Creditos", command=creditwindow)

menu_bar.add_cascade(label="Arquivo", menu=file_menu)
menu_bar.add_cascade(label="Confiurações", menu=setup_menu)
menu_bar.add_cascade(label="Ajuda", menu=help_menu)

root.config(menu=menu_bar)

main_frame = tk.Frame(root, width=800, height=600)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.place(x=20, y=0)
# Crie um frame secundário dentro do frame principal com tamanho menor
sub_frame = tk.Frame(main_frame, width=300, height=500)
sub_frame.pack()

# Crie uma barra de rolagem vertical para o frame secundário
scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
scrollbar.place(x=100, y=0, relheight=0.99)  # Define a posição e altura da barra de rolagem

# Crie um canvas dentro do frame secundário
canvas = tk.Canvas(sub_frame, yscrollcommand=scrollbar.set, width=300, height=500)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure a barra de rolagem
scrollbar.config(command=canvas.yview)
canvas.bind("<MouseWheel>", on_mouse_wheel)

# Crie um frame dentro do canvas para adicionar conteúdo
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Adicione conteúdo ao frame (substitua isto pelo seu conteúdo real)
for i in brazilian_stocks:
    label = tk.Label(content_frame, text=f" {i[0]}")
    label.bind("<Button-1>", lambda event, label=label: change_label_color(event, label))
    label.bind("<MouseWheel>", on_mouse_wheel)
    label.pack()
    scrollslabelslist.append(label)


# Atualize o canvas quando o conteúdo for modificado
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


vertical_separator = ttk.Separator(master=root, orient="vertical")
vertical_separator.pack(fill="y", pady=10, expand=True)

vertical_separator.place(x=150, relheight=1, relwidth=1)
stockarea_title = tk.Label(root, text=f"Analise da empresa {varnotfill}", font=25)
stockarea_title.place(x=350, y=10)

stockname_label = tk.Label(root, text=f"{varnotfill}")
stockname_label.place(x=220, y=70)

stockvalue_label = tk.Label(root, text=f"R$:{varnotfill}")
stockvalue_label.place(x=550, y=70)

stocknumber_label = tk.Label(root, text=f"voce possui: {varnotfill} ações nesse empresa")
stocknumber_label.place(x=300, y=330)

upareaperiod_label = tk.Label(root,
                              text=f"periodo analisado:\nde: {varnotfill}/{varnotfill}/{varnotfill} \nate: {varnotfill}/{varnotfill}/{varnotfill}")
upareaperiod_label.place(x=650, y=200)

upperiodbtn = tk.Button(root, text="selecionar periodo", command=period_selector)
upperiodbtn.place(x=650, y=250)

stock_graphimg = Image.open(os.sep.join([os.getcwd(), "gcache", "u2clm4ND_mid.png"]))
stock_graphimg.thumbnail((400, 225))
photo = ImageTk.PhotoImage(stock_graphimg)

# Crie um widget Label para exibir a imagem
stock_graph_label = tk.Label(root, image=photo)
stock_graph_label.image = photo  # Mantém uma referência à imagem para evitar que ela seja coletada pelo coletor de lixo
stock_graph_label.pack()
stock_graph_label.place(x=220, y=100)
horizontal_separator = ttk.Separator(
    master=root,
    orient="horizontal"
)
horizontal_separator.pack(fill="x", padx=10, expand=True)

horizontal_separator.place(x=152, rely=0.67, relwidth=1, relheight=1)

risktitlelabel = tk.Label(root, text="Gerenciamento de risco:", font=25)
risktitlelabel.place(x=360, y=410)

risklabel = tk.Label(root, text=f"Risco:R${varnotfill}")
risklabel.place(x=200, y=450)

cashlabel = tk.Label(root, text=f"Saldo:R${varnotfill}")
cashlabel.place(x=200, y=470)

periodlabel = tk.Label(root,
                       text=f"periodo: de: {varnotfill}/{varnotfill}/{varnotfill}- até: {varnotfill}/{varnotfill}/{varnotfill}")
periodlabel.place(x=200, y=490)

lastriskupdate = tk.Label(root, text=f"ultimo calculo de risco: {varnotfill}/{varnotfill}/{varnotfill}")
lastriskupdate.place(x=450, y=490)

moneyreturnlabel = tk.Label(root, text=f"Retorno: R${varnotfill}")
moneyreturnlabel.place(x=450, y=470)

lastsimbutton=tk.Button(root, text="Ultima simulação", )
lastsimbutton.place(x=330, y=540)
riskbutton = tk.Button(root, text="calcular risco", command=riskcalc_window)
riskbutton.place(x=450, y=540)

canvas.bind("<Configure>", on_configure)

alt_load_btn = tk.Button(root, text="carregar portifolio", command=open_file)
alt_load_btn.place(x=15, y=545)

portfolioedit_btn = tk.Button(root, text="editar portifolio", command=portfoloioedit_window)
portfolioedit_btn.place(x=20, y=515)

root.mainloop()
