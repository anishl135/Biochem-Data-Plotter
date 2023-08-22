import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

class BiochemistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biochemistry Software")

        self.data = []

        self.data_points_label = tk.Label(root, text="Number of Data Points:")
        self.data_points_label.pack()

        self.data_points_entry = tk.Entry(root)
        self.data_points_entry.pack()

        self.x_axis_label = tk.Label(root, text="Parameters in X axis:")
        self.x_axis_label.pack()

        self.x_axis_entry = tk.Entry(root)
        self.x_axis_entry.pack()

        self.y_axis_label = tk.Label(root, text="Parameters in Y axis:")
        self.y_axis_label.pack()

        self.y_axis_entry = tk.Entry(root)
        self.y_axis_entry.pack()

        self.enter_points_button = tk.Button(root, text="Enter Data Points", command=self.enter_data_points)
        self.enter_points_button.pack()

    def enter_data_points(self):
        try:
            data_points = int(self.data_points_entry.get())
            if data_points <= 0:
                messagebox.showerror("Error", "Number of Data Points should be positive.")
                return

            x_parameter = self.x_axis_entry.get()
            y_parameter = self.y_axis_entry.get()

            self.data = []

            self.data_entry_window = tk.Toplevel(self.root)
            self.data_entry_window.title("Enter Data Points")

            self.data_labels = []
            self.data_entries_x = []
            self.data_entries_y = []

            for i in range(data_points):
                data_label = tk.Label(self.data_entry_window, text=f"Data Point {i + 1}")
                data_label.pack()

                x_label = tk.Label(self.data_entry_window, text=f"{x_parameter}:")
                x_label.pack()
                x_entry = tk.Entry(self.data_entry_window)
                x_entry.pack()

                y_label = tk.Label(self.data_entry_window, text=f"{y_parameter}:")
                y_label.pack()
                y_entry = tk.Entry(self.data_entry_window)
                y_entry.pack()

                self.data_labels.append(data_label)
                self.data_entries_x.append(x_entry)
                self.data_entries_y.append(y_entry)

            plot_button = tk.Button(self.data_entry_window, text="Plot Graph", command=self.plot_graph)
            plot_button.pack()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def plot_graph(self):
        self.data = []

        for i in range(len(self.data_entries_x)):
            x_value = self.data_entries_x[i].get()
            y_value = self.data_entries_y[i].get()

            try:
                x_value = float(x_value)
                y_value = float(y_value)
                self.data.append((x_value, y_value))

            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")
                return

        if not self.data:
            messagebox.showerror("Error", "No data points available to plot.")
            return

        x_values = [data[0] for data in self.data]
        y_values = [data[1] for data in self.data]

        plt.figure()
        plt.plot(x_values, y_values, 'bo-', label='Data')  # 'bo-' specifies blue markers with connecting lines
        plt.title("Data Plot")
        plt.xlabel(self.x_axis_entry.get())
        plt.ylabel(self.y_axis_entry.get())
        plt.legend()
        plt.grid()
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = BiochemistryApp(root)
    root.mainloop()
