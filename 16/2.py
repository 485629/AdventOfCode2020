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
        self.tickets = [ticket for ticket in self.tickets if self.check_ticket(ticket)]
        self.order = [set(self.dic.keys())] * len(self.dic.keys())
        self.indexes = {}

    def check_ticket(self, ticket):
        for number in ticket:
            if not self.in_any_range(number):
                return False
        return True

    def in_any_range(self, num):
        return any([self.in_one_range(k, num) for k in self.dic.keys()])

    def in_one_range(self, key, num):
        for my_range in self.dic[key]:
            if my_range[0] <= num <= my_range[1]:
                return key
        return False

    def determine_order(self):
        for ticket in self.tickets:
            for index in range(len(ticket)):
                s = set(self.in_one_range(k, ticket[index]) for k in self.dic.keys())
                if False in s:
                    s.remove(False)
                self.order[index] = self.order[index].intersection(s)
        self.indexes = {}

        while len(self.indexes.keys()) != len(self.dic.keys()):
            for index in range(len(self.order)):
                if len(self.order[index]) == 1:
                    key = next(iter(self.order[index]))
                    self.indexes[key] = index
                    for x in self.order:
                        if key in x:
                            x.remove(key)

    def compute_my_ticket(self):
        self.determine_order()
        num = 1
        for key in self.indexes.keys():
            if key.startswith("departure"):
                num *= self.tickets[0][self.indexes[key]]
        return num


with open("input.txt", "r") as f:
    my_input = f.read().split("\n\n")

print(TrainTicket(my_input[0], my_input[1], my_input[2]).compute_my_ticket())
