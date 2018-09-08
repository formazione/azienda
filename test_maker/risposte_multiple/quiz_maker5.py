import os
from random import shuffle

num = 1
allquiz = ""


def makequiz(domanda, r1, r2, r3, r4):
    global num
    global allquiz
    giusta = r1
    lista = [r1, r2, r3, r4]
    shuffle(lista)
    listaval = []
    for n, r in enumerate(lista):
        if r == r1:
            listaval.append(r1)
        else:
            listaval.append("")

    vr1 = listaval[0]
    vr2 = listaval[1]
    vr3 = listaval[2]
    vr4 = listaval[3]

    r1 = lista[0]
    r2 = lista[1]
    r3 = lista[2]
    r4 = lista[3]

    quiz = """<div style="background-color:lightblue">
    <h1>""" + domanda + """<span id='a""" + str(num) + """'>______</span></h1><br>
    <form id=\"d""" + str(num) + """\">
    <input type="radio" name="choice" value=\"""" + vr1 + """\">""" + r1 + """
    <input type="radio" name="choice" value=\"""" + vr2 + """\">""" + r2 + """
    <input type="radio" name="choice" value=\"""" + vr3 + """\">""" + r3 + """
    <input type="radio" name="choice" value=\"""" + vr4 + """\">""" + r4 + """
    <br>
    <input type="submit" value="submit" onclick="validate(choice.value, """ + str(num) + """)">
    </form>
    </div>"""
    num += 1

    quiz += """<script>
var validate = function(valore, number) {
form = "d" + number
span = "a" + number
var formname = document.getElementById(form)
var spanname = document.getElementById(span)


if (valore != "") {
    formname.innerHTML ="<div style='background-color:lightgreen'><h1>Esatto";
    formname.innerHTML += "</h1></div>";
    spanname.innerHTML = valore;
}

else {

    formname.innerHTML = "<div style='background-color:pink'><h1>Sbagliato";
    formname.innerHTML += "</h1></div>";
}
};

</script>"""
    allquiz += quiz
    print(quiz)
    return quiz


def getdata(file_txt):
    "prende i dati da file_txt e crea la domanda con makequiz"
    with open(file_txt, "r", encoding="utf-8") as file:
        numquest = int((len(file.readlines()) - 1) / 5)
        file.seek(0)
        for i in range(numquest):
            domanda = file.readline()
            r1 = file.readline()
            r2 = file.readline()
            r3 = file.readline()
            r4 = file.readline()
            makequiz(domanda, r1, r2, r3, r4)
            file.readline()


def save(file_html):
    "salva il file html"
    global all
    with open(file_html, "w", encoding="utf-8") as file:
        file.write(allquiz)


_file = "test"
file_txt = _file + ".txt"
file_html = _file + ".html"

if os.path.exists(file_txt):
    getdata(file_txt)
    message = ""
else:
    message = "\n=============\nAttenzione:\nIl file di testo con i dati non è stato trovato.\nDevi prima creare il file di testo con la domanda nella prima riga\nle 4 risposte nelle altre 4 righe\n e una riga vuota alla fine\nGrazie dell'attenzione: 25/04/2018 - Festa della repubblica\n\n" + file_txt
    print(message)

save(file_html)

import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Stiamo aprendo il file " + file_html + "nel tuo browser, attendere prego." + message).pack()


os.system(file_html)
