import requests
from bs4 import BeautifulSoup

def obter_orientacao_medica(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            orientacao = soup.find("div", class_="section-content")
            if orientacao:
                return orientacao.get_text(strip=True)
            else:
                return "Não foi possível obter a orientação médica."
        else:
            return f"Houve um problema ao acessar o site. Código de status: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Houve um erro ao acessar o site: {str(e)}"

def conversar():
    print("Baymax: Olá, eu sou Baymax. O seu agente pessoal de saúde. Como posso ajudar?")
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() in ["sair", "adeus", "até mais"]:
            print("Baymax: Até mais! Cuide-se e mantenha-se saudável!")
            break
        else:
            url_orientacao = "https://medlineplus.gov/encyclopedia.html"  # URL do MedlinePlus
            resposta = obter_orientacao_medica(url_orientacao)
            print("Baymax: Com base em sua pergunta, aqui está uma orientação médica relevante:")
            print(resposta)
            print("Baymax: Se você tiver mais perguntas ou precisar de mais assistência, estarei aqui para ajudar.")

# Exemplo de uso
conversar()
