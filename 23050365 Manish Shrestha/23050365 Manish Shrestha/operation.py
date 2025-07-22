from datetime import datetime as date

class FileOperations:
    @staticmethod
    def read_plot_file():
        plot_details = "./plots/plots.txt"
        with open(plot_details, "r") as file:
            plots = [line.strip().split(', ') for line in file.readlines()]
        return [Plot(*plot) for plot in plots]

    @staticmethod
    def write_plot_file(plots):
        with open("./plots/plots.txt", "w") as file:
            for plot in plots:
                file.write(', '.join([plot.land_id, plot.location, plot.direction, plot.area, plot.price, plot.status]) + '\n')
