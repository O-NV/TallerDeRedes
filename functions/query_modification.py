def query_modification(packet):
    try:
        if packet['IP']['src'] == '172.17.0.3':
            if packet['MYSQL']['packet_length'] > 0:
                newquery = 'show tables'
                difference = len(newquery) - len(packet['MYSQL']['query'])
                packet['MYSQL']['packet_length'] = packet['MYSQL']['packet_length'] + difference
                packet['IP']['len'] = packet['IP']['len'] + difference
                packet['MYSQL']['query'] = newquery
            return packet
    except:
        return None