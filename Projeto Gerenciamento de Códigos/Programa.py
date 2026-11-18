import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import pdfplumber
import re
import sqlite3
import os
import shutil
from collections import Counter

# ===== CONFIG =====
DB = "codigos.db"
BACKUP = "codigos_backup.db"

COR_FUNDO = "#1e1e1e"
COR_CARD = "#2c2c2c"
COR_TEXTO = "#ffffff"
COR_DESTAQUE = "#4CAF50"

# ===== EXTRAÇÃO =====
def extrair_codigos(pdf_path):

    texto = ""

    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""

    texto = texto.replace("\n", " ")

    # ===== REGEX FLEXÍVEL =====
    padrao = r"""
    (?:c[oó]d(?:igo)?\.?)
    \s*
    (\d{3})
    """

    encontrados = re.findall(
        padrao,
        texto,
        re.IGNORECASE | re.VERBOSE
    )

    return sorted(encontrados)

# ===== BANCO =====
def carregar_antigos():

    if not os.path.exists(DB):
        return []

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS codigos (
            codigo TEXT
        )
    """)

    cur.execute("SELECT codigo FROM codigos")

    dados = [x[0] for x in cur.fetchall()]

    conn.close()

    return dados

def salvar_codigos(codigos):

    if os.path.exists(DB):
        shutil.copy(DB, BACKUP)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS codigos")

    cur.execute("""
        CREATE TABLE codigos (
            codigo TEXT
        )
    """)

    cur.executemany(
        "INSERT INTO codigos VALUES (?)",
        [(c,) for c in codigos]
    )

    conn.commit()
    conn.close()

# ===== INTERFACE =====
def criar_card(titulo, valor):

    frame = tk.Frame(
        frame_resultados,
        bg=COR_CARD,
        padx=15,
        pady=10
    )

    frame.pack(fill="x", pady=6)

    tk.Label(
        frame,
        text=titulo,
        fg="#bbbbbb",
        bg=COR_CARD,
        anchor="w"
    ).pack(fill="x")

    tk.Label(
        frame,
        text=str(valor),
        fg=COR_TEXTO,
        bg=COR_CARD,
        font=("Arial", 13, "bold"),
        anchor="w",
        justify="left",
        wraplength=600
    ).pack(fill="x")

# ===== ANÁLISE =====
def analisar(pdf_path):

    global novos_codigos

    if not pdf_path.lower().endswith(".pdf"):

        messagebox.showerror(
            "Erro",
            "Arquivo não é PDF."
        )

        return

    novos_codigos = extrair_codigos(pdf_path)

    antigos = carregar_antigos()

    if not novos_codigos:

        messagebox.showerror(
            "Erro",
            "Nenhum código encontrado."
        )

        return

    contador = Counter(novos_codigos)

    repetidos = {
        c: count
        for c, count in contador.items()
        if count > 1
    }

    removidos = sorted(
        set(antigos) - set(novos_codigos)
    )

    maior = max(novos_codigos)

    # ===== DISPONÍVEIS =====
    todos = set(
        str(i).zfill(3)
        for i in range(1, 1000)
    )

    usados = set(novos_codigos)

    disponiveis = sorted(todos - usados)

    # ===== PRÓXIMO CÓDIGO =====
    if disponiveis:

        proximo = disponiveis[0]

    else:

        if int(maior) >= 999:
            proximo = "001"

        else:
            proximo = str(
                int(maior) + 1
            ).zfill(3)

    # ===== LIMPA RESULTADOS =====
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # ===== RESULTADOS =====
    criar_card(
        "Total de códigos",
        len(novos_codigos)
    )

    criar_card(
        "Maior código",
        maior
    )

    criar_card(
        "Próximo código sugerido",
        proximo
    )

    # ===== REPETIDOS =====
    texto_repetidos = (
        "\n".join(
            [
                f"{k} → {v}x"
                for k, v in repetidos.items()
            ]
        )
        if repetidos
        else "Nenhum"
    )

    criar_card(
        "Códigos repetidos",
        texto_repetidos
    )

    # ===== REUTILIZÁVEIS =====
    if removidos:

        texto_removidos = str(removidos)

    else:

        texto_removidos = "Nenhum"

    criar_card(
        "Códigos reutilizáveis",
        texto_removidos
    )

    # ===== DISPONÍVEIS =====
    if disponiveis:

        texto_disponiveis = str(disponiveis)

    else:

        texto_disponiveis = "Nenhum"

    criar_card(
        "Códigos disponíveis",
        texto_disponiveis
    )

# ===== SALVAR =====
def salvar():

    if not novos_codigos:

        messagebox.showwarning(
            "Aviso",
            "Nenhum dado para salvar."
        )

        return

    salvar_codigos(novos_codigos)

    messagebox.showinfo(
        "Sucesso",
        "Dados salvos com sucesso!"
    )

# ===== DRAG PDF =====
def drop(event):

    arquivo = event.data.strip("{}")

    analisar(arquivo)

# ===== SCROLL =====
def on_mousewheel(event):

    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

# ===== JANELA =====
janela = TkinterDnD.Tk()

janela.title("Analisador de Códigos")

janela.geometry("700x700")

janela.configure(bg=COR_FUNDO)

# ===== CANVAS =====
canvas = tk.Canvas(
    janela,
    bg=COR_FUNDO,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    janela,
    orient="vertical",
    command=canvas.yview
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.bind_all(
    "<MouseWheel>",
    on_mousewheel
)

# ===== FRAME PRINCIPAL =====
frame_principal = tk.Frame(
    canvas,
    bg=COR_FUNDO
)

janela_id = canvas.create_window(
    (0, 0),
    window=frame_principal,
    anchor="n"
)

def atualizar_scroll(event):

    canvas.configure(
        scrollregion=canvas.bbox("all")
    )

frame_principal.bind(
    "<Configure>",
    atualizar_scroll
)

# ===== CENTRALIZAÇÃO =====
def centralizar_conteudo(event):

    largura_canvas = event.width

    largura_max = 700

    nova_largura = min(
        largura_canvas,
        largura_max
    )

    canvas.itemconfig(
        janela_id,
        width=nova_largura
    )

canvas.bind(
    "<Configure>",
    centralizar_conteudo
)

# ===== CONTAINER =====
container = tk.Frame(
    frame_principal,
    bg=COR_FUNDO
)

container.pack(
    fill="both",
    expand=True,
    padx=20
)

# ===== TÍTULO =====
titulo = tk.Label(
    container,
    text="📄 Analisador de Códigos",
    font=("Arial", 20, "bold"),
    fg=COR_TEXTO,
    bg=COR_FUNDO
)

titulo.pack(pady=20)

# ===== ÁREA PDF =====
area_drop = tk.Label(
    container,
    text="📂 Arraste o PDF aqui",
    bg=COR_CARD,
    fg=COR_TEXTO,
    height=5,
    font=("Arial", 12)
)

area_drop.pack(
    fill="x",
    pady=10
)

area_drop.drop_target_register(DND_FILES)

area_drop.dnd_bind(
    "<<Drop>>",
    drop
)

# ===== RESULTADOS =====
frame_resultados = tk.Frame(
    container,
    bg=COR_FUNDO
)

frame_resultados.pack(
    fill="both",
    expand=True,
    pady=10
)

# ===== BOTÃO =====
btn_salvar = tk.Button(
    container,
    text="💾 Salvar dados",
    command=salvar,
    bg=COR_DESTAQUE,
    fg="white",
    relief="flat",
    height=2,
    font=("Arial", 12, "bold")
)

btn_salvar.pack(
    fill="x",
    pady=20
)

# ===== VARIÁVEL =====
novos_codigos = []

# ===== INICIAR =====
janela.mainloop()