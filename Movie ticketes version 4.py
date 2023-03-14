"""Movie theatre ticketing system - v4
Confirm order
Created by Sophie Sainsbury
"""


# Component 4 - Confirm Order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"You have ordered {number} {ticket} ticket(s) "
                    f"at a cost of ${cost * number:.2f\n}"
                    f"'Y' or 'N': ")
    if confirm == 'Y':
        return True

    else:
        return False


# Component 3 - Calculate ticket price
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print("********** Fanfare Movies - ticketing system **********\n")


adult_tickets = 0
child_tickets = 0
student_tickets = 0
gift_tickets = 0
tickets_sold = 0
total_sales = 0

# Component 2 - Get the category and number of tickets required


ticket_wanted = "Y"
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want: \n"
                        "\t 'A' for adult, or\n"
                        "\t 'S' for student, or\n"
                        "\t 'C' for child, or\n"
                        "\t 'G' for gift voucher\n"
                        ">> ").upper()
    num_tickets = int(input(f"How many {ticket_type} tickets do you want: "))
    cost = get_price(ticket_type)

    if confirm_order(ticket_type, num_tickets, cost):
        print("order confirmed")
    else:
        print("order canceled")

    print(f"You have ordered {num_tickets} {ticket_type} ticket(s) "
          f"at a cost of ${cost * num_tickets:.2f}")
    ticket_wanted = input("Do you want to sell another ticket (Y/N): "
                          "").upper()


# Main routine
sell_ticket()