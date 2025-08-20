import requests
import csv
import bs4


def main():
    url_list = extract_urls()
    raw_data = products_info(url_list)
    write_csv(raw_data)


def extract_urls():
    with open("url_file.csv", newline="") as csv_file:
        reader = csv.reader(csv_file)
        urls = []

        for row in reader:
            urls.append(row[0])
    return urls


def products_info(urls):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"
    requests_header = {
        "User-Agent": user_agent,
        "Accept-Language": "en-US, en;q=0.5",
    }

    products_data = []
    for url in urls:
        print(f"scrapping through url: {url}")
        res = requests.get(url, headers=requests_header)
        html_page = res.content
        soup = bs4.BeautifulSoup(html_page, "lxml")

        price = products_price(soup)
        title = products_title(soup)
        rating = products_rating(soup)
        description = product_description(soup)

        title = title.strip()
        product_details = {
            "title": title,
            "price": price,
            "rating": rating,
            "description": description,
        }
        products_data.append(product_details)
    return products_data


def products_price(soup):
    price_tag = soup.select("span[class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")
    return price_tag[0].getText()


def products_title(soup):
    title_tag = soup.select("#productTitle")[0]
    return title_tag.getText()


def products_rating(soup):
    rating_tag = soup.select("#acrPopover")
    return rating_tag[0].get("title")


def product_description(soup):
    details_keys = soup.select("th[class='a-color-secondary a-size-base prodDetSectionEntry']")
    details_values = soup.select("td[class='a-size-base prodDetAttrValue']")

    details = {}
    for i in range(len(details_values)):
        details[details_keys[i].getText()] = details_values[i].getText()
    return details


def write_csv(data):
    with open("amazon_products_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price", "rating", "description"])
        writer.writeheader()
        for i in range(len(data)):
            writer.writerow({
                "title": data[i]["title"],
                "price": data[i]["price"],
                "rating": data[i]["rating"],
                "description": data[i]["description"],
            })


if __name__ == "__main__":
    main()
