## Question 1 ##

def calculate_discount(price, discount_percent):
    # Calculate the final price after applying a discount.
    # If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price