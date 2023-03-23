#import pyautogui
#import time
#import pyperclip
import pandas as pd


def tabela():
    tabela = pd.read_csv(r"C:\Users\kezia\Downloads\Divulgação Geral (respostas) - Respostas ao formulário 1.csv", encoding="utf-8", sep=",")
    return tabela


def acessar_dados_da_tabela():
    tabela = pd.read_csv(r"C:\Users\kezia\Downloads\Divulgação Geral (respostas) - Respostas ao formulário 1.csv", encoding="utf-8", sep=",")


    qtd_linhas = tabela["Carimbo de data/hora"].count()
    print(qtd_linhas)
    aux = qtd_linhas - 1

    tipo_de_divulgacao = tabela["Tipo de divulgacao"][aux]
    # com base o tipo da divulgação fazer a seleção das cariaveis

    # ------------------------------------    DEFESA    ---------------------------------------------
    if (tipo_de_divulgacao == 'Defesa'):
        get_tipo_da_defesa(tabela, aux)
        get_titulo_da_defesa(tabela, aux)
        get_nome_do_aluno(tabela, aux)
        get_orientador(tabela, aux)
        get_coorientador(tabela, aux)
        get_banca_examinadora(tabela, aux)
        get_data_da_defesa(tabela, aux)
        get_hora_da_defesa(tabela, aux)
        get_local_da_defesa(tabela, aux)

        # mostrando na tela
        print("tipo de divulgação: " + get_tipo_de_divulgacao(tabela, aux))
        print("tipo da defesa: " + get_tipo_da_defesa(tabela, aux))
        print("título da defesa: " + get_titulo_da_defesa(tabela, aux))
        print("nome do aluno: " + get_nome_do_aluno(tabela, aux))
        print("orientador: " + get_orientador(tabela, aux))
        print("coorientador: " + get_coorientador(tabela, aux))
        print("banca examinadora: " + get_banca_examinadora(tabela, aux))
        print("data: " + get_data_da_defesa(tabela, aux))
        print("hora: " + get_hora_da_defesa(tabela, aux))
        print("local: " + get_local_da_defesa(tabela, aux))

# --------------------------------------    PUBLICAÇÃO CIENTÍFICA    ----------------------------------------
    elif (tipo_de_divulgacao == 'Publicação Científica'):

        natureza_da_publicacao(tabela, aux)
        titulo_do_trabalho(tabela, aux)
        resumo_da_publicacao(tabela, aux)
        primeiro_autor(tabela, aux)
        demais_autores(tabela, aux)
        link_da_publicacao(tabela, aux)
        informacoes_complementares_artigo(tabela, aux)

        # mostrando na tela
        print("Natureza a publicação: " + natureza_da_publicacao(tabela, aux))
        print("Título do trabalho: " + titulo_do_trabalho(tabela, aux))
        print("\nResumo da publicação: " + resumo_da_publicacao(tabela, aux))
        print("\nPrimeiro autor: " + primeiro_autor(tabela, aux))
        print("Demais autores: " + demais_autores(tabela, aux))
        print("Link da publicação: " + link_da_publicacao(tabela, aux))
        print("Informações complementares do artigo: " + informacoes_complementares_artigo(tabela, aux))

# ------------------------------------    PALESTRA/SEMINÁRIO   -------------------------------------------------
    elif (tipo_de_divulgacao == 'Palestra/Seminário'):

        nome_do_palestrante(tabela, aux)
        titulacao_do_palestrante(tabela, aux)
        descricao_da_atuacao_do_palestrante(tabela, aux)
        titulo_da_palestra(tabela, aux)
        resumo_da_palestra(tabela, aux)
        data_da_apresentacao(tabela, aux)
        hora_da_apresentacao(tabela, aux)
        local_da_apresentacao(tabela, aux)
        comentarios_adicionais_palestra(tabela, aux)

        # mostrando na tela
        print("Nome do palestrante: " + nome_do_palestrante(tabela, aux))
        print("Titulação do palestrante: " + titulacao_do_palestrante(tabela, aux))
        print("Descrição da atuação do palestrante: " + descricao_da_atuacao_do_palestrante(tabela, aux))
        print("Título da palestra: " + titulo_da_palestra(tabela, aux))
        print("\nResumo da palestra: " + resumo_da_palestra(tabela, aux))
        print("\nData da apresentação: " + data_da_apresentacao(tabela, aux))
        print("Hora da apresentação: " + hora_da_apresentacao(tabela, aux))
        print("Local da apresentação: " + local_da_apresentacao(tabela, aux))
        print("Comentários adicionais: " + comentarios_adicionais_palestra(tabela, aux))


# ------------------------------   Participação em Eventos (Congressos, Bancas Externas, Simpósios, etc)   -------------------------------

    elif (tipo_de_divulgacao == 'Participação em Eventos (Congressos, Bancas Externas, Simpósio etc)'):

        descricao_do_evento(tabela, aux)
        participante(tabela, aux)
        outras_informacoes_relevantes(tabela, aux)

        # mostrando na tela
        print("Descrição do evento: " + descricao_do_evento(tabela, aux))
        print("Participante: " + participante(tabela, aux))
        print("Outra informações relevantes: " + outras_informacoes_relevantes(tabela, aux))

# -------------------------------------   Oportunidade (estágio, IC, bolsa, etc)   --------------------------------------
    elif (tipo_de_divulgacao == 'Oportunidade (vagas de estágio, IC, bolsa etc)'):

        descricao_da_oportunidade(tabela, aux)
        contato(tabela, aux)

        # mostrar na tela
        print("Descrição da oportunidade: " + descricao_da_oportunidade(tabela, aux))
        print("Contato: " + contato(tabela, aux))

# --------------------------------------   Outros eventos   ----------------------------------------------------------
    else:
        titulo_do_evento(tabela, aux)
        data_do_evento(tabela, aux)
        hora_do_evento(tabela, aux)
        local_do_evento(tabela, aux)
        informacoes_adicionais_do_evento(tabela, aux)


        # mostrar na tela
        print("Título do evento: " + titulo_do_evento(tabela, aux))
        print("Local do evento: " + data_do_evento(tabela, aux))
        print("Hora do evento: " + hora_do_evento(tabela, aux))
        print("Título do evento: " + local_do_evento(tabela, aux))
        print("Informações adicionais do evento: " + informacoes_adicionais_do_evento(tabela, aux))






# --------------------------------------  FUNCOES DE ACESSO AOS DADOS DE "Outros eventos"   ----------------------------------------------------------
def titulo_do_evento(tabela, aux):
    if (pd.isnull(tabela["Título do evento"][aux])):
        titulo_do_evento = ''
        return titulo_do_evento
    else:
        titulo_do_evento = tabela["Título do evento"][aux]
        return titulo_do_evento


def local_do_evento(tabela, aux):
    if (pd.isnull(tabela["Local do evento"][aux])):
        local_do_evento = ''
        return local_do_evento
    else:
        local_do_evento = tabela["Local do evento"][aux]
        return local_do_evento


def data_do_evento(tabela, aux):
    if (pd.isnull(tabela["Data do evento"][aux])):
        data_do_evento = ''
        return data_do_evento
    else:
        data_do_evento = tabela["Data do evento"][aux]
        return data_do_evento


def hora_do_evento(tabela, aux):
    if (pd.isnull(tabela["Hora do evento"][aux])):
        hora_do_evento = ''
        return hora_do_evento
    else:
        hora_do_evento = tabela["Hora do evento"][aux]
        return hora_do_evento


def informacoes_adicionais_do_evento(tabela, aux):
    if (pd.isnull(tabela["Informações adicionais do evento"][aux])):
        informacoes_adicionais_do_evento = ''
        return informacoes_adicionais_do_evento
    else:
        informacoes_adicionais_do_evento = tabela["Informações adicionais do evento"][aux]
        return informacoes_adicionais_do_evento


# -------------------------------------   FUNCOES DE ACESSO AOS DADOS DE "Oportunidade (estágio, IC, bolsa, etc)"   --------------------------------------
def descricao_da_oportunidade(tabela, aux):
    if (pd.isnull(tabela["Descrição da oportunidade"][aux])):
        descricao_da_oportunidade = ''
        return descricao_da_oportunidade
    else:
        descricao_da_oportunidade = tabela["Descrição da oportunidade"][aux]
        return descricao_da_oportunidade

def contato(tabela, aux):
    if (pd.isnull(tabela["Contato"][aux])):
        contato = ''
        return contato
    else:
        contato = tabela["Contato"][aux]
        return contato


# ------------------------------   FUNCOES DE ACESSO AOS DADOS DE "Participação em Eventos (Congressos, Bancas Externas, Simpósios, etc)"   -------------------------------
def descricao_do_evento(tabela, aux):
    if (pd.isnull(tabela["Descrição do evento"][aux])):
        descricao_do_evento = ''
        return descricao_do_evento
    else:
        descricao_do_evento = tabela["Descrição do evento"][aux]
        return descricao_do_evento

def participante(tabela, aux):
    if (pd.isnull(tabela["Participante"][aux])):
        participante = ''
        return participante
    else:
        participante = tabela["Participante"][aux]
        return participante

def outras_informacoes_relevantes(tabela, aux):
    if (pd.isnull(tabela["Outras informações relevantes"][aux])):
        outras_informacoes_relevantes = ''
        return outras_informacoes_relevantes
    else:
        outras_informacoes_relevantes = tabela["Outras informações relevantes"][aux]
        return outras_informacoes_relevantes


# ------------------------------------  FUNCOES DE ACESSO AOS DADOS DE  "PALESTRA/SEMINÁRIO"   -------------------------------------------------

def nome_do_palestrante(tabela, aux):
    if (pd.isnull(tabela["Nome do(a) Palestrante"][aux])):
        nome_do_palestrante = ''
        return nome_do_palestrante
    else:
        nome_do_palestrante = tabela["Nome do(a) Palestrante"][aux]
        return nome_do_palestrante


def titulacao_do_palestrante(tabela, aux):
    if (pd.isnull(tabela["Titulação do(a) Palestrante"][aux])):
        titulacao_do_palestrante = ''
        return titulacao_do_palestrante
    else:
        titulacao_do_palestrante = tabela["Titulação do(a) Palestrante"][aux]
        return titulacao_do_palestrante


def descricao_da_atuacao_do_palestrante(tabela, aux):
    if (pd.isnull(tabela["Descrição de atuação do(a) palestrante"][aux])):
        descricao_da_atuacao_do_palestrante = ''
        return descricao_da_atuacao_do_palestrante
    else:
        descricao_da_atuacao_do_palestrante = tabela["Descrição de atuação do(a) palestrante"][aux]
        return descricao_da_atuacao_do_palestrante


def titulo_da_palestra(tabela, aux):
    if (pd.isnull(tabela["Título da Palestra"][aux])):
        titulo_da_palestra = ''
        return titulo_da_palestra
    else:
        titulo_da_palestra = tabela["Título da Palestra"][aux]
        return titulo_da_palestra


def resumo_da_palestra(tabela, aux):
    if (pd.isnull(tabela["Resumo da palestra"][aux])):
        resumo_da_palestra = ''
        return resumo_da_palestra
    else:
        resumo_da_palestra = tabela["Resumo da palestra"][aux]
        return resumo_da_palestra


def data_da_apresentacao(tabela, aux):
    if (pd.isnull(tabela["Data da apresentação"][aux])):
        data_da_apresentacao = ''
        return data_da_apresentacao
    else:
        data_da_apresentacao = tabela["Data da apresentação"][aux]
        return data_da_apresentacao


def hora_da_apresentacao(tabela, aux):
    if (pd.isnull(tabela["Hora da apresentação"][aux])):
        hora_da_apresentacao = ''
        return hora_da_apresentacao
    else:
        hora_da_apresentacao = tabela["Hora da apresentação"][aux]
        return hora_da_apresentacao


def local_da_apresentacao(tabela, aux):
    if (pd.isnull(tabela["Local da apresentação (se remoto inserir o link)"][aux])):
        local_da_apresentacao = ''
        return local_da_apresentacao
    else:
        local_da_apresentacao = tabela["Local da apresentação (se remoto inserir o link)"][aux]
        return local_da_apresentacao


def comentarios_adicionais_palestra(tabela, aux):
    if (pd.isnull(tabela["Comentários adicionais"][aux])):
        comentarios_adicionais_palestra = ''
        return comentarios_adicionais_palestra
    else:
        comentarios_adicionais_palestra = tabela["Comentários adicionais"][aux]
        return comentarios_adicionais_palestra


# ------------------------------------------  FUNCOES DE ACESSO AOS DADOS De "PUBLICAÇÃO CIENTÍFICA"   ----------------------------

def natureza_da_publicacao(tabela, aux):
    if (pd.isnull(tabela["Natureza da Publicação"][aux])):
        natureza_da_publicacao = ''
        return natureza_da_publicacao
    else:
        natureza_da_publicacao = tabela["Natureza da Publicação"][aux]
        return natureza_da_publicacao


def titulo_do_trabalho(tabela, aux):
    if (pd.isnull(tabela["Título da publicação"][aux])):
        titulo_do_trabalho = ''
        return titulo_do_trabalho
    else:
        titulo_do_trabalho = tabela["Título da publicação"][aux]
        return titulo_do_trabalho


def resumo_da_publicacao(tabela, aux):
    if (pd.isnull(tabela["Resumo da piblicação"][aux])):
        resumo_da_publicacao = ''
        return resumo_da_publicacao
    else:
        resumo_da_publicacao = tabela["Resumo da piblicação"][aux]
        return resumo_da_publicacao


def primeiro_autor(tabela, aux):
    if (pd.isnull(tabela["Primeiro Autor"][aux])):
        primeiro_autor = ''
        return primeiro_autor
    else:
        primeiro_autor = tabela["Primeiro Autor"][aux]
        return primeiro_autor


def demais_autores(tabela, aux):
    if (pd.isnull(tabela["Demais autores"][aux])):
        demais_autores = ''
        return demais_autores
    else:
        demais_autores = tabela["Demais autores"][aux]
        return demais_autores


def link_da_publicacao(tabela, aux):
    if (pd.isnull(tabela["Link da publicação"][aux])):
        link_da_publicacao = ''
        return link_da_publicacao
    else:
        link_da_publicacao = tabela["Link da publicação"][aux]
        return link_da_publicacao


def informacoes_complementares_artigo(tabela, aux):
    if (pd.isnull(tabela["Informações Complementares"][aux])):
        informacoes_complementares_artigo = ''
        return informacoes_complementares_artigo
    else:
        informacoes_complementares_artigo = tabela["Informações Complementares"][aux]
        return informacoes_complementares_artigo


# ------------------------------------------  FUNCOES DE ACESSO AOS DADOS DE "DEFESA"   ----------------------------
def get_tipo_de_divulgacao(tabela, aux):
    tipo_de_divulgacao = tabela["Tipo de divulgacao"][aux]
    return tipo_de_divulgacao


def get_tipo_da_defesa(tabela, aux):
    if (pd.isnull(tabela["Tipo da Defesa"][aux])):
        tipo_da_defesa = ''
        return tipo_da_defesa
    else:
        tipo_da_defesa = tabela["Tipo da Defesa"][aux]
        return tipo_da_defesa


def get_titulo_da_defesa(tabela, aux):
    if (pd.isnull(tabela["Titulo da defesa"][aux])):
        titulo_da_defesa = ''
        return titulo_da_defesa
    else:
        titulo_da_defesa = tabela["Titulo da defesa"][aux]
        return titulo_da_defesa


def get_nome_do_aluno(tabela, aux):
    if (pd.isnull(tabela["Nome do aluno (a)"][aux])):
        nome_do_aluno = ''
        return nome_do_aluno
    else:
        nome_do_aluno = tabela["Nome do aluno (a)"][aux]
        return nome_do_aluno


def get_orientador(tabela, aux):
    if (pd.isnull(tabela["Orientador (a)"][aux])):
        orientador = ''
        return orientador
    else:
        orientador = tabela["Orientador (a)"][aux]
        return orientador


def get_coorientador(tabela, aux):
    if (pd.isnull(tabela["Coorientador (a)"][aux])):
        coorientador = ''
        return coorientador
    else:
        coorientador = tabela["Coorientador (a)"][aux]
        return coorientador


def get_banca_examinadora(tabela, aux):
    if (pd.isnull(tabela["Banca examinadora - formato: Nome - Instituição"][aux])):
        banca_examinadora = ''
        return banca_examinadora
    else:
        banca_examinadora = tabela["Banca examinadora - formato: Nome - Instituição"][aux]
        return banca_examinadora


def get_data_da_defesa(tabela, aux):
    if (pd.isnull(tabela["Data da defesa"][aux])):
        data_da_defesa = ''
        return data_da_defesa
    else:
        data_da_defesa = tabela["Data da defesa"][aux]
        return data_da_defesa


def get_hora_da_defesa(tabela, aux):
    if (pd.isnull(tabela["Hora da defesa"][aux])):
        hora_da_defesa = ''
        return hora_da_defesa
    else:
        hora_da_defesa = tabela["Hora da defesa"][aux]
        return hora_da_defesa


def get_local_da_defesa(tabela, aux):
    if (pd.isnull(tabela["Local da defesa (inserir link se for remoto)"][aux])):
        local_da_defesa = ''
        return local_da_defesa
    else:
        local_da_defesa = tabela["Local da defesa (inserir link se for remoto)"][aux]
        return local_da_defesa
