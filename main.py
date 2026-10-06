#meowreceipt
from pyscript import display, document


def Meowreceipt(e): #computing for the meowceipt
    document.getElementById('results').innerHTML = "" #clear
    submeow = float(document.getElementById('submeow').value) 

    #getting the vat and total
    vat = submeow * 0.12 
    total = submeow + vat

    display(f"Subtotal: ₱{submeow:.2f}", target ='results')
    display(f"VAT: ₱{vat:.2f}", target ='results')
    display(f"Total: ₱{total:.2f}", target ='results')