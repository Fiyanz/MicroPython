def internet(ssid, pasw): 					
    import network							
    wlan = network.WLAN(network.STA_IF)		#membuat starus jaringan
    wlan.active(True)						
    if not wlan.isconnected():				
        print("connect to wlan ...")		
        wlan.connect(ssid, pasw)
        while not wlan.isconnected():
            pass
        
    print('wlan config', wlan.ifconfig())	#menampilkan status jaringan
    

user = "your ssid"							#masukan ssid dan password
pasword = "your password"
internet(user, pasword)