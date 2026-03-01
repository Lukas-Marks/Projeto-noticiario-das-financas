import requests
from bs4 import BeautifulSoup
import webbrowser
from datetime import datetime


def pegar_noticias():
    # 1️⃣ Acessa o site
    url = "https://www.dadosdemercado.com.br/ultimas-noticias"
    response = requests.get(url)

    # 2️⃣ Converte HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 3️⃣ Pega div principal
    external_news = soup.find("div", id="external-news")

    # 4️⃣ Pega as primeiras 5 notícias
    news_divs = external_news.find_all("div", class_="news", recursive=False)[:20]

    noticias = []

    # 5️⃣ Extrai título e link
    for div in news_divs:
        p = div.find("p")
        if p:
            a = p.find("a")
            if a and a.get("href"):
                titulo = a.get_text(strip=True)
                link = a["href"]
                noticias.append((titulo, link))

    # 6️⃣ Captura horário atual
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return noticias, horario


def main():
    # 7️⃣ Primeira carga
    noticias, horario = pegar_noticias()

    while True:
        print("\n===== Últimas Notícias =====")
        print(f"Última atualização: {horario}\n")

        # 8️⃣ Mostra menu
        for i, (titulo, _) in enumerate(noticias, start=1):
            print(f"{i} - {titulo}")

        print("69 - Atualizar notícias (Reset)")
        print("0 - Encerrar")

        try:
            escolha = int(input("\nEscolha uma opção: "))

            if escolha == 0:
                print("Encerrando programa...")
                break

            elif escolha == 69:
                print("Atualizando notícias...\n")
                noticias, horario = pegar_noticias()

            elif 1 <= escolha <= len(noticias):
                link_escolhido = noticias[escolha - 1][1]
                print("Abrindo notícia...\n")
                webbrowser.open(link_escolhido)

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite apenas números.")


if __name__ == "__main__":
    main()