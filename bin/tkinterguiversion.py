import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from time import time
import os

from CL_portfolio_libs.CL_portfolio_management import Portfolio
from datetime import datetime
from tkcalendar import DateEntry
import webbrowser
from tkinter import filedialog

import CL_portfolio_libs.CL_finance as fnc
import CL_portfolio_libs.CL_plotter as ptt

brazilian_stocks = ['PETR4', 'VALE3', 'ITUB4', 'BBDC4', 'ABEV3',
                    'WEGE3', 'BBAS3', 'MGLU3', 'SUZB3', 'ALPA4', 'ALUP11',
                    'ALUP3', 'ALUP4', 'ANIM3', 'ARZZ3', 'ATMP3', 'ATOM3',
                    'AZEV3', 'BIDI11', 'BIDI3', 'BIDI4', 'BOBR3', 'BOBR4',
                    'BOVA11', 'BPAC3', 'BPAN4', 'BRAP4', 'BEEF3', 'BPAC11',
                    'BRAP3', 'BRKM3', 'CCRO3', 'CGRA3']

brazilian_stocks = list(set(brazilian_stocks))
brazilian_stocks.sort()

for i in brazilian_stocks:
    brazilian_stocks[brazilian_stocks.index(i)] = [i, 10]
brazilian_stocks_dict = {}
for i in brazilian_stocks:
    brazilian_stocks_dict[i[0]] = i[1]

usr_portfolio = Portfolio(brazilian_stocks, "Meu portifolio")

scrollslabelslist = []
editstocklabelslist = []
varnotfill = "???"
entry_dict = {}


def argumentedfunction():
    no_web_err(root=root)


def lastsimulation_show():
    info = usr_portfolio.last_simulation
    info = info.to_dict()
    risklabel_list = ['p10', 'p25', 'p50', 'p75', 'p90']
    final_plotlist_x = [i for i in range(30)]
    final_plotlist_y = []
    for i in risklabel_list:
        temp_list = []
        for k in info['data'][i]:
            temp_list.append(info['data'][i][k])
        final_plotlist_y.append(temp_list)
    figure = ptt.SimulationFig(final_plotlist_x, final_plotlist_y)
    figure.set_labels(risklabel_list)
    pathtoimage = os.sep.join([os.getcwd(), 'CL_GUI', 'gcache', f"simulacao{int((info['time_ended']))}.png"])
    figure.fig_cache(pathtoimage, True)
    resultwin = tk.Tk()
    resultwin.geometry('600x450')

    stock_graphimg2 = Image.open(pathtoimage)

    stock_graphimg2.thumbnail((400, 225))
    photo2 = ImageTk.PhotoImage(stock_graphimg2, master=resultwin)

    # Crie um widget Label para exibir a imagem
    stock_graph_label2 = tk.Label(resultwin, image=photo2)
    stock_graph_label2.image = photo2
    stock_graph_label2.place(x=100, y=100)


def riskcalc_window():
    j = tk.Tk()
    style = ttk.Style(j)
    style.theme_use('clam')
    global photo2

    def riskrun_btn():
        usr_portfolio.run_simulation(risk_var.get())
        lastsimulation_show()

        j.destroy()

        #  chamar a risco aqui(ano)
        # pegar o resultado e pllottar

    j.geometry("300x200")
    j.title("Calcular risco")
    style = ttk.Style(j)
    style.theme_use('clam')
    riskcalc_label = tk.Label(j, text="Selecione o periodo do risco:")
    riskcalc_label.place(x=50, y=20)
    risk_var = tk.StringVar(j)
    r1 = tk.Radiobutton(j, text="Dia", variable=risk_var, value='1d')
    r1.place(x=50, y=50)

    r2 = tk.Radiobutton(j, text="Mes", variable=risk_var, value='1mo')

    r2.place(x=50, y=80)
    r3 = tk.Radiobutton(j, text="Ano", variable=risk_var, value='1y')

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
    style = ttk.Style(root)
    style.theme_use('clam')
    tk.Label(root, text="Sem acesso a internet \n Reinicie o aplicativo ou tente mais tarde").place(relx=0.2, rely=0.5)
    tk.Button(root, text="OK", command=root.destroy).place(relx=0.45, rely=0.7)


def mainscrollhset():
    canvas.update_idletasks()  # Atualize o canvas
    canvas_height = content_frame.winfo_reqheight()  # Altura total do conteúdo
    canvas.config(scrollregion=(0, 0, 0, canvas_height))  # Atualize a região de rolagem do canvas

    # Verifique se a altura total do conteúdo é maior que a altura visível
    if canvas_height > canvas.winfo_height():
        scrollbar.configure(command=canvas.yview)
        canvas.bind("<MouseWheel>", on_mouse_wheel)
    else:

        scrollbar.configure(command=None)
        canvas.unbind("<MouseWheel>")
        for label in scrollslabelslist:
            label.unbind("<MouseWheel>")


def change_fronthistory(iniday, finday):
    # unstable please read again
    sym = stockname_label.cget("text")
    sym = sym.replace(' ', '')

    dt = time()
    if True:
        arr = fnc.history([sym], iniday, finday, '1d')
        arr = arr[sym]
    figure = ptt.PortfolioFig(arr.index, arr['Open'])
    figure.set_bgcollor('black')

    figure.fig_cache(os.sep.join([os.getcwd(), 'CL_GUI', 'gcache', f'{sym}.png']))

    stock_graphimg = Image.open(os.sep.join([os.getcwd(), 'CL_GUI', 'gcache', f'{sym}.png']))
    stock_graphimg.resize((800, 450))
    stock_graphimg.thumbnail((400, 225))
    photo = ImageTk.PhotoImage(stock_graphimg)

    # Crie um widget Label para exibir a imagem
    stock_graph_label = tk.Label(root, image=photo)
    stock_graph_label.image = photo  # Mantém uma referência à imagem para evitar que ela seja coletada pelo coletor de lixo

    iniprice = arr["Open"][0]
    finalprice = arr["Open"][-1]
    if iniprice > finalprice:
        value_c = 'red'
        strdir = ''
    else:
        value_c = 'green'
        strdir = '+'
    stockvalue_label.config(
        text=f"{strdir}{round(100 * (finalprice - iniprice) / (iniprice), 3)}% R$:{round(finalprice, 2)}", fg=value_c)


def portfoloioedit_window():
    def adicionar_elemento():
        elemento = entry.get()
        selecionado = tk.BooleanVar()
        lista.append({"nome": elemento, "selecionado": selecionado})
        update_lista()

    def save_changes():
        usr_portfolio.portfolio.clear()
        usr_portfolio.name = name_entry.get()

        for elemento in lista:
            nome = elemento["nome"]
            selecionado = elemento["selecionado"].get()
            entrada = entry_dict.get(nome, None)

            if selecionado and entrada:
                valor_entrada = entrada.get()
                usr_portfolio.portfolio[nome] = valor_entrada

        # tudo ok
        for widget in content_frame.winfo_children():
            widget.destroy()
        global scrollslabelslist
        scrollslabelslist = []
        for i in usr_portfolio.portfolio:
            label = tk.Label(content_frame, text=f" {i}")
            label.bind("<Button-1>", lambda event, label=label: change_label_color(event, label))
            label.bind("<MouseWheel>", on_mouse_wheel)
            label.pack()
            scrollslabelslist.append(label)
        mainscrollhset()
        root.destroy()

    def on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_frame_configure(event):
        canvas.itemconfig(canvas_frame, width=canvas.winfo_width())

    def update_lista():

        global entry_dict
        for i in lista_frame.winfo_children():
            i.destroy()

        for idx, elemento in enumerate(lista):
            frame = tk.Frame(lista_frame)
            frame.pack(fill="x")

            label = tk.Label(frame, text=elemento["nome"])
            label.pack(side="left")

            entry = tk.Entry(frame)
            entry.pack(side="left")

            checkbox = tk.Checkbutton(frame, variable=elemento["selecionado"])
            checkbox.place(relx=0.7)
            checkbox.bind("<Button-1>", lambda event, index=idx: update_checkbox_state(index))

            # Verifique se a chave existe no dicionário usr_portfolio.portfolio
            if elemento["nome"] in usr_portfolio.portfolio:
                entry.insert(0, usr_portfolio.portfolio[elemento["nome"]])

            entry_dict[elemento["nome"]] = entry

        # Atualize o scrollregion do canvas para incluir todo o conteúdo
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def update_checkbox_state(index):
        lista[index]["selecionado"].set(not lista[index]["selecionado"].get())

    lista = []

    root = tk.Tk()
    root.title("Criar portifolio")
    root.geometry("400x500")
    style = ttk.Style(root)
    style.theme_use('clam')

    name_entry = tk.Entry(root)
    name_entry.insert(0, "Meu portifolio")
    name_entry.pack(side="top", padx=100)

    entry = tk.Entry(root)
    entry.pack(side="top", pady=10, padx=100)

    name_label = tk.Label(root, text="Nome do portfolio")

    name_label.place(relx=0, rely=0)
    stockname_lbl = tk.Label(root, text="Codigo da empresa")
    stockname_lbl.place(relx=0, rely=0.05)

    adicionar_button = tk.Button(root, text="Adicionar", command=adicionar_elemento)
    adicionar_button.pack(side="top")

    remover_button = tk.Button(root, text="Salvar alterações", command=save_changes)
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
    save_file()

    root.mainloop()


def update_scrollbar_elements(selected_items):
    pass


def creditwindow():
    j = tk.Tk()
    j.geometry("300x300")
    j.title("creditos")
    style = ttk.Style(j)
    style.theme_use('clam')

    credits_text = tk.Label(j,
                            text="Creditos: \n                          Graficos:Henrique Assis \n                             Plotagem:Henrique Assis \n                     Arquivos:Emilio Vital \n                                  API financeira:Leticia Aleixo \n                           Risco:Gabriella Morgado")
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

    file_name = tk.filedialog.askopenfilename(filetypes=[('Portifolio', '*.jprt')],
                                              initialdir='..' + os.sep + '_data_port')
    if file_name != "" and file_name != ():
        file_name = file_name.replace("/", os.sep)
        file_name = file_name.replace("\\", os.sep)
        usr_portfolio = Portfolio.load(file_name)
    for widget in content_frame.winfo_children():
        widget.destroy()
    global scrollslabelslist
    scrollslabelslist = []
    for i in usr_portfolio.portfolio:
        label = tk.Label(content_frame, text=f" {i}")
        label.bind("<Button-1>", lambda event, label=label: change_label_color(event, label))
        label.bind("<MouseWheel>", on_mouse_wheel)
        label.pack()
        scrollslabelslist.append(label)
    mainscrollhset()


def period_selector():
    j = tk.Tk()
    j.geometry("270x380")
    j.title("selecionar periodo")
    style = ttk.Style(j)
    style.theme_use('clam')

    style = ttk.Style(j)
    style.theme_use('clam')

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
        change_fronthistory(f"{inicaldatalist[2]}-{inicaldatalist[1]}-{inicaldatalist[0]}",
                            f"{endcaldatalist[2]}-{endcaldatalist[1]}-{endcaldatalist[0]}")

    period_fselbt = tk.Button(j, text="Selecionar", command=periodselctorbtn_command)
    period_fselbt.place(x=110, y=320)

    j.mainloop()


def save_file():
    # Lógica para salvar um arquivo

    file_name = '..' + os.sep + '_data_port'
    if file_name != "" and file_name != ():
        file_name = file_name.replace("/", os.sep)
        file_name = file_name.replace("\\", os.sep)
        usr_portfolio.save(file_name)


def change_label_color(event, label):
    for i in scrollslabelslist:
        i.config(bg="lightgray")
    label.config(bg="blue")
    stockname_label.config(text=label.cget("text"))
    stockarea_title.config(text=f'Analise da empresa {label.cget("text")}')
    stocknametext = stockname_label.cget("text").replace(" ", "")
    stocknumber_label.configure(text=f'Você possui {usr_portfolio[stocknametext]} ações nessa empresa')

    data_string = "2023-11-17 15:30:00"
    dt = time()
    # Converter a string em um objeto datetime
    data_hora_objeto = datetime.strptime(data_string, "%Y-%m-%d %H:%M:%S")

    dia = data_hora_objeto.day
    mes = data_hora_objeto.month
    ano = data_hora_objeto.year
    if dia < 6:
        dia_atual = 28
        if mes == 1:
            mes_atual = 12
            ano_atual = ano - 1
        else:
            mes_atual = mes - 1
            ano_atual = ano
    else:
        dia_atual = dia - 5
        ano_atual = ano
        mes_atual = mes
    if dia_atual == 29:
        dia_atual -= 1

    change_fronthistory(f'{ano_atual - 1}-{mes_atual}-{dia_atual}', f'{ano_atual}-{mes_atual}-{dia_atual}')

    upareaperiod_label.config(
        text=f"periodo analisado:\nde: {dia_atual}/{mes_atual}/{ano_atual - 1} \nate: {dia_atual}/{mes_atual}/{ano_atual}")


def cut_text():
    # Lógica para recortar texto
    pass


def copy_text():
    # Lógica para copiar texto
    pass


def paste_text():
    # Lógica para colar texto
    pass



root = tk.Tk()
root.geometry("800x600")
root.title("analise de portifolio")
# style = ttk.Style(root)
# style.theme_use('clam')

style = ttk.Style(root)
style.theme_use('clam')

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
for i in usr_portfolio.portfolio:
    label = tk.Label(content_frame, text=f" {i}")
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
stockvalue_label.place(x=520, y=70)

stocknumber_label = tk.Label(root, text=f"voce possui: {varnotfill} ações nesse empresa")
stocknumber_label.place(x=300, y=330)

upareaperiod_label = tk.Label(root,
                              text=f"periodo analisado:\nde: {varnotfill}/{varnotfill}/{varnotfill} \nate: {varnotfill}/{varnotfill}/{varnotfill}")
upareaperiod_label.place(x=650, y=200)

upperiodbtn = tk.Button(root, text="selecionar periodo", command=period_selector)
upperiodbtn.place(x=650, y=250)

stock_graphimg = Image.open(os.sep.join([os.getcwd(), "CL_GUI", "gcache", "u2clm4ND_mid.png"]))
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

lastsimbutton = tk.Button(root, text="Ultima simulação", command=lastsimulation_show)
lastsimbutton.place(x=350, y=540)
riskbutton = tk.Button(root, text="calcular risco", command=riskcalc_window)
riskbutton.place(x=500, y=540)

canvas.bind("<Configure>", on_configure)

alt_load_btn = tk.Button(root, text="carregar portifolio", command=open_file)
alt_load_btn.place(x=5, y=545)

portfolioedit_btn = tk.Button(root, text="criar portifolio", command=portfoloioedit_window)
portfolioedit_btn.place(x=10, y=515)

root.mainloop()
