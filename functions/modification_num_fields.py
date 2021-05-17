def modification_num_fields(packet):
    try:
        if packet['IP']['src'] == '172.17.0.2':
            if packet['MYSQL']['packet_length'] > 0:
                packet['MYSQL']['num_fields'] = 4
                return packet
    except:
        return None