# interface.py
# Interface gráfica da Calculadora de Bases usando Tkinter.

import tkinter as tk
from tkinter import ttk, messagebox

from calculos import (
    decimal_para_binario,
    decimal_para_octal,
    decimal_para_hexadecimal,
    binario_para_decimal,
    binario_para_octal,
    binario_para_hexadecimal,
    octal_para_binario,
    octal_para_decimal,
    octal_para_hexadecimal,
    hexadecimal_para_binario,
    hexadecimal_para_decimal,
    hexadecimal_para_octal,
)


# Dicionário que relaciona a base escolhida com a função de conversão.
CONVERSOES = {
    ("Decimal", "Binário"): decimal_para_binario,
    ("Decimal", "Octal"): decimal_para_octal,
    ("Decimal", "Hexadecimal"): decimal_para_hexadecimal,

    ("Binário", "Decimal"): binario_para_decimal,
    ("Binário", "Octal"): binario_para_octal,
    ("Binário", "Hexadecimal"): binario_para_hexadecimal,

    ("Octal", "Binário"): octal_para_binario,
    ("Octal", "Decimal"): octal_para_decimal,
    ("Octal", "Hexadecimal"): octal_para_hexadecimal,

    ("Hexadecimal", "Binário"): hexadecimal_para_binario,
    ("Hexadecimal", "Decimal"): hexadecimal_para_decimal,
    ("Hexadecimal", "Octal"): hexadecimal_para_octal,
}


BASES = ["Decimal", "Binário", "Octal", "Hexadecimal"]


def converter():
    numero = entrada_numero.get().strip()
    origem = combo_origem.get()
    destino = combo_destino.get()

    if not numero:
        messagebox.showwarning("Atenção", "Digite um número para converter.")
        return

    if origem == destino:
        resultado = numero.upper()
        label_resultado.config(text=resultado)
        return

    funcao = CONVERSOES.get((origem, destino))

    if funcao is None:
        messagebox.showerror("Erro", "Conversão não encontrada.")
        return

    try:
        # As conversões decimais precisam receber um inteiro.
        if origem == "Decimal":
            numero_convertido = int(numero)
            resultado = funcao(numero_convertido)
        else:
            resultado = funcao(numero)

        label_resultado.config(text=str(resultado).upper())

    except ValueError:
        messagebox.showerror(
            "Entrada inválida",
            f"O valor informado não é um número válido em {origem}."
        )


def limpar():
    entrada_numero.delete(0, tk.END)
    combo_origem.set("Decimal")
    combo_destino.set("Binário")
    label_resultado.config(text="—")
    entrada_numero.focus()


# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Bases")
janela.geometry("560x520")
janela.resizable(False, False)


# Título
titulo = tk.Label(
    janela,
    text="CALCULADORA DE BASES",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=(25, 5))


subtitulo = tk.Label(
    janela,
    text="Conversão entre Decimal, Binário, Octal e Hexadecimal",
    font=("Arial", 10)
)
subtitulo.pack(pady=(0, 25))


# Área principal
frame = tk.Frame(janela)
frame.pack(padx=40, fill="x")


# Número
label_numero = tk.Label(
    frame,
    text="Número:",
    font=("Arial", 12, "bold")
)
label_numero.pack(anchor="w")

entrada_numero = tk.Entry(
    frame,
    font=("Arial", 16),
    justify="center"
)
entrada_numero.pack(fill="x", pady=(5, 20), ipady=7)


# Base de origem
label_origem = tk.Label(
    frame,
    text="Converter de:",
    font=("Arial", 12, "bold")
)
label_origem.pack(anchor="w")

combo_origem = ttk.Combobox(
    frame,
    values=BASES,
    state="readonly",
    font=("Arial", 12)
)
combo_origem.set("Decimal")
combo_origem.pack(fill="x", pady=(5, 15), ipady=5)


# Base de destino
label_destino = tk.Label(
    frame,
    text="Converter para:",
    font=("Arial", 12, "bold")
)
label_destino.pack(anchor="w")

combo_destino = ttk.Combobox(
    frame,
    values=BASES,
    state="readonly",
    font=("Arial", 12)
)
combo_destino.set("Binário")
combo_destino.pack(fill="x", pady=(5, 25), ipady=5)


# Botões
frame_botoes = tk.Frame(frame)
frame_botoes.pack(fill="x")

botao_converter = tk.Button(
    frame_botoes,
    text="CONVERTER",
    command=converter,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)
botao_converter.pack(side="left", expand=True, fill="x", padx=(0, 5))


botao_limpar = tk.Button(
    frame_botoes,
    text="LIMPAR",
    command=limpar,
    font=("Arial", 12),
    padx=20,
    pady=10
)
botao_limpar.pack(side="right", expand=True, fill="x", padx=(5, 0))


# Resultado
label_resultado_titulo = tk.Label(
    janela,
    text="RESULTADO",
    font=("Arial", 12, "bold")
)
label_resultado_titulo.pack(pady=(35, 8))


label_resultado = tk.Label(
    janela,
    text="—",
    font=("Arial", 24, "bold"),
    relief="solid",
    bd=1,
    width=25,
    pady=12
)
label_resultado.pack()


# Enter também executa a conversão
entrada_numero.bind("<Return>", lambda event: converter())

entrada_numero.focus()

janela.mainloop()
