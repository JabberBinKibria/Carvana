# Car data with their models and specs stored as nested dictionary
car_brands = ["Audi", "Bentley", "Chevrolet", "Chrysler", "BMW", "Cadillac", "Dodge", "Ferrari", "Ford", "Mercedes"]

# Dictionary to store car models for each brand
car_models = {
    "Audi": ["Audi R8", "2024 Audi RS 3"],
    "Bentley": ["2024 Bentley Bentayga", "2024 Bentley Continental GT"],
    "Chevrolet": ["2025 Chevrolet Equinox EV", "2025 Chevrolet Corvette"],
    "Chrysler": ["2023 Chrysler 300", "2025 Chrysler Corvette"],
    "BMW": ["2025 BMW M3", "2025 BMW X1"],
    "Cadillac": ["2024 Cadillac Escalade", "2024 Cadillac Lyriq"],
    "Dodge": ["2023 Dodge Challenger", "2025 Dodge Durango"],
    "Ferrari": ["2024 Ferrari Purosangue", "2015 Ferrari 458 Spider"],
    "Ford": ["2025 Ford Mustang", "2006 Ford GT"],
    "Mercedes": ["2024 Mercedes-AMG GT", "2024 Mercedes G-Class"]
}

# Dictionary to store specifications for each car model
car_specs = {
    "Audi R8": {
        "MSRP": 158600,
        "MPG": "14 city / 23 highway",
        "Engine": "5.2 L V10",
        "Horsepower": 562,
        "Transmission": "7-speed automatic",
        "Dimensions": "174″ L x 76″ W x 49″ H"
    },
    "2024 Audi RS 3": {
        "MSRP": 62300,
        "MPG": "19 city / 29 highway",
        "Engine": "2.5 L 5-cylinder",
        "Horsepower": 401,
        "Transmission": "7-speed automatic",
        "Dimensions": "179″ L x 73″ W x 56″ H"
    },
    "2024 Bentley Bentayga": {
        "MSRP": 203200,
        "MPG": "14 city / 21 highway",
        "Engine": "4.0 L V8",
        "Horsepower": 542,
        "Transmission": "8-speed automatic",
        "Dimensions": "202-209″ L x 79″ W x 68-69″ H"
    },
    "2024 Bentley Continental GT": {
        "MSRP": 242700,
        "MPG": "14 city / 22 highway",
        "Engine": "4.0 L V8, 6.0 L W12",
        "Horsepower": 542,
        "Transmission": "8-speed automatic",
        "Dimensions": "191″ L x 77″ W x 55″ H"
    },
    "2025 Chevrolet Equinox EV": {
        "MSRP": 33600,
        "MPG": "117 city / 99 highway",
        "Engine": "Electric",
        "Horsepower": 213,
        "Transmission": "Electric",
        "Dimensions": "202-209″ L x 79″ W x 68-69″ H"
    },
    "2025 Chevrolet Corvette": {
        "MSRP": 68300,
        "MPG": "16 city / 24 highway",
        "Engine": "5.5 L V8, 6.2 L V8",
        "Horsepower": 490,
        "Transmission": "8-speed automatic",
        "Dimensions": "182-185″ L x 76-80″ W x 49″ H"
    },
    "2023 Chrysler 300": {
        "MSRP": 36145,
        "MPG": "19 city / 30 highway",
        "Engine": "3.6 L V6",
        "Horsepower": 292,
        "Transmission": "8-speed automatic",
        "Dimensions": "199″ L x 75″ W x 59″ H"
    },
    "2025 BMW M3": {
        "MSRP": 76000,
        "MPG": "16 city / 23 highway",
        "Engine": "3.0 L 6-cylinder",
        "Horsepower": 473,
        "Transmission": "8-speed automatic, 6-speed manual",
        "Dimensions": "189″ L x 74″ W x 57″ H"
    },
    "2025 BMW X1": {
        "MSRP": 40950,
        "MPG": "23 city / 31 highway",
        "Engine": "2.0 L 4-cylinder",
        "Horsepower": 241,
        "Transmission": "7-speed automatic",
        "Dimensions": "177″ L x 73″ W x 65″ H"
    },
    "2024 Cadillac Escalade": {
        "MSRP": 81895,
        "MPG": "21 city / 27 highway",
        "Engine": "3.0 L 6-cylinder diesel, 6.2 L V8",
        "Horsepower": 277,
        "Transmission": "10-speed automatic",
        "Towing Capacity": "7,000 to 7,700 lbs"
    },
    "2024 Cadillac Lyriq": {
        "MSRP": 57195,
        "MPG": "95 city / 82 highway",
        "Engine": "314 mi battery-only",
        "Horsepower": 220,
        "Transmission": "Electric"
    },
    "2023 Dodge Challenger": {
        "MSRP": 32800,
        "MPG": "19 city / 30 highway",
        "Engine": "3.6 L V6, 5.7 L V8, 6.4 L V8",
        "Horsepower": 303,
        "Transmission": "8-speed automatic, 6-speed manual",
        "Towing Capacity": "1,000 lbs"
    },
    "2025 Dodge Durango": {
        "MSRP": 41995,
        "MPG": "18 city / 25 highway",
        "Engine": "3.6 L V6, 5.7 L V8, 6.2 L V8",
        "Horsepower": 295,
        "Transmission": "8-speed automatic",
        "Towing Capacity": "6,200 to 8,700 lbs"
    },
    "2024 Ferrari Purosangue": {
        "MSRP": 393350,
        "MPG": "11 city / 15 highway",
        "Engine": "6.5 L V12",
        "Horsepower": 715,
        "Transmission": "8-speed automatic",
        "Dimensions": "196″ L x 80″ W x 63″ H"
    },
    "2015 Ferrari 458 Spider": {
        "MSRP": 259000,
        "MPG": "13 city / 17 highway",
        "Engine": "4.5 L V8",
        "Horsepower": 570,
        "Transmission": "7-speed automatic",
        "Dimensions": "178″ L x 76″ W x 48″ H"
    },
    "2025 Ford Mustang": {
        "MSRP": 31920,
        "MPG": "21 city / 32 highway",
        "Engine": "2.3 L 4-cylinder, 5.0 L V8",
        "Horsepower": 315,
        "Transmission": "10-speed automatic, 6-speed manual",
        "Dimensions": "189-190″ L x 75-76″ W x 55″ H"
    },
    "2006 Ford GT": {
        "MSRP": 60950,
        "MPG": "13 city / 31 highway",
        "Engine": "5.4 L V8",
        "Horsepower": 550,
        "Transmission": "6-speed automatic",
        "Dimensions": "183″ L x 77″ W x 44″ H"
    },
    "2024 Mercedes-AMG GT": {
        "MSRP": 168000,
        "MPG": "16 city / 22 highway",
        "Engine": "4.0L V8 Biturbo",
        "Horsepower": 577,
        "Transmission": "9-speed automatic",
        "Dimensions": "189″ L x 76″ W x 54″ H"
    },
    "2024 Mercedes G-Class": {
        "MSRP": 139900,
        "MPG": "14 city / 16 highway",
        "Engine": "4.0L V8 Biturbo",
        "Horsepower": 416,
        "Transmission": "9-speed automatic",
        "Dimensions": "191″ L x 78″ W x 77″ H"
    }
}

def display_welcome():
    # Display welcome message at program start
    print("\nWelcome to our Carvana Dealership!")
    print("=" * 34)

def display_brands():
    # Display numbered list of available car brands
    print("\nAvailable Car Brands:")
    for i in range(len(car_brands)):
        print(str(i + 1) + ". " + car_brands[i])

def get_brand_choice():
    
    # Get and validate user's brand selection
    # Returns: selected brand name as string

    while True:
        try:
            choice = int(input("\nEnter the number of your chosen brand: "))
            if 1 <= choice <= len(car_brands):
                return car_brands[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_models(brand):
    # Display available models for selected brand
    print("\nAvailable", brand, "Models:")
    models = car_models[brand]
    for i in range(len(models)):
        print(str(i + 1) + ". " + models[i])

def get_model_choice(brand):
    # Get and validate user's model selection
    models = car_models[brand]
    while True:
        try:
            choice = int(input("\nEnter the number of your chosen model: "))
            if 1 <= choice <= len(models):
                return models[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_specs(model):
    # Display specifications for selected car model
    if model in car_specs:
        specs = car_specs[model]
        print("\nCar Specifications:")
        print("=" * 30)
        print("Model:", model)
        for spec, value in specs.items():
            print(spec + ":", value)

def confirm_purchase():
    # Get purchase confirmation from user
    while True:
        choice = input("\nWould you like to confirm this purchase? (yes/no): ").lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    # Main program function that controls the program flow
    display_welcome()
    
    while True:
        display_brands()
        selected_brand = get_brand_choice()
        
        display_models(selected_brand)
        selected_model = get_model_choice(selected_brand)
        
        display_specs(selected_model)
        
        if confirm_purchase():
            print("\nPurchase confirmed!")
            print("Thank you for purchasing the", selected_model + "!")
            break
        else:
            print("\nPurchase cancelled. Let's start over.")

# Call main function
main()



