from playwright.sync_api import Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}


class APIUtils:

    def getToken(self, playwright:Playwright, user_credentials):
        email = user_credentials["user_email"]
        password = user_credentials["user_password"]

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        responce = api_request_context.post("api/ecom/auth/login",
                                            data={"userEmail": email, "userPassword": password})
        assert responce.ok
        print(responce.json())
        token = responce.json()["token"]
        return token

    def createOrder(self, playwright:Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        responce = api_request_context.post("api/ecom/order/create-order",
                                                    data=ordersPayload,
                                                    headers={"Authorization": token, "Content-Type": "application/json"})
        print(responce.json())
        order_number = responce.json()["orders"][0]
        return order_number
