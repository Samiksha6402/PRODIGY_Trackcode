import requests
from bs4 import BeautifulSoup
import pandas as pd

# Written the function to fetch product data from Amazon(can choose any )
def fetch_product_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    product_info = {}
    name = soup.find('span', id='productTitle')  
    product_info['ProductName'] = name.text.strip() if name else "Unknown Product"
    price = soup.find('span', id='priceblock_ourprice')  
    product_info['Price'] = price.text.strip() if price else "Price Not Avaiable"
    rating = soup.find('span', class_='a-icon-alt')  
    product_info['Rating'] = rating.text.strip() if rating else "No Ratings Yet"
    reviews = soup.find('span', id='acrCustomerReviewText')  
    product_info['NumReviews'] = reviews.text.strip() if reviews else "0 Reviews"
    product_info['Category'] = 'Electronics'  
    product_info['StockQuantity'] = 'In Stock'
    product_info['Discount'] = 'None'  
    product_info['Sales'] = "No Discount"  
    asin = url.split('/dp/')[1] if '/dp/' in url else 'N/A'
    product_info['ProductID'] = asin if asin!='N/A' else "Unknown ID"
    product_info['DateAdded'] = '2024-01-01' 
    products.append(product_info)
    return products
def save_to_csv(products, filename="product.csv"):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    url = 'https://www.amazon.in/HP-Laptop-255-G9-Ryzen/dp/B0DJCTH9ZD'
    products = fetch_product_data(url)

    if products:
        custom_filename = input("Enter the filename to save the data(Press enter for default name as 'product.csv): ").strip()
        filename=custom_filename if custom_filename else "product.csv"
        save_to_csv(products,filename)
    else:
        print("No products found.")

if __name__ == "__main__":
    main()
