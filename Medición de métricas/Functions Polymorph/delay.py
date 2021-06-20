def delay(packet):
    import time
    if packet['IP']['src'] == '172.17.0.2':
        if packet['MYSQL']['packet_length'] == 1:
            try:
                delay = time.time() - packet.time
            	 packet.global_var('time',time.time())
            	 print("El delay es: ",round(delay,3))
            	 return packet
        	  except:
            	 packet.global_var('time', time.time())
            	 return packet