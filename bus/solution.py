############ Do not change the assignment code value ############
assignment_code = 140110201
name = "arda"
surname = "hazar"
student_id = "221401053"
### Do not change the variable names above, just fill them in ###

import zeep
import json
import xml.etree.ElementTree as ET

def announcements(line_code):
    url = "https://api.ibb.gov.tr/iett/UlasimDinamikVeri/Duyurular.asmx?wsdl"
    client = zeep.Client(wsdl=url)
    result = client.service.GetDuyurular_json()
    result = json.loads(result)
    messages = []
    num_announcements = 0
    for hat_info in result:
        if hat_info["HATKODU"] == line_code:
            num_announcements += 1
            messages.append(hat_info["MESAJ"])
            return num_announcements, messages

def stopping_buses():
    url = "https://api.ibb.gov.tr/iett/FiloDurum/SeferGerceklesme.asmx?wsdl"
    client = zeep.Client(wsdl=url)
    result = client.service.GetFiloAracKonum_json()
    result = json.loads(result)
    stopping_buses = [bus["KapiNo"] for bus in result if bus["Hiz"] == "0"]
    return stopping_buses
    
def max_speeds():
    url = "https://api.ibb.gov.tr/iett/FiloDurum/SeferGerceklesme.asmx?wsdl"
    client = zeep.Client(wsdl=url)
    result = client.service.GetFiloAracKonum_json()
    result = json.loads(result)
    for bus in result:
        bus["Hiz"] = float(bus["Hiz"])
    top_buses = sorted(result, key=lambda bus: bus["Hiz"], reverse=True)[:3]
    return top_buses

def show_line_stops(line_code, direction):
    url = "https://api.ibb.gov.tr/iett/ibb/ibb.asmx?wsdl"
    client = zeep.Client(wsdl=url)
    result = client.service.DurakDetay_GYY(hat_kodu=line_code)
    duraklar = []
    for table in result.findall("Table"):
        yon = table.find("YON").text
        if yon == direction:
            durak_adi = table.find("DURAKADI").text
            duraklar.append(durak_adi)
    return duraklar        


    
def live_tracking(line_code, direction):
    pass




#print(announcements("16D"))
#print(stopping_buses())
#print(show_line_stops("4","G"))
#print(max_speeds())
