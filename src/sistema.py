
import json
import re
import unicodedata
from pathlib import Path


# ==========================================
# 1. CONFIGURAÇÃO E CARREGAMENTO DOS DADOS
# ==========================================

PASTA_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_JSON = PASTA_PROJETO / "data" / "base_conhecimento.json"

GRAFO_TEMAS = {
    "Documentação": [
        "Serviços públicos",
        "Direitos do consumidor"
    ],
    "Serviços públicos": [
        "Documentação",
        "Direitos do consumidor"
    ],
    "Direitos do consumidor": [
        "Documentação",
        "Serviços públicos"
    ]
}


def carregar_base():
    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list) or not dados:
            print("Erro: base vazia ou inválida.")
            return []

        campos = {
            "id", "tema", "pergunta",
            "orientacao", "fonte",
            "data_verificacao", "palavras_chave"
        }

        for registro in dados:
            if not isinstance(registro, dict):
                print("Erro: registro inválido.")
                return []

            if not campos.issubset(registro):
                print("Erro: campos obrigatórios ausentes.")
                return []

            if not isinstance(registro["palavras_chave"], list):
                print("Erro: palavras-chave inválidas.")
                return []

        print("Base carregada com sucesso!")
        print("Quantidade de registros:", len(dados))
        return dados

    except FileNotFoundError:
        print("Erro: arquivo JSON não encontrado.")
        return []

    except (json.JSONDecodeError, UnicodeError):
        print("Erro: não foi possível ler o JSON.")
        return []


# ==========================================
# 2. NORMALIZAÇÃO E BUSCA
# ==========================================

PALAVRAS_IGNORADAS = {
    "a", "o", "as", "os", "de", "do", "da",
    "dos", "das", "um", "uma", "meu", "minha",
    "como", "para", "por", "que", "e", "em",
    "no", "na", "eu", "quero", "sobre"
}


def normalizar(texto):
    texto = unicodedata.normalize("NFD", str(texto).lower())

    return "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )


def extrair_termos(texto):
    palavras = re.findall(r"\w+", normalizar(texto))

    return {
        palavra for palavra in palavras
        if palavra not in PALAVRAS_IGNORADAS
    }


def buscar_orientacoes(pergunta, base):
    termos_pergunta = extrair_termos(pergunta)

    if not termos_pergunta:
        return []

    resultados = []

    for registro in base:
        termos_registro = extrair_termos(
            registro["pergunta"]
        )

        termos_chave = set()

        for palavra in registro["palavras_chave"]:
            termos_chave.update(extrair_termos(palavra))

        pontos_pergunta = len(
            termos_pergunta & termos_registro
        )

        pontos_chave = len(
            termos_pergunta & termos_chave
        )

        pontuacao = pontos_pergunta + (2 * pontos_chave)

        if pontuacao > 0:
            resultados.append({
                "registro": registro,
                "pontuacao": pontuacao
            })

    resultados.sort(
        key=lambda item: (
            -item["pontuacao"],
            str(item["registro"]["id"])
        )
    )

    return resultados


def avaliar_pergunta(pergunta, base):
    if not pergunta.strip():
        return None, "ENTRADA_VAZIA"

    pergunta_normalizada = normalizar(pergunta).strip(" ?!")

    # Correspondência exata tem prioridade
    for registro in base:
        cadastrada = normalizar(
            registro["pergunta"]
        ).strip(" ?!")

        if pergunta_normalizada == cadastrada:
            return registro["id"], "ENCONTRADA"

    resultados = buscar_orientacoes(pergunta, base)

    if not resultados:
        return None, "SEM_RESPOSTA"

    maior = resultados[0]["pontuacao"]

    empatados = [
        item for item in resultados
        if item["pontuacao"] == maior
    ]

    if len(empatados) > 1:
        return None, "AMBIGUA"

    return resultados[0]["registro"]["id"], "ENCONTRADA"


# ==========================================
# 3. MODELOS DE RESPOSTA
# ==========================================

def apresentar_resposta(registro, modelo=2):
    if modelo == 1:
        print("\n=== RESPOSTA SIMPLES ===")
        print(registro["orientacao"])
        print("Fonte:", registro["fonte"])

    elif modelo == 2:
        print("\n===== CITIZEN ASSIST AI =====")
        print("\nPergunta identificada:")
        print(registro["pergunta"])

        print("\nOrientação:")
        print(registro["orientacao"])

        print("\nFonte consultada:")
        print(registro["fonte"])

        print("\nData de verificação:")
        print(
            registro["data_verificacao"]
            or "Verificação pendente"
        )

        print("\nAviso:")
        print("Este assistente é um protótipo educacional.")
        print("Confirme as informações no órgão oficial.")

        print("\nAssuntos relacionados:")
        for tema in GRAFO_TEMAS.get(registro["tema"], []):
            print("-", tema)

    else:
        print("Modelo inválido.")


# ==========================================
# 4. CONSULTA DE PERGUNTAS
# ==========================================

def consultar_pergunta(pergunta, base, modelo=2):
    identificador, status = avaliar_pergunta(pergunta, base)

    if status == "ENTRADA_VAZIA":
        print("Digite uma pergunta válida.")
        return

    if status == "SEM_RESPOSTA":
        print("Não encontrei uma orientação confiável.")
        print("Consulte os temas disponíveis.")
        return

    if status == "ENCONTRADA":
        for registro in base:
            if registro["id"] == identificador:
                apresentar_resposta(registro, modelo)
                return

    # Apresentar opções em caso de empate
    resultados = buscar_orientacoes(pergunta, base)
    maior = resultados[0]["pontuacao"]

    empatados = [
        item["registro"] for item in resultados
        if item["pontuacao"] == maior
    ]

    print("\nSua pergunta pode ter mais de um significado.")

    for numero, registro in enumerate(empatados, start=1):
        print(f'{numero} - {registro["pergunta"]}')

    escolha = input(
        "\nEscolha uma orientação (0 para cancelar): "
    ).strip()

    if not escolha.isdigit():
        print("Opção inválida.")
        return

    numero = int(escolha)

    if numero == 0:
        return

    if 1 <= numero <= len(empatados):
        apresentar_resposta(empatados[numero - 1], modelo)
    else:
        print("Opção inexistente.")


# ==========================================
# 5. NAVEGAÇÃO ENTRE TEMAS
# ==========================================

def navegar_temas(base, modelo=2):
    temas = list(GRAFO_TEMAS.keys())

    while True:
        print("\n=== NAVEGAÇÃO POR TEMAS ===")

        for numero, tema in enumerate(temas, start=1):
            print(f"{numero} - {tema}")

        print("0 - Voltar ao menu principal")

        escolha = input("\nEscolha um tema: ").strip()

        if escolha == "0":
            return

        if not escolha.isdigit():
            print("Digite um número válido.")
            continue

        numero = int(escolha)

        if not 1 <= numero <= len(temas):
            print("Tema inexistente.")
            continue

        tema = temas[numero - 1]

        registros_tema = [
            registro for registro in base
            if registro["tema"] == tema
        ]

        print(f"\n=== {tema.upper()} ===")

        for registro in registros_tema:
            print(f'{registro["id"]} - {registro["pergunta"]}')

        print("\nAssuntos relacionados:")
        for relacionado in GRAFO_TEMAS[tema]:
            print("-", relacionado)

        escolha_id = input(
            "\nDigite o ID da orientação (0 para voltar): "
        ).strip()

        if escolha_id == "0":
            continue

        if not escolha_id.isdigit():
            print("Digite um ID válido.")
            continue

        id_selecionado = int(escolha_id)

        encontrado = next(
            (
                registro for registro in registros_tema
                if registro["id"] == id_selecionado
            ),
            None
        )

        if encontrado:
            apresentar_resposta(encontrado, modelo)
        else:
            print("Orientação não encontrada neste tema.")


# ==========================================
# 6. MENU PRINCIPAL
# ==========================================

def iniciar_assistente_v2(base):
    if not base:
        print("Base de conhecimento indisponível.")
        return

    modelo_atual = 2

    while True:
        print("\n===== CITIZEN ASSIST AI V2 =====")
        print("1 - Navegar pelos temas")
        print("2 - Fazer uma pergunta")
        print("3 - Alterar modelo de resposta")
        print("4 - Informações do projeto")
        print("0 - Sair")
        print(f"\nModelo atual: {modelo_atual}")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            navegar_temas(base, modelo_atual)

        elif opcao == "2":
            pergunta = input("\nDigite sua pergunta: ")
            consultar_pergunta(pergunta, base, modelo_atual)

        elif opcao == "3":
            print("\n1 - Modelo simples")
            print("2 - Modelo estruturado")

            escolha = input("Escolha o modelo: ").strip()

            if escolha in ("1", "2"):
                modelo_atual = int(escolha)
                print("Modelo atualizado!")
            else:
                print("Modelo inválido.")

        elif opcao == "4":
            print("\nCitizen Assist AI - Global Solution 2026.2")
            print("Protótipo educacional de orientação cidadã.")
            print("Não representa órgãos públicos.")
            print("Não solicita dados pessoais.")

        elif opcao == "0":
            print("\nEncerrando o Citizen Assist AI.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ==========================================
# 7. EXECUÇÃO DO PROGRAMA
# ==========================================

if __name__ == "__main__":
    base = carregar_base()
    iniciar_assistente_v2(base)
