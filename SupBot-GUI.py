from tkinter import ttk
from tkinter import *
from splinter import Browser
from selenium import webdriver
# Setup for Splinter
browser = "empty"
refresh = True
# Setup for Tk
master = Tk()
master.title("SupBot")

# Setup for ttk
style = ttk.Style()
style.configure(style="my.TButton", foreground="black", background="white", font=('Times', 15))

# adds icon
master.iconbitmap('S.ico')

# makes the window a constant size
master.geometry('700x600')
master.resizable(0, 0)


# defines the functions for the widgets
def refresh_browser_func():
    global browser
    global refresh
    while refresh:
        browser.reload()


def stop_refreshing_browser_func():
    global refresh
    refresh = False


def opens_browser_func():
    global browser
    browser = Browser('chrome')
    browser.visit('https://www.supremenewyork.com/shop/')
    refresh_browser_Btn.grid(row=1, column=0)
    stop_refreshing_browser_Btn.grid(row=1, column=2)


# defines the widgets
opens_browser_Btn = ttk.Button(master, text="Launch Supreme", style="my.TButton", width="20", command=opens_browser_func)
refresh_browser_Btn = ttk.Button(master, text="Refresh", style="my.TButton", width="20", command=refresh_browser_func)
stop_refreshing_browser_Btn = ttk.Button(master, text="Stop Refreshing", style="my.TButton", width="20", command= stop_refreshing_browser_func)

# places the widgets
opens_browser_Btn.grid(row=0, column=0)


# runs Tk
master.mainloop()

driver = webdriver.Firefox()
driver.get('http://google.com')

ids = driver.find_elements_by_xpath('//*[@id]')
def elements():
    for ii in ids:
        print(ii.get_attribute('id'))

elements()