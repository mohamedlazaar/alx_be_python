weather = input("What's the weather like today? (sunny/rainy/cloud): ").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cloud":
    print("Make sure to wear a warm coat an a scarf.")
else:
    print("Sorry, I don't have recommandations for this weather.")