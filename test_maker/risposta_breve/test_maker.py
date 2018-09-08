start = """[hoops name="input_text"]
<script>\n"""
content = ""
with open("dati.txt", "r", encoding="utf-8") as file:
    for line in file:
        content += "input(\"" + line.split("/")[0] + "\", \"" + line.split("/")[1].strip() + "\");\n"
        file.readline()

end = """</script>"""

print(start + content + end)

with open("copy_in_wp.html", "w", encoding="utf-8") as file:
    file.write(start + content + end)
