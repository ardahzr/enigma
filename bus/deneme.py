import zeep
import json
import xml.etree.ElementTree as ET

url = "https://api.ibb.gov.tr/iett/FiloDurum/SeferGerceklesme.asmx?wsdl"
client = zeep.Client(wsdl=url)
result = client.service.GetHatOtoKonum_json(HatKodu="19S")
result = json.loads(result)
buses = []
for bus in result:
    if bus["yon"] == "YENİDOĞAN PERONLAR":
        otobus = [bus["kapino"],float(bus["enlem"]),float(bus["boylam"])]
        buses.append(otobus)
print(buses)

url = "https://api.ibb.gov.tr/iett/ibb/ibb.asmx?wsdl"
client = zeep.Client(wsdl=url)
result = client.service.DurakDetay_GYY(hat_kodu="4")


stops = []
for table in result.findall("Table"):
    yon = table.find("YON").text
    if yon == "G":
        durak_adi = table.find("DURAKADI").text
        xkoordinat = float(table.find("XKOORDINATI").text)
        ykoordinat = float(table.find("YKOORDINATI").text)
        listem = [durak_adi,ykoordinat,xkoordinat]
        stops.append(listem)
print(stops)

with open("where.js", "w", encoding="utf-8") as file:
    file.write("stops = [")
    for stop in stops:
        file.write(f"['{stop[0]}', {stop[1]}, {stop[2]}], ")
    file.write("]\nbuses = [")
    for bus in buses:
        file.write(f"['{bus[0]}', {bus[1]}, {bus[2]}], ")
    file.write("]")
    