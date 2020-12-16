import uuid
from random import randrange


class Order:
    def __init__(self, price, volume, orderID, orderType):
        """Order stored necessary order data"""
        self.orderID = orderID
        self.orderType = orderType
        self.price = price
        self.volume = volume


class OrderBook:
    def __init__(self):
        """ Order Book stored several orders"""

        self.orders = []

    def addOrdersToList(self, orders):
        """
        add several orders to list
        """
        for order in orders:
            self.addOrderToList(order)

    def addOrderToList(self, order):
        """
        add order to list
        """
        self.orders.append(order)

    def removeOrderByID(self, orderID):
        """
        remove order from list
        """
        order = self.getOrderByID(orderID)
        self.orders.remove(order)

    def getOrderByID(self, orderID):
        """
        get order by id in list of orders
        """
        for order in self.orders:
            if order.orderID == orderID:
                return order

    def countOrders(self):
        """
        return total number of orders
        """
        return len(self.orders)

    def displayOrders(self):
        """print all orders"""
        for i in self.orders:
            self.displayOrder(i)

    def displaySortedOrdersByPrice(self):
        """print all orders sorted by price"""
        sortedOrders = self.getOrdersSortedByPrice()
        for i in sortedOrders:
            self.displayOrder(i)

    def getOrdersSortedByPrice(self):
        """receive all orders sorted by price"""
        orders = self.orders
        orders.sort(key=lambda order: order.price)
        return orders

    def displayOrder(self, order):
        """print all orders"""
        print("orderID: ", order.orderID)
        print("orderType: ", order.orderType)
        print("price: ", order.price)
        print("volume: ", order.volume)
        print("\n")


if __name__ == '__main__':
    # create 6 orders
    order_1 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    order_2 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    order_3 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    order_4 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    order_5 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    order_6 = Order(
        randrange(
            1000, 3000), randrange(
            10000, 50000), uuid.uuid4(), "buy")
    orders = []

    orders.extend([order_1, order_2, order_3, order_4, order_5, order_6])
    orderBook = OrderBook()
    orderBook.addOrdersToList(orders)
    print("Result of order book: \n")
    orderBook.displaySortedOrdersByPrice()
