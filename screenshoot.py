# Import Plugin Selenium dll ==========================================
from selenium.webdriver.common.keys import Keys #Di Gunakan untuk Keys.ENTER
from selenium.webdriver.common.by import By #Di Gunakan untuk By.CSS_SELECTOR/XPATH
from selenium import webdriver #Webdriver untuk Chrome
import time
import datetime

# Ini adalah Dictionary dengan satu Key dan banyak Value ====================================
interface = {
        "BCALC1" : ['10.68.68.2','10.68.68.2%2F19','./Capture link IP Sec/BCALC1/2022/','BCALC1'],
        "BCALC1_2" : ['10.68.68.3','10.68.68.3%2F19','./Capture link IP Sec/BCALC1/2022/','BCALC1'],
        "BSD" : ['10.63.140.3','10.63.140.3%2F14','./Capture link IP Sec/BSD/2022/','BSD'],
        "BSD_2" : ['10.63.140.4','10.63.140.4%2F14','./Capture link IP Sec/BSD/2022/','BSD'],
        "CPC" : ['10.64.0.29','10.64.0.29%2F14','./Capture link IP Sec/CPC/2022/','CPC'],
        "CPC_2" : ['10.64.0.30','10.64.0.30%2F14','./Capture link IP Sec/CPC/2022/','CPC'],
        "FOR" : ['10.61.0.1','10.61.0.1%2F14','./Capture link IP Sec/FOR/2022/','FOR'],
        "FOR_2" : ['10.61.0.2','10.61.0.2%2F14','./Capture link IP Sec/FOR/2022/','FOR'],
        "GSW" : ['10.70.4.1','10.70.4.1%2F11','./Capture link IP Sec/GSW/2022/','GSW'],
        "GSW_2" : ['10.70.4.2','10.70.4.2%2F11','./Capture link IP Sec/GSW/2022/','GSW'],
        "HSB" : ['10.66.128.1','10.66.128.1%2F13','./Capture link IP Sec/HSB/2022/','HSB'],
        "HSB_2" : ['10.66.128.2','10.66.128.2%2F13','./Capture link IP Sec/HSB/2022/','HSB'],
        "JDL" : ['10.70.0.1','10.70.0.1%2F11','./Capture link IP Sec/JDL/2022/','JDL'],
        "JLD_2" : ['10.70.0.2','10.70.0.2%2F11','./Capture link IP Sec/JDL/2022/','JDL'],
        "LMP" : ['10.69.0.29','10.69.0.29%2F12','./Capture link IP Sec/LMP/2022/','LMP'],
        "LMP_2" : ['10.69.0.30','10.69.0.30%2F13','./Capture link IP Sec/LMP/2022/','LMP'],
        "TCM" : ['10.70.8.1','10.70.8.1%2F9','./Capture link IP Sec/TCM/2022/','TCM'],
        "TCM_2" : ['10.70.8.2','10.70.8.2%2F9','./Capture link IP Sec/TCM/2022/','TCM'],
        "WBCA" : ['10.60.31.29','10.60.31.29%2F12','./Capture link IP Sec/WBCA-PI/2022/','WBCA'],
        "WBCA_2" : ['10.60.31.30','10.60.31.30%2F12','./Capture link IP Sec/WBCA-PI/2022/','WBCA']  
}

# Input Pilihan Custom -----------------------------
print('============================')
print('1. Screenshoot Harian')
print('2. Screenshoot Custom')
print('============================')
pilihan = input('Masukan Pilihan : ')
if pilihan == "2" :
   device =  str(input('Masukan Device(Ex.FOR/CPC) : '))
   ipsec = str(input('Pilih IPSEC (1-2) : '))

# Input Data Waktu Netflow --------------------------
print('\n==== Masukan Waktu Awal ====')
waktu = str(input("Masukan Tanggal (2022/12/30) : "))
waktu_s = waktu.split('/')

jam = input("Masukan Jam (24.00) : ")
jam_s = jam.split('.')

print('\n==== Masukan Jam Akhir ====')
jam2 = input("Masukan Jam (24.00) : ")
jam2_s = jam2.split('.')

print('\n=== Masukan Tanggal Folder ===')
tgl_folder = str.upper(input('Masukan Tanggal Gambar (Ex 10-OKTOBER) : '))
bulan_folder = tgl_folder.split('-')

epoch_time = datetime.datetime(int(waktu_s[0]),int(waktu_s[1]), int(waktu_s[2]), int(jam_s[0]), int(jam_s[1]), 0).timestamp()*1000
epoch_time2 = datetime.datetime(int(waktu_s[0]),int(waktu_s[1]), int(waktu_s[2]), int(jam2_s[0]), int(jam2_s[1]), 0).timestamp()*1000
#========================================


# Deklarasi webdriver & Tampilan Windows Maksimal ====================
driver = webdriver.Chrome()
driver.maximize_window()    

# Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
driver.get('http://10.38.3.25/login/login.jsp')
driver.find_element('name','j_username').send_keys('ald')
driver.find_element('name','j_password').send_keys('ald' + Keys.ENTER)


# Membuat Function untuk di panggil kembali pada Looping
def loop (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    element.screenshot(lokasi+ str.title(bulan_folder[1]) + '/' + str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC1_traffic.png')
   

def loop2 (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    element.screenshot(lokasi+ str.title(bulan_folder[1]) + '/' + str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC2_traffic.png')   



def loop3 (ip1:(str), ip2:(str), lokasi:(str), nama:(str)):
    web = 'http://10.38.3.25/report.jsp?templid=_if&output=chart&device=' + ip1 + '&if=' + ip2 + '&chartTitle=Traffic+Rate'
    driver.get(web+'&stime='+ str(int(epoch_time)) + '&etime=' + str(int(epoch_time2)) + '&sample_nunits=1&sample_unit=minute')
    driver.set_window_size(782, 768)
    time.sleep(1)
    element = driver.find_element('name','rep_form')
    if ipsec == "2":
        element.screenshot(lokasi+ 'Backup' + '/' + str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC2_traffic.png')
    else:
        element.screenshot(lokasi+ 'Backup' + '/' + str(tgl_folder)+'-2022_'+nama+'-WAN-IPSEC1_traffic.png')
        

if pilihan == "2":
    if ipsec == "2":
        choice = interface[device + "_2"]
    else:
        choice = interface[device]

    loop3(choice[0], choice[1], choice[2], choice[3])
else:
    # Looping (for IP - Location Folder - Name)
    loop('10.68.68.2','10.68.68.2%2F19','./Capture link IP Sec/BCALC1/2022/','BCALC1')
    loop2('10.68.68.3','10.68.68.3%2F19','./Capture link IP Sec/BCALC1/2022/','BCALC1') 
    loop('10.63.140.3','10.63.140.3%2F14','./Capture link IP Sec/BSD/2022/','BSD')
    loop2('10.63.140.4','10.63.140.4%2F14','./Capture link IP Sec/BSD/2022/','BSD')  
    loop('10.64.0.29','10.64.0.29%2F14','./Capture link IP Sec/CPC/2022/','CPC')  
    loop2('10.64.0.30','10.64.0.30%2F14','./Capture link IP Sec/CPC/2022/','CPC')  
    loop('10.61.0.1','10.61.0.1%2F14','./Capture link IP Sec/FOR/2022/','FOR')  
    loop2('10.61.0.2','10.61.0.2%2F14','./Capture link IP Sec/FOR/2022/','FOR')  
    loop('10.70.4.1','10.70.4.1%2F11','./Capture link IP Sec/GSW/2022/','GSW')  
    loop2('10.70.4.2','10.70.4.2%2F11','./Capture link IP Sec/GSW/2022/','GSW')  
    loop('10.66.128.1','10.66.128.1%2F13','./Capture link IP Sec/HSB/2022/','HSB')  
    loop2('10.66.128.2','10.66.128.2%2F13','./Capture link IP Sec/HSB/2022/','HSB')  
    loop('10.70.0.1','10.70.0.1%2F11','./Capture link IP Sec/JDL/2022/','JDL')  
    loop2('10.70.0.2','10.70.0.2%2F11','./Capture link IP Sec/JDL/2022/','JDL')
    loop('10.69.0.29','10.69.0.29%2F12','./Capture link IP Sec/LMP/2022/','LMP')  
    loop2('10.69.0.30','10.69.0.30%2F13','./Capture link IP Sec/LMP/2022/','LMP')    
    loop('10.70.8.1','10.70.8.1%2F9','./Capture link IP Sec/TCM/2022/','TCM')  
    loop2('10.70.8.2','10.70.8.2%2F9','./Capture link IP Sec/TCM/2022/','TCM')  
    loop('10.60.31.29','10.60.31.29%2F12','./Capture link IP Sec/WBCA-PI/2022/','WBCA')
    loop2('10.60.31.30','10.60.31.30%2F12','./Capture link IP Sec/WBCA-PI/2022/','WBCA')

time.sleep(1)
driver.quit()  








# DOCUMENTATION!!!!!
# -------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# driver.find_element('name','q').send_keys('Aldo Hidayat' + Keys.ENTER)
# assert 'Aldo Hidayat','Aldo' in driver.find_element(By.CSS_SELECTOR,'h3').text
# assert 'Aldo Hidayat' in driver.title


# -------------------------------------------------------------------------------------------
# # BCALC1 - IPSEC1
# driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.68.68.2&if=10.68.68.2%2F19&chartTitle=Traffic+Rate'+str(epoch))
# driver.set_window_size(782, 768)
# time.sleep(1)
# element = driver.find_element('name','rep_form')
# element.screenshot('./Capture link IP Sec/BCALC1/2022/'+str(date)+'-2022_BCALC1-WAN-IPSEC1_traffic.png') 