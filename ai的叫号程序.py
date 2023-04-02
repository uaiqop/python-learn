# 这个程序是由ChatGPT写的
class Customer:
    def __init__(self, id):
        self.id = id


class Queue:
    def __init__(self):
        self.customers = []
        self.served_customer_num = 0

    def add_customer(self, customer):
        self.customers.append(customer)

    def serve_customer(self):
        if len(self.customers) > 0:
            customer = self.customers[0]
            print("正在为顾客%d叫号..." % customer.id)
            self.served_customer_num += 1
            del self.customers[0]
        else:
            print("暂时没有顾客，请稍候再来叫号。")

    def get_customer_num(self):
        return len(self.customers)

    def get_served_customer_num(self):
        return self.served_customer_num

    def is_customer_served(self, customer):
        if customer.id <= self.served_customer_num:
            return True
        else:
            return False


def main():
    queue = Queue()

    for i in range(1, 6):
        customer = Customer(i)
        queue.add_customer(customer)

    queue.serve_customer()
    queue.serve_customer()

    print("当前顾客数量: %d" % queue.get_customer_num())
    print("当前已经叫号的顾客数量: %d" % queue.get_served_customer_num())

    customer1 = Customer(1)
    customer2 = Customer(2)
    customer3 = Customer(3)
    if queue.is_customer_served(customer1):
        print("顾客1已经叫到号")
    else:
        print("顾客1还没有叫到号")
    if queue.is_customer_served(customer2):
        print("顾客2已经叫到号")
    else:
        print("顾客2还没有叫到号")
    if queue.is_customer_served(customer3):
        print("顾客3已经叫到号")
    else:
        print("顾客3还没有叫到号")


if __name__ == "__main__":
    main()
