def modification_packet_number(packet):
    try:
        if packet['IP']['src'] == '172.17.0.3' and packet['MYSQL']['packet_length'] > 0:
            original = packet['MYSQL']['packet_number']
            packet['MYSQL']['packet_number'] = 111
            cambio = packet['MYSQL']['packet_number']
            print('numero paquete original: ' , original , 'numero paquete cambiado: ' , cambio)
        return packet
    except:
        return None