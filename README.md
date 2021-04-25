Este proyecto consistió en la comunicación entre servidor y cliente usando el protocolo DNS. Para esto, se utilizó el servidor CoreDNS y el cliente
Dog, los cuales fueron instalados mediante código fuente en un documento Docker. Con las respectivas imágenes creadas y contenedores corriendo, se abre 
el server y con el cliente se establece la comunicación con el servidor. Teniendo esto, se capturan datos con Wireshark y se analizan los paquetes 
generados con la comunicación hecha.


INSTALACIÓN:

Ingrese a la carpeta en donde se encuentre el Dockerfile correspondiente, se procederá a realizar un build para así obtener las imágenes de cada uno de estos Docker:

    sudo docker build -t NAME .

Luego, a cada imagen se le realizará un run para poder crear su respectivo contenedor:

    sudo docker run -it ID_IMAGEN .

Teniendo los contenedores de cada software, se podrán iniciar o detener de la siguiente manera:

    sudo docker container start -i ID_CONTAINER
    sudo docker container stop -i ID_CONTAINER

    
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
