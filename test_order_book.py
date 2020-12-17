import pytest
import main


class TestOrderBook():
    order_1 = main.Order(1, 10, "id-101", "buy")
    order_2 = main.Order(2, 11, "id-102", "buy")
    order_3 = main.Order(3, 12, "id-103", "buy")
    order_4 = main.Order(4, 13, "id-104", "buy")
    order_5 = main.Order(5, 14, "id-105", "buy")
    order_6 = main.Order(6, 15, "id-106", "buy")
    total = []
    total.extend([order_5, order_3, order_6, order_2, order_1, order_4])

    def test_get_ordersSortedByPrice(self):
        orderBook = main.OrderBook()
        orderBook.addOrdersToList(self.total)

        orders = orderBook.getOrdersSortedByPrice()
        prices = []
        for i in orders:
            prices.extend([i.price])

        expectedPriceOrder = [1, 2, 3, 4, 5, 6]
        assert prices == expectedPriceOrder

    def test_get_ordersByID(self):
        orderBook = main.OrderBook()
        orderBook.addOrdersToList(self.total)

        orderID = "id-101"
        order = orderBook.getOrderByID(orderID)
        assert order.orderID == orderID

    def test_removeOrderByID(self):
        orderBook = main.OrderBook()
        orderBook.addOrdersToList(self.total)

        totalOrdersBeforeRemoving = orderBook.countOrders()
        orderID = "id-102"
        order = orderBook.getOrderByID(orderID)
        assert order.orderID == orderID

        orderBook.removeOrderByID(orderID)
        orderAfterRemoving = orderBook.getOrderByID(orderID)
        expected = None
        assert orderAfterRemoving == expected
        totalOrdersAfterRemoving = orderBook.countOrders()

        assert int(totalOrdersBeforeRemoving) == 6
        assert int(totalOrdersAfterRemoving) == 5

    def test_addOrderToList(self):
        orderBook = main.OrderBook()
        orderBook.addOrdersToList(self.total)

        totalOrdersBeforeAdding = orderBook.countOrders()
        orderID = "id-107"
        newOrder_7 = main.Order(7, 15, orderID, "buy")
        orderBook.addOrderToList(newOrder_7)

        orderAfterAdding = orderBook.getOrderByID(orderID)
        assert orderAfterAdding == newOrder_7
        totalOrdersAfterAdding = orderBook.countOrders()

        assert int(totalOrdersBeforeAdding) == 6
        assert int(totalOrdersAfterAdding) == 7


if __name__ == "__main__":
    pytest.main()
