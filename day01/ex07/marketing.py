import sys


def get_all(a, b, c):
    a = set(a)
    b = set(b)
    c = set(c)
    d = a.union(b).union(c)
    return d

def not_seen_email(all, a, b, c):
    print(all - c)

def not_client(all, a, b, c):
    print(all - a)

def client_not_seen_event(all, a, b, c):
    print(a - b)

def run(cmd):
    clients =       ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants =  ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients =    ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    a = set(clients)
    b = set(participants)
    c = set(recipients)
    all = get_all(clients, participants, recipients)

    if cmd == "call_center":
        not_seen_email(all, a, b, c)
    elif cmd == "potential_clients":
        not_client(all, a, b, c)
    elif cmd == "loyalty_program":
        client_not_seen_event(all, a, b, c)
    else:
        raise Exception("wrong name")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1])

# call_center, potential_clients, loyalty_program