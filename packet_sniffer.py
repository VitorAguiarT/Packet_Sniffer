import pyshark
import wget

def capturePackets(networkInterface):
    """  
    Captura pacotes continuamente da interface e printa os pacotes HTTPs filtrados.
    """
    capturePacket = pyshark.LiveCapture(interface=networkInterface, display_filter='http')
    for preFilterPacket in capturePacket.sniff_continuously():
        filteredPacket = filterHTTP(preFilterPacket)
        try:
            url = filteredPacket['http']._all_fields['http.request.full_uri']
            if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png'):
                if('Python-urllib/3.8' in filteredPacket['http']._all_fields['http.user_agent']):
                    pass
                else:
                    saveImage(url)
            else:
                pass
        except:
            pass

def filterHTTP(packet):
    """
    Filtra pacotes HTTPs.
    """
    if 'http' in packet:
        return packet

def saveImage(url):
    """
    Baixa a imagem diretamente da url capturada.
    """
    fileName = wget.download(url, out="./Captured_Images")
    print('\nDownloaded image name:', fileName)

capturePackets('wlp3s0')
