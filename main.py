import scrapy

#Uma "spider" em Scrapy é uma classe que determina quais dados serão extraídos e como será feita a navegação entre páginas
#CSS Selectors: https://www.w3schools.com/cssref/css_selectors.php
#Request: requisição a um site podendo conter URLs ou outros
#Response: resposta do site após uma requisição recebida como um argumento de uma função parse ou callback. Contém o código HTML ou outros
#>: filho direto


class StakeSpider(scrapy.Spider):
    name = 'spider_stake' #Nome no terminal
    start_urls = ['https://stake.bet.br/esportes/futebol/brasil/brasileirao-serie'] #Link onde o scraping começa

    def parse(self, response):
        linhas = response.css('li.KambiBC-sandwich-filter__event-list-item') #Pega cada linha contendo os jogos, porcentagens e número de apostas

        for linha in linhas:
            times = response.css('div.sc-fqkvVR.cyiQDV::text').get()
            time_casa = times[0]
            time_fora = times[1]

            dia_jogo = response.css('div.KambiBC-event-item__match-clock-container > div > span.KambiBC-event-item__start-time--date::txt').get() #Verificar
            hora_jogo = response.css('div.KambiBC-sandwich-filter__event-detail-container > div.KambiBC-sandwich-filter__event-detail-top > div.KambiBC-event-item__match-clock-container > div > span.KambiBC-event-item__start-time--time::txt').get() #Verificar
            #teste

#sc-fqkvVR cyiQDV: classe usada para o nome dos times dentro dos quadrados(está em ordem)
#sc-kAyceB dwQxLC: classe usada para as porcentagens
#KambiBC-sandwich-filter_show-more-right-text: classe usada para o número de apostas
