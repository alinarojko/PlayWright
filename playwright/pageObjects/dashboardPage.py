from pageObjects.orderHistoryPage import OrderHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavigationLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        return OrderHistoryPage(self.page)


