"""
Made by Aleksander Tyamin
04.05.2021

A simple project with a primitive GUI.
This program allows you to see the load on your CPU and RAM.
"""

import sys
import tkinter
from tkinter import ttk

import cpu
import ram
import settings


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.title(settings.APPLICATION_TITLE)

        self.__cpu_load_labels = list()
        self.__cpu_load_progress_bars = list()
        self.__ram_load_label = None
        self.__ram_load_bar = None

        self.__cpu = cpu.CPU()
        self.__ram = ram.RAM()
        self.__create_widgets()
        self.__configure_cpu_section()
        self.__configure_ram_section()

    def __create_widgets(self):
        self.__create_cpu_widgets()
        self.__create_ram_widgets()

        exit_button = ttk.Button(self, text='Close', command=self.__exit)
        exit_button.pack(fill=tkinter.X)

    def __create_cpu_widgets(self):
        self.__cpu_group_elements = ttk.LabelFrame(self, text='CPU Power')
        self.__cpu_group_elements.pack(fill=tkinter.BOTH)

        cores_information = ttk.Label(self.__cpu_group_elements,
                                      text=f'Cores: {self.__cpu.amount_cores} '
                                           f'Threads: {self.__cpu.amount_threads}',
                                      anchor=tkinter.CENTER)
        cores_information.pack(fill=tkinter.X)

        for _ in range(self.__cpu.amount_threads):
            self.__cpu_load_labels.append(ttk.Label(self.__cpu_group_elements, anchor=tkinter.CENTER))
            self.__cpu_load_progress_bars.append(ttk.Progressbar(self.__cpu_group_elements, length=100))
        for i in range(self.__cpu.amount_threads):
            self.__cpu_load_labels[i].pack(fill=tkinter.X)
            self.__cpu_load_progress_bars[i].pack(fill=tkinter.X)

    def __configure_cpu_section(self):
        cores_load = self.__cpu.cores_loading
        for i in range(self.__cpu.amount_threads):
            self.__cpu_load_labels[i].configure(text=f'Core {i}: {cores_load[i]}%')
            self.__cpu_load_progress_bars[i].configure(value=cores_load[i])

        self.after(1000, self.__configure_cpu_section)

    def __create_ram_widgets(self):
        self.__ram_group_elements = ttk.LabelFrame(self, text='RAM Power')
        self.__ram_group_elements.pack(fill=tkinter.BOTH)

        self.__ram_load_label = ttk.Label(self.__ram_group_elements, text='', anchor=tkinter.CENTER)
        self.__ram_load_label.pack(fill=tkinter.X)

        self.__ram_load_bar = ttk.Progressbar(self.__ram_group_elements, length=100)
        self.__ram_load_bar.pack(fill=tkinter.X)

    def __configure_ram_section(self):
        ram_load = self.__ram.memory_usage
        ram_total_mb = round(ram_load[0]/1048576)
        ram_total_percent = ram_load[2]
        ram_used_mb = round(ram_load[3]/1048576)
        ram_available_mb = round(ram_load[1]/1048576)
        self.__ram_load_label.configure(text=f'Total: {ram_total_mb} MB\tLoad: {ram_total_percent}%\n'
                                             f'Used: {ram_used_mb} MB\tAvailable: {ram_available_mb} MB')
        self.__ram_load_bar.configure(value=ram_total_percent)

        self.after(1000, self.__configure_ram_section)

    def __exit(self):
        self.destroy()
        sys.exit()


def main():
    app = Window()
    app.mainloop()


if __name__ == '__main__':
    main()
