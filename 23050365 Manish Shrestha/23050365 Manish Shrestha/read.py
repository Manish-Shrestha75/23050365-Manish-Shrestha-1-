class Plot:
    def __init__(self, plot_id, location, direction, area, price, status):
        self.plot_id = plot_id
        self.location = location
        self.direction = direction
        self.area = area
        self.price = price
        self.status = status

    def __str__(self):
        return f"Plot ID: {self.plot_id}, Location: {self.location}, Direction: {self.direction}, Area (annas): {self.area}, Price (per month): Rs {self.price}"
