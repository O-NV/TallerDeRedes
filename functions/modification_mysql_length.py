def modification_mysql_length(packet):
    try:
        if packet['IP']['src'] == '172.17.0.3':
            original = packet['MYSQL']['packet_length']
            packet['MYSQL']['packet_length'] = 35
            print('packet length original: ' , original , 'packet length cambiado: ', packet['MYSQL']['packet_length'])
            return packet
    except:
        return None