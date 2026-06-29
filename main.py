
contacts={
    "Abrar":{"phone":"894765285", "city":"hyderabad"},
    "Arhan":{"phone":"584654656","city":"Hyderabad"}

}

def add_contact(name, phn, city):
    contacts[name]={"phone":phn, "city":city}

    print(f"contact {name} was added")


def search(name):
    information=contacts.get(name)
    if information:
        print(f"found :{name}")
        print(f"phone number: {information['phone']}")
        print(f"city {information['city']}")

while True:
    n=int(input("enter a choice:"))
    if n==1:
        namee=str(input("enter your name"))
        phonee=int(input("phn no: "))
        cityy=str(input("city: "))
        add_contact(namee, phonee, cityy)
    if n==2:
        name_to_be_searched=str(input("name:"))
        search(name_to_be_searched)
    








