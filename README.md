> **Entrega 1:**

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

Server:

    ./coredns 

Inicia el servidor en el puerto predeterminado (53)

    ./coredns -dns.port=PORT 

Inicia el servidor en un puerto específico

Cliente:

    dog -q example.net -t MX -n 1.1.1.1 
        
-q => Host name o domain name \
-t => DNS record type \
-n => Address del nameserver




GitHub cliente: https://github.com/ogham/dog
GitHub servidor: https://github.com/coredns/coredns

Video explicativo (hacer click en la imagen):
[![Video explicativo](https://1.bp.blogspot.com/-lX1jN6MwtW0/XSv46aF3KeI/AAAAAAAAD2I/uod3M0T0SeEvFMHq03BLtNGpsRexD1JewCLcBGAs/s1600/Want2host.jpg)](https://youtu.be/VIXUY6DNDv4)

Video explicativo 2.0:

https://youtu.be/Ty-BlkJTvc0



> **Entrega 2:**

Por motivos fuerza mayor, desde la segunda entrega se utilizará el protocolo a MYSQL, donde el servidor será MariaDB y el cliente será Mycli.
Como la creacion del Docker era parte de la entrega anterior, para este protocolo se utilizarán Dockerfile de "DockerHub"

**Instalacion docker Servidor MYSQL**
    
    docker pull mariadb

**Instalacion docker Cliente MYSQL**
    
    docker pull chaifeng/mycli

**Arranque del Servidor y Cliente**

Server:
Para arrancar el servidor, debemos ingresar los siguientes comandos:
    
    docker images
    docker run -e MYSQL_ROOT_PASSWORD=password -d mariadb
    docker ps
Con el ultimo comando, aparecerá en pantalla una tabla con los items "CONTAINER ID", "IMAGE" ETC. Copie le nombre que sale en la tabla e ingrese:

    docker exec -it "NOMBRE" mysql -u root -p


Client:
Para arrancar el cliente se debe ingresar:

    docker run -it -e MYSQL_HOST=172.17.0.3 e72124d6d0

La segunda parte del proyecto tiene como finalidad interceptar y modificar el trafico generado por software MYSQL mediante Polymorph 

**Instalacion Polymorph**

    apt-get install build-essential python-dev libnetfilter-queue-dev tshark tcpdump python3-pip wireshark git
    pip3 install git+https://github.com/kti/python-netfilterqueue
    pip3 install polymorph

**Uso de Polymorph**

Capturar trafico generado por los docker:
    
    capture -v -i docker0

Mostrar las funciones guardadas en polymorph:
    
    functions -s 

Abrir y editar alguna funcion:

    functions -a "nombrefuncion" -e vim
    
Interceptar trafico de los sw:

    intercept

Video explicativo (hacer click en la imagen):

[![Video explicativo](https://edteam-media.s3.amazonaws.com/courses/big/3aa59acc-3472-4875-b9c6-216825be755b.png)](https://youtu.be/Cz20_ZtU368)
