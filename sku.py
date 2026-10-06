#skugenerator
from pyscript import display, document


def sku_generator(e):
    document.getElementById("results").innerHTML = "" #clear

    #values from input field
    category = str(document.getElementById("category").value)
    products = str(document.getElementById("products").value) 
    stock = str(document.getElementById("stock").value) 

    #using the minimal amount of letters to identify a product
    category_code = category[0:3].upper()
    products_code = products[0:15:2].upper()

    #generating the sku
    FinalSKU = category_code + "-" + products_code + "-" + stock
    display(f'SKU: {FinalSKU}', target="results")