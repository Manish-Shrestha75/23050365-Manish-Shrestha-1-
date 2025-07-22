from datetime import datetime as date

print("============================================================")
print("||           WELCOME TO THE LAND RENTAL SYSTEM :)         >>")
print("============================================================")

class Land:
    def __init__(self, plot_id, location, direction, area, price, status):
        self.plot_id = plot_id
        self.location = location
        self.direction = direction
        self.area = area
        self.price = price
        self.status = status

    def __str__(self):
        return f"Land ID: {self.plot_id}, Location: {self.location}, Direction: {self.direction}, Area (annas): {self.area}, Price (per month): Rs {self.price}"

class RentalInvoice:
    def __init__(self, customer_name, date_time, rentals, total_amount):
        self.customer_name = customer_name
        self.date_time = date_time
        self.rentals = rentals
        self.total_amount = total_amount

    def save_invoice(self):
        filename = f"./rent_invoice/{self.customer_name.replace(' ', '_')}_{self.date_time.replace(':', '-')}.txt"
        with open(filename, "w") as file:
            file.write("Techno Property Nepal Multiple Land Rental Invoice\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Date/Time: {self.date_time}\n")
            file.write(f"Customer Name: {self.customer_name}\n")
            for rental in self.rentals:
                file.write(f"Land ID: {rental['plot_id']}, Location: {rental['location']}, ")
                file.write(f"Direction: {rental['direction']}, Area (annas): {rental['area']}, ")
                file.write(f"Duration (months): {rental['duration']}, Cost: Rs {rental['cost']}\n")
            file.write(f"Total Amount: Rs {self.total_amount}\n")
        print(f"Invoice saved as {filename}")

class ReturnInvoice:
    def __init__(self, customer_name, date_time, returns, total_fine):
        self.customer_name = customer_name
        self.date_time = date_time
        self.returns = returns
        self.total_fine = total_fine

    def save_invoice(self):
        filename = f"./return_invoice/{self.customer_name.replace(' ', '_')}_{self.date_time.replace(':', '-')}.txt"
        with open(filename, "w") as file:
            file.write("Techno Property Nepal Multiple Land Return Invoice\n")
            file.write("------------------------------------------------\n")
            file.write(f"Date/Time: {self.date_time}\n")
            file.write(f"Customer Name: {self.customer_name}\n")
            for return_detail in self.returns:
                file.write(f"Land ID: {return_detail['plot_id']}, Location: {return_detail['location']}, ")
                file.write(f"Direction: {return_detail['direction']}, Area (annas): {return_detail['area']}, ")
                file.write(f"Contract Duration (months): {return_detail['contract_duration']}, ")
                file.write(f"Actual Duration (months): {return_detail['actual_duration']}, ")
                file.write(f"Cost: Rs {return_detail['cost']}, Fine: Rs {return_detail['fine']}\n")
            file.write(f"Total Fine: Rs {self.total_fine}\n")
        print(f"Invoice saved as {filename}")

class LandManagementSystem:
    def __init__(self):
        self.lands = self.read_land_file()

    def read_land_file(self):
        land_details = "./lands/lands.txt"
        with open(land_details, "r") as file:
            lands = [line.strip().split(', ') for line in file.readlines()]
        return [Land(*land) for land in lands]

    def write_land_file(self):
        with open("./lands/lands.txt", "w") as file:
            for land in self.lands:
                file.write(', '.join([land.plot_id, land.location, land.direction, land.area, land.price, land.status]) + '\n')

    def print_lands_data(self, available=True):
        print("\nAvailable Lands:" if available else "\nRented Lands:")
        for land in self.lands:
            if (land.status == "Available" and available) or (land.status == "Not Available" and not available):
                print(land)
    def rent_status_lands(self):
        rent_status = True
        total_amount = 0
        rentals = []
        customer_name = input("Enter your name: ")
        
        while rent_status:
            self.print_lands_data()
            plot_id = input("\nEnter the land ID: ")
            try:
                duration = int(input("\nEnter the duration of the rent in months: "))
                found = False
                for land in self.lands:
                    if land.plot_id == plot_id and land.status == "Available":
                        land.status = "Not Available"
                        cost = int(land.price) * duration
                        total_amount += cost
                        rentals.append({
                            'plot_id': land.plot_id,
                            'location': land.location,
                            'direction': land.direction,
                            'area': land.area,
                            'duration': duration,
                            'cost': cost
                        })
                        found = True
                        break
                if not found:
                    print("\nThe selected land is unavailable or the land ID is invalid.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number for the duration.")
            more = input("\nWould you like to rent more lands? (yes/no): ").lower()
            if more != 'yes':
                rent_status = False

        if rentals:
            date_now = date.now().strftime("%Y-%m-%d %H:%M:%S")
            rental_invoice = RentalInvoice(customer_name, date_now, rentals, total_amount)
            rental_invoice.save_invoice()
            self.write_land_file()
            print("""
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                Thank you for choosing our lands.
                        All selected lands have been rented successfully.
                    Please check the rent_invoice folder for your invoice.
               ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                """)
        else:
            print("No lands were rented.")

    def return_land(self):
        returning = True
        total_fine = 0
        returns = []
        customer_name = input("Enter your name: ")

        while returning:
            self.print_lands_data(available=False)
            plot_id = input("Enter the land ID of the land to return: ")
            try:
                actual_duration = int(input("Enter the actual duration of the rent in months: "))
                contract_duration = int(input("Enter the duration as per contract in months: "))
                found = False
                for land in self.lands:
                    if land.plot_id == plot_id and land.status == "Not Available":
                        land.status = "Available"
                        cost = int(land.price) * contract_duration
                        fine = (actual_duration - contract_duration) * int(land.price) * 1.5 if actual_duration > contract_duration else 0
                        total_fine += fine
                        returns.append({
                            'plot_id': land.plot_id,
                            'location': land.location,
                            'direction': land.direction,
                            'area': land.area,
                            'actual_duration': actual_duration,
                            'contract_duration': contract_duration,
                            'cost': cost,
                            'fine': fine
                        })
                        found = True
                        break
                if not found:
                    print("Invalid land ID or the land is not currently rented.")
            except ValueError:
                print("Invalid input. Please enter a valid number for durations.")

            more = input("Do you want to return more lands? (yes/no): ").lower()
            if more != 'yes':
                returning = False

        if returns:
            date_now = date.now().strftime("%Y-%m-%d_%H_%M_%S")
            return_invoice = ReturnInvoice(customer_name, date_now, returns, total_fine)
            return_invoice.save_invoice()
            self.write_land_file()
            print("All selected lands have been returned successfully.")
        else:
            print("No lands were returned.")

    def display_all_lands(self):
        self.print_lands_data(available=True)
        self.print_lands_data(available=False)

    def main(self):
        while True:
            print("\n1. Rent Land\n2. Return Land\n3. Display Available and Rented Lands\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.rent_status_lands()
            elif choice == '2':
                self.return_land()
            elif choice == '3':
                self.display_all_lands()
            elif choice == '4':
                print("Thank you for using the system.")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    land_system = LandManagementSystem()
    land_system.main()
