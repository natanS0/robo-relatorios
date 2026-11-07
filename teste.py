from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://www.bing.com")
    
    # Digita a pesquisa
    page.fill('textarea[name="q"]', "Notícias sobre o IBGE")
    page.press('textarea[name="q"]', "Enter")
    
    # 👇 A MÁGICA ACONTECE AQUI 👇
    # O robô vai esperar até que a caixa de resultados do Bing (#b_results) apareça.
    # Se demorar mais de 10 segundos, ele desiste e dá erro.
    page.wait_for_selector('#b_results', timeout=10000) 
    
    # Só depois que os resultados aparecerem, ele tira o print
    page.screenshot(path="resultado_bing.png")
    
    browser.close()