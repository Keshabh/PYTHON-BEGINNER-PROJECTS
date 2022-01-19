import time
import random
location_and_models={'patel nagar':{'UberGo':5,'UberAuto':7,'Go sedan':4,'Premier':0,'UberXL':2,'BikeShare':3}, 'punjabi bagh':{'UberGo':2,'UberAuto':10,'Go sedan':2,'Premier':4,'UberXL':4,'BikeShare':6}, 'karol bagh':{'UberGo':1,'UberAuto':11,'Go sedan':4,'Premier':3,'UberXL':6,'BikeShare':3}, 'rk puram':{'UberGo':3,'UberAuto':7,'Go sedan':5,'Premier':4,'UberXL':3,'BikeShare':5}}
models = ["UberGo","UberAuto","Go sedan","Premier","UberXL","BikeShare"]
ride_per_km={"UberGo":14,"UberAuto":16,"Go sedan":20,"Premier":25,"UberXL":26,"BikeShare":10}
rent_per_day= {"UberGo":1500,"UberAuto":1600,"Go sedan":2000,"Premier":2200,"UberXL":2500,"BikeShare":1000}
locations=['patel nagar','punjabi bagh','karol bagh','rk puram']
def login():
    passw="1234a"
    print("#NOTE: user pass is: 1234a")
    number= input("Enter your phone number or gamil: ")
    password = input("Password: ")
    if password==passw:
     return 1
    else:
     print("Invalid Id or Password.\n")
     login()

def source_destination():
    print("\n#NOTE: Currently cars are only available in: ",locations)
    source=input("\nEnter source: ")
    destination=input("Enter destination: ")
    val = cars_available(source)
    if val==1:
        return source
    else:
        print("Sorry, No cars are available right now in this location.")
        print("Kindly try it later or enter another location...")
        source_destination()

def cars_available(source):
    if source in location_and_models:
        #check if number of cars in that location is more than 0
        #sum all the models available in the source_area
        if sum(location_and_models[source].values()) > 0:
            return 1
        else:
            return 0
    else:
        return 0

def model_available(source,choice):
    #check if number of choice-1 index model car is more than 1 in source
    model=models[choice-1]
    if location_and_models[source][model]>0:
        return True
    else:
        return False

def select_car():
    val=int(input("\npress 1. For Ride 2. For Rent\nEnter: "))
    if val==1:
        choice=int(input("\npress 1.For UberGo 2.For UberAuto 3.Go sedan 4.Premier 5.UberXL 6.BikeShare\nEnter: "))
        day=0
    elif val==2:
        choice=int(input("\npress 1.For UberGo 2.For UberAuto 3.Go sedan 4.Premier 5.UberXL 6.BikeShare\nEnter: "))
        day= int(input("Enter number of days to rent it: "))
    else:
        print("Invalid value chosen")
        select_car()
    return val,choice,day

def book_ride():
    source=source_destination()
    val,choice,day=select_car()
    amount=payment(val,choice,day)
    print("\n...")
    time.sleep(3)
    if(model_available(source,choice)):
        print("\n**Your cab has been booked**")
        print("\n---> Cab Details")
        if val==1:
            print("Model: ",models[choice-1])
            print("Model no: ",23435422)
        else:
            print("Model: ",models[choice-1])
            print("Model no: ",23435422)
            print("Rent for: ",day," days")
        print("\n---> Driver Details")
        print("Driver Name: "+"Dhiraj kuamr")
        print("Phone number: "+ "9477393939")
        print("\n*Kindly contact him for exact location*")
        print("Total Amount to be paid is: ",amount)
        return 1
    else:
        print("Sorry this car is not available in the specified location.\nKindly look for another model.")
        return 0

def cancel_ride():
    val=int(input("print 1.To Exit 2.To Cancel Ride.\nEnter: "))
    if val==1:
        print("Thank you for enjoying the ride.\nI hope you liked our cab service.")
        exit(1)
    elif val==2:
        print("\n*Your Ride is Cancelled*")
    else:
        print("Invalid Value")
        cancel_ride()

def payment(val,choice,day):
    #calculate price for
    if val==1:
        price=ride_per_km[models[choice-1]]*random.randint(1,50)
    else:
        price=rent_per_day[models[choice-1]]*day
    return price


def main():
    if login()==1:
        if(book_ride()):
            cancel_ride()

if __name__=="__main__":
    main()
