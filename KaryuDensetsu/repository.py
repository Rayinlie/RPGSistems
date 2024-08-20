import json

# Função para selecionar trunfo por ID
def selecionar_trunfo_por_id(trunfo_id, filepath):
    # Carrega o conteúdo do JSON
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)

    # Lista de trunfos
    trunfos = data["trunfos"]

    for trunfo in trunfos:
        if trunfo["id"] == trunfo_id:
            return trunfo
    return "Trunfo não encontrado."

# Função para selecionar trunfo por Nome
def selecionar_trunfo_por_nome(nome,filepath):
    # Carrega o conteúdo do JSON
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)

    # Lista de trunfos
    trunfos = data["trunfos"]

    for trunfo in trunfos:
        if trunfo["name"].lower() == nome.lower():
            return trunfo
    return "Trunfo não encontrado."

# Função para selecionar caminho por ID
def selecionar_caminho_por_id(caminho_id,filepath):
    with open(filepath, encoding='utf-8') as file:
        caminhos = json.load(file)["caminhos"]

    for caminho in caminhos:
        if caminho["id"] == caminho_id:
            return caminho
    return "Caminho não encontrado."

# Função para selecionar caminho por Nome
def selecionar_caminho_por_nome(nome,filepath):
    with open(filepath, encoding='utf-8') as file:
        caminhos = json.load(file)["caminhos"]

    for caminho in caminhos:
        if caminho["name"].lower() == nome.lower():
            return caminho
    return "Caminho não encontrado."

def selecionar_upgrade_por_id(upgrade_id,filepath):
    with open(filepath, encoding='utf-8') as file:
        upgrades = json.load(file)["upgrades"]

    for upgrade in upgrades:
        if upgrade["id"] == upgrade_id:
            return upgrade
    return "Upgrade não encontrado."

def selecionar_upgrade_por_nome(nome,filepath):
    with open(filepath, encoding='utf-8') as file:
        upgrades = json.load(file)["upgrades"]

    for upgrade in upgrades:
        if upgrade["name"].lower() == nome.lower():
            return upgrade
    return "Upgrade não encontrado."

def selecionar_tecnica_por_id(tecnica_id,filepath):
    with open(filepath, encoding='utf-8') as file:
        tecnicas = json.load(file)["tecnicas"]

    for tecnica in tecnicas:
        if tecnica["id"] == tecnica_id:
            return tecnica
    return "Técnica não encontrada."

def selecionar_tecnica_por_nome(nome,filepath):
    with open(filepath, encoding='utf-8') as file:
        tecnicas = json.load(file)["tecnicas"]

    for tecnica in tecnicas:
        if tecnica["name"].lower() == nome.lower():
            return tecnica
    return "Técnica não encontrada."

def selecionar_ocupacao_por_id(ocupacao_id,filepath):
    with open(filepath, encoding='utf-8') as file:
        ocupacoes = json.load(file)["ocupacoes"]

    for ocupacao in ocupacoes:
        if ocupacao["id"] == ocupacao_id:
            return ocupacao
    return "Ocupação não encontrada."

def selecionar_ocupacao_por_nome(nome,filepath):
    with open(filepath, encoding='utf-8') as file:
        ocupacoes = json.load(file)["ocupacoes"]

    for ocupacao in ocupacoes:
        if ocupacao["name"].lower() == nome.lower():
            return ocupacao
    return "Ocupação não encontrada."