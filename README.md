# Packet_Sniffer
**Sniffer de Pacotes HTTP, Desenvolvido no Período 2020.1, Cadeira: IF678 - Infraestrutura de Comunicação**

- O Script foi desenvolvido utilizando Python3 e as bibliotecas PyShark e Wget.

**Objetivo**

- Capturar pacotes, filtrar os pacotes HTTPs e armazenar em um diretório local todas as imagens contidas nos pacotes filtrados.


**Instalando o PyShark e Wget (Ubuntu)**

$ sudo apt-get install python3-pip

$ sudo apt-get update -y && sudo apt-get install -y tshark

$ sudo pip3 install wget

$ python3 -m pip install pyshark
  *OU*
$ git clone https://github.com/KimiNewt/pyshark.git && cd pyshark/src && sudo python3 setup.py install

**Exacutando o Script**

$ sudo python3 packet_sniffer.py
