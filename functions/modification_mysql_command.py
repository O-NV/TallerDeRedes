def modification_mysql_command(packet):
    try:
        if packet['IP']['src'] == '172.17.0.3':
            if packet['MYSQL']['packet_length'] > 0:
                original = packet['MYSQL']['command']
                packet['MYSQL']['command'] = 2
                print('command original: ', original , 'command cambiado: ' , packet['MYSQL']['command'])
                return packet
    except:
        return None