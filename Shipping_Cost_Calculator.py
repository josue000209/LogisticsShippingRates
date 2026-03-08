# Shipping Cost Calculator

## Input package weight and shipping rate
weigth = float (input("Enter the packafe weight in kilograms: "))
rate = float (input("Enter the shippin rate per kilogram"))

## Calculate shipping cost 
shipping_cost = weight * rate

## Display the result 
print (f"Shipping cost: {shipping_cost} USD")
