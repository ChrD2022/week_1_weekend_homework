# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
   
    search_pet_breed = []

    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            search_pet_breed.append(pet)
    return search_pet_breed

def find_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]:
        if pet ["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]:
        if pet ["name"] == pet_name:
             pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"] 

def remove_customer_cash(customers, bill):
    customers["cash"] -= bill

def get_customer_pet_count(customers):
    return len(customers['pets'])

def add_pet_to_customer(customers, pet):
    customers["pets"].append(pet)

def customer_can_afford_pet(customers, pets):
    return customers["cash"] >= pets["price"]
   
def sell_pet_to_customer(pet_shop, pet, customer):
   if pet in pet_shop["pets"]:
    if customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        add_pet_to_customer(customer, pet)
    
    
    














































































