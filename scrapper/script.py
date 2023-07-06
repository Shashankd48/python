# import requests
# from bs4 import BeautifulSoup

# def scrape_website(query):
#     # Format the query for the URL
#     formatted_query = query.replace(" ", "+")
#     url = f"https://www.google.com/search?q={formatted_query}"

#     # Send GET request to the website
#     response = requests.get(url)
#     response.raise_for_status()

#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, "html.parser")

#     with open("output.html", "w", encoding="utf-8") as file:
#         file.write(soup.prettify())

#     print("soup", soup)

#     # Find and extract desired data from the parsed HTML
#     data = soup.find("div", class_="result").text

#     print("Scraped data:", data)

# # Example usage
# search_query = "reactjs jobs in india"
# scrape_website(search_query)
