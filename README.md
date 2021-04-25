Este proyecto consistió en la comunicación entre servidor y cliente usando el protocolo DNS. Para esto, se utilizó el servidor CoreDNS y el cliente
Dog, los cuales fueron instalados mediante código fuente en un documento Docker. Con las respectivas imágenes creadas y contenedores corriendo, se abre 
el server y con el cliente se establece la comunicación con el servidor. Teniendo esto, se capturan datos con Wireshark y se analizan los paquetes 
generados con la comunicación hecha.

COMANDOS:

- Server:

    ./coredns \
        Inicia el servidor en el puerto predeterminado (53)

    ./coredns -dns.port=PORT \
        Inicia el servidor en un puerto específico

- Cliente:

    dog -q example.net -t MX -n 1.1.1.1 \
        -q => Host name o domain name \
        -t => DNS record type \
        -n => Address del nameserver
