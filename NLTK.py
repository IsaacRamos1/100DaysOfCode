

from nltk.chat.util import Chat, reflections

#importação das bibliotecas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4 as bs
import spacy
import urllib.request
import re
import nltk
import random
import string
import requests
import numpy as np
from flask import Flask, request, jsonify


#carregamento da base de dados
dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Bact%C3%A9ria')
dados = dados.read()
dados_html = bs.BeautifulSoup(dados, 'lxml')
paragrafos = dados_html.find_all('p')

conteudo = ''
for p in paragrafos:
    conteudo += p.text

conteudo = conteudo.lower()

lista_sentencas = nltk.sent_tokenize(conteudo)
pln = spacy.load('pt_core_news_sm')
stop_words = spacy.lang.pt.stop_words.STOP_WORDS

def preprocessamento(texto):
    # remover URL
    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)
    
    #remover espaços em branco
    texto = re.sub(r" +", ' ', texto)
    
    #lematização
    documento = pln(texto)
    lista = []
    
    for token in documento:
        lista.append(token.lemma_)
        
    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
    
    return lista

lista_sentencas_preprocessadas = []
for i in range(len(lista_sentencas)):
    lista_sentencas_preprocessadas.append(preprocessamento(lista_sentencas[i]))


'''for _ in range(5):
    i = random.randint(0, len(lista_sentencas) - 1)
    print(lista_sentencas[i])
    print(lista_sentencas_preprocessadas[i])
    print('----------')'''


textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae', 'ola')
textos_boas_vindas_respostas = ('hey', 'olá', 'opa', 'oi', 'Bem Vindo!', 'como você está?')

def responder_saudacao(texto):
    for palavra in texto.split():
        if palavra.lower() in textos_boas_vindas_entrada:
            return random.choice(textos_boas_vindas_respostas)

def responder(texto_usuario):
    resposta_chatbot = ''
    lista_sentencas_preprocessadas.append(texto_usuario)
    
    tfidf = TfidfVectorizer()
    palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_preprocessadas)
    
    similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas) #ultima
    indice_sentenca = similaridade.argsort()[0][-2]
    vetor_similar = similaridade.flatten()
    vetor_similar.sort()
    
    vetor_encontrado = vetor_similar[-2]
    
    if(vetor_encontrado == 0):
        resposta_chatbot = resposta_chatbot + 'Desculpe, não entendi!'
        return resposta_chatbot
    else:
        resposta_chatbot = resposta_chatbot + lista_sentencas[indice_sentenca]
        return resposta_chatbot

continuar = True
print('Olá, sou um chatbot e vou responder perguntas sobre IA: ')
while(continuar == True):
    texto_usuario = input()
    texto_usuario = texto_usuario.lower()
    if(texto_usuario != 'sair'):
        if(responder_saudacao(texto_usuario) != None):                                     #TESTE NO CONSOLE
            print('Chatbot: ' + responder_saudacao(texto_usuario))
        else:
            print('Chatbot: ')
            print(responder(preprocessamento(texto_usuario)))
            lista_sentencas_preprocessadas.remove(preprocessamento(texto_usuario))
    
    else:
        continuar = False
        print('Chatbot: Até Breve!')

#etapa: criação da API Flask
'''app = Flask(__name__)   

@app.route("/<string:txt>", methods= ["POST"])
def conversar(txt):
    resposta = ''
    texto_usuario = txt
    texto_usuario = texto_usuario.lower()
    if(responder_saudacao(texto_usuario) != None):                                  #TESTE NO POSTMAN (APP DESKTOP)
        resposta = responder_saudacao(texto_usuario)
    else:
        resposta = responder(preprocessamento(texto_usuario))
        lista_sentencas_preprocessadas.remove(preprocessamento(texto_usuario))
    return jsonify({'texto_respondido': resposta})

app.run(port= 5000, debug= False)'''



















     


