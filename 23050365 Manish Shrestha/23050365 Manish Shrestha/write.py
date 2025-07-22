class RentalInvoice:
    def __init__(self, customer_name, date_time, rentals, total_amount):
        self.customer_name = customer_name
        self.date_time = date_time
        self.rentals = rentals
        self.total_amount = total_amount

    def save_invoice(self):
        filename = f"./rent_invoice/{self.customer_name.replace(' ', '_')}_{self.date_time.replace(':', '-')}.txt"
        with open(filename, "w") as file:
            file.write("Techno Property Nepal Multiple Plot Rental Invoice\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Date/Time: {self.date_time}\n")
            file.write(f"Customer Name: {self.customer_name}\n")
            for rental in self.rentals:
                file.write(f"Plot ID: {rental['plot_id']}, Location: {rental['location']}, ")
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
            file.write("Techno Property Nepal Multiple Plot Return Invoice\n")
            file.write("-------------------------------------------------\n")
            file.write(f"Date/Time: {self.date_time}\n")
            file.write(f"Customer Name: {self.customer_name}\n")
            for return_detail in self.returns:
                file.write(f"Plot ID: {return_detail['plot_id']}, Location: {return_detail['location']}, ")
                file.write(f"Direction: {return_detail['direction']}, Area (annas): {return_detail['area']}, ")
                file.write(f"Contract Duration (months): {return_detail['contract_duration']}, ")
                file.write(f"Actual Duration (months): {return_detail['actual_duration']}, ")
                file.write(f"Cost: Rs {return_detail['cost']}, Fine: Rs {return_detail['fine']}\n")
            file.write(f"Total Fine: Rs {self.total_fine}\n")
        print(f"Invoice saved as {filename}")
