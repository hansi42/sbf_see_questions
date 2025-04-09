import requests, re
URL = "https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Fragenkatalog-See/Basisfragen/Basisfragen-node.html"
URL2 ="https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Fragenkatalog-See/Spezifische-Fragen-See/Spezifische-Fragen-See-node.html"
URL3="https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Fragenkatalog-See/Navigationsaufgaben/Navigationsaufgaben-node.html"
#REGEX="<p>\n(\d+)\.(.+?)<li>(.+?)<br/>.*?<li>(.+?)<br/>.*?<li>(.+?)<br/>.*?<li>(.+?)<br/>.*?\n(?=<p class=\"line\"></p>)"
REGEX="<p>\n(\d+)\.(.+?)<li>(.+?)<br/>.*?<li>(.+?)<br/>.*?<li>(.+?)<br/>.*?<li>(.+?)<.*?\n(?=<p class=\"line\"></p>)"
REGEX_links="<img src=\"(.+?)\""
REGEX_question="^(.*?)<"
page = requests.get(URL2)
matches = re.findall(REGEX, page.text, re.DOTALL)

filename="/tmp/test.txt"
#f = open(filename,"w")
#f.write("number; q; a1; a2; a3; a4; links[;..]\n")
#f.close()
f = open(filename, "a")

for i in matches:

    question = re.findall(REGEX_question, i[1])

    link_csv =""
    if(re.search(REGEX_links, i[1])):
        links = (re.findall(REGEX_links, i[1]))
        for l in links:
            link_csv += ",\"" + l + "\""
        print(link_csv)
    f.write(f"{i[0]},\"{''.join(question)}\",\"{i[2]}\",\"{i[3]}\",\"{i[4]}\",\"{i[5]}\"{link_csv}\n") 

f.close()
