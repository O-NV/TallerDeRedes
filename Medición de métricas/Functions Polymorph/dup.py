def dup(packet):
    try:
        if packet['IP']['len'] == 64:
            print("DUP")
    except:
        return packet
