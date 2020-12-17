class TrainTicket:

    def __init__(self, data, my_ticket, nearby_tickets):
        self.dic = {}
        for i in data.split("\n"):
            item = i.split(": ")
            ranges = item[1].split(" or ")
            self.dic.setdefault(item[0], []).append([int(x) for x in ranges[0].split("-")])
            self.dic.setdefault(item[0], []).append([int(x) for x in ranges[1].split("-")])
        self.tickets = []
        self.tickets.append([int(x) for x in my_ticket.split(":\n")[1].split(",")])
        for ticket in nearby_tickets.split(":\n")[1].split("\n"):
            self.tickets.append([int(x) for x in ticket.split(",")])
        self.sum = 0
        self.check_tickets()



    def check_tickets(self):
        for ticket in self.tickets:
            for number in ticket:
                if not self.in_range(number):
                    self.sum += number
        print(self.sum)


    def in_range(self, num):
        for items in self.dic.values():
            for my_range in items:
                if my_range[0] <= num <= my_range[1]:
                    return True
        return False













with open("input.txt", "r") as f:
    my_input = f.read().split("\n\n")

TrainTicket(my_input[0], my_input[1], my_input[2])
