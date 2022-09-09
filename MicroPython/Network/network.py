def internet(ssid, pasw): 					#fungsi internet
    import network							#include library network
    wlan = network.WLAN(network.STA_IF)		#membuat starus jaringan
    wlan.active(True)						#mengaktifkan WiFi
    if not wlan.isconnected():				# logika menghubungkan jaringan
        print("connect to wlan ...")		
        wlan.connect(ssid, pasw)
        while not wlan.isconnected():
            pass
        
    print('wlan config', wlan.ifconfig())	#menampilkan status jaringan
    

user = "your ssid"							#masukan ssid dan password
pasword = "your password"
internet(user, pasword)