from pageObjects.orderDetailsPage import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def selectOrder(self, order_number):
        row = self.page.locator("tr").filter(has_text=order_number)
        row.get_by_role("button", name="View").click()
        return OrderDetailsPage(self.page)






