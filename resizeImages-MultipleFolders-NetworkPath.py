# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:42:33 2019

@author: BRRociniLu
"""

"""
Script para redimensionar de imagens com recursividade

"""

from PIL import Image
import glob
import os
import datetime

def main():
    
    now = datetime.datetime.now()
    
    #caminho a ser analisado - colocar "\\" no lugar de "\"
    path_in = '//SERVER/F$/Example' 
    
    #True = remover arquivos originais
    #False = não remover os arquivos originais
    removerArquivosOriginais = True
    
    #extensao procurada
    ext = '.jpg'
    
    #tamanho maximo que a imagem pode ter, serao sera redimensionada
    hd_size = 1280*1024
    
    #width para qual a img sera redimensionada
    basewidth = 1280
    
    #contadores
    redimensionados = 0
    desconsiderados = 0
    erros = 0
    
    print('*** Iniciando Script  ***\n')
   
    print('Procurando: ',path_in + '\\*' + ext)
   
    #recursivo
    result = [y for x in os.walk(path_in) for y in glob.glob(os.path.join(x[0], '*'+ ext))]
    for filename in result:
        try:
            print('\nLendo Arquivo -> ',filename)    
            img = Image.open(filename)
            
            if img.size[0]*img.size[1] > hd_size:
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
    
                img = img.resize((basewidth, hsize))
                
                print('Criado ->',filename + filename.split('\\')[-1].split('.')[0] + '_resized-' + str(now.date()) + ext)            
                img.save(filename + filename.split('\\')[-1].split('.')[0] + '_resized-' + str(now.date()) + ext)
                
                redimensionados +=1
                
                if removerArquivosOriginais:
                    print('Deletado ->',filename + filename.split('\\')[-1].split('.')[0] + ext)
                    os.remove(filename) #remove o arquivo original
            else:
                print('Nao esta em HD -> ',filename)
                desconsiderados +=1
        except IOError:
            print('Erro ao ler arquivo -> ',filename)
            erros +=1
        
        
    print('\n*** Estatisticas ***')
    print('redimensionados -> ', redimensionados)
    print('desconsiderados -> ', desconsiderados)
    print('registro  erros -> ', erros)
    print('*** Script Finalizado ***')
    
if __name__ == "__main__":
    main()