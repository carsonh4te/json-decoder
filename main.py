import json
import tkinter as tk
import os


class Transfer:

    @staticmethod
    def add_to(x, y, file):
        direct = r"/Users/cart/PycharmProjects/pythonProject/dumps"
        try:
            with open(file, "r") as json_file:
                dump = json.load(json_file)

            dump[x] = y

            with open(os.path.join(direct, file), "w") as json_file:
                json.dump(dump, json_file, indent=4)
        except Exception as e:
            print("Let's just ignore all exceptions, like this one: %s" % str(e))
        finally:
            print("Appended %s" % file)

    @staticmethod
    def write_to(data, file):
        direct = r"/Users/cart/PycharmProjects/pythonProject/dumps"
        try:
            json_object = json.dumps(data, indent=4)
            with open(os.path.join(direct, file), "w") as json_file:
                json_file.write(json_object)
        except Exception as e:
            print("Let's just ignore all exceptions, like this one: %s" % str(e))
        finally:
            print("Data Written to %s" % file)

    @staticmethod
    def read_from(x, page):
        direct = r"/Users/cart/PycharmProjects/pythonProject/dumps"
        try:
            with open(os.path.join(direct, x), "r") as json_file:
                data = json.load(json_file)
            if page != "":
                print(data[page])
            else:
                print(data)
        except Exception as e:
            print("Let's just ignore all exceptions, like this one: %s" % str(e))


class Window:
    direct = r"/Users/cart/PycharmProjects/pythonProject/dumps"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("JSON File Writer")
        self.window.geometry("725x475")

        self.name_label = tk.Label(self.window, text="Name")
        self.name_label.grid(column=0, row=0, padx=5, pady=5)

        self.name_entry = tk.Entry(self.window, width=30)
        self.name_entry.grid(column=1, row=0, padx=5, pady=5)

        self.data_label = tk.Label(self.window, text="Data")
        self.data_label.grid(column=0, row=1, padx=5, pady=5)

        self.data_entry = tk.Text(self.window)
        self.data_entry.grid(column=1, row=1, padx=5, pady=5)

        self.file_label = tk.Label(self.window, text="File Name")
        self.file_label.grid(column=0, row=2, padx=5, pady=5)

        self.file_entry = tk.Entry(self.window, width=30)
        self.file_entry.grid(column=1, row=2, padx=5, pady=5)

        self.write_button = tk.Button(self.window, text="Write", command=self.write_push)
        self.write_button.grid(column=0, row=3, padx=5, pady=5)

        self.read_button = tk.Button(self.window, text="Read", command=self.read)
        self.read_button.grid(column=1, row=3, padx=5, pady=5)

        self.l0 = tk.Label(self.window, width=3, height=3)
        self.l0.grid(column=2, row=2)

        self.window.columnconfigure(2, minsize=10)

        self.window.mainloop()

    def write_push(self):
        file = self.file_entry.get()
        name = self.name_entry.get()
        data = self.data_entry.get("1.0", "end-1c")
        directory = os.path.join(self.direct, file)
        if os.path.exists(directory):
            print(f"{directory} Already Exists, Appending Current Data")
            Transfer.add_to(name, data, directory)
        elif os.path.exists(directory) is False:
            print(f"{directory} Does Not Exist, Creating New File")
            self.write()

    def write(self):
        name = self.name_entry.get()
        data = {
            name: self.data_entry.get("1.0", "end-1c")
        }
        file = self.file_entry.get()
        Transfer.write_to(data, file)

    def read(self):
        file = self.file_entry.get()
        page = self.name_entry.get()
        Transfer.read_from(file, page)


if __name__ == "__main__":
    Window()
