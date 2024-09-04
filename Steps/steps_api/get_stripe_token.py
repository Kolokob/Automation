import stripe

stripe.api_key = "pk_test_51Pv0hIJolQv4GJEHBoiy1JcpoecMYYlJCwqttbYN2Luk1QGv14rsiRG6xPoqEseOA1WOaKOeSwKkL32DMCdeSW2v00jsXwGl42"

def create_stripe_token():
    try:
        token = stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": 12,
                "exp_year": 2024,
                "cvc": "123",
            },
        )
        return token.id
    except Exception as e:
        print(f"Failed to create Stripe token: {e}")
        return None

stripe_token = create_stripe_token()
if stripe_token:
    print(f"Generated Stripe token: {stripe_token}")
