#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # empty dictionary where we'll save our tickets
    dictionary = {}
    routes = []
    # populating our hash table
    for i in range(length):
        if tickets[i].source not in dictionary:
            dictionary[tickets[i].source] = tickets[i].destination

    # add the starting ticket our route
    routes.append(dictionary["NONE"])
    # reconstructing our route
    # while i < length:
    #     if dictionary

    print("Dictionary at 0", dictionary[0])
    return routes

    # return route
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")
tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)
print(result)
