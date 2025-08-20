import bs4
import requests


def products_price():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"
    requests_header = {
        "User-Agent": user_agent,
        "Accept-Language": "en-US, en;q=0.5",
    }
    url = "https://www.amazon.com/SUPFINE-Compatible-Protection-Translucent-Anti-Fingerprint/dp/B0D9VRKZ1D?pd_rd_w=kJQdM&content-id=amzn1.sym.f089f9cf-a233-4ca4-a53e-cc1f5dde5545&pf_rd_p=f089f9cf-a233-4ca4-a53e-cc1f5dde5545&pf_rd_r=1E69EAW25SG8X884QJEM&pd_rd_wg=II4nv&pd_rd_r=2805e12b-b98e-47e1-bbc6-119b5a1f2a1d&pd_rd_i=B0D9VRKZ1D&th=1"
    res = requests.get(url, headers=requests_header)
    res = res.content
    soup = bs4.BeautifulSoup(res, "lxml")
    price_tag = soup.select("span[class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")
    return price_tag[0].getText()

print(products_price())
