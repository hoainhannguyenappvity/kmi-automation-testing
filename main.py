from tkinter import *
from tkinter import ttk

# UTILS
from utils.chromedriver import chromedriver
from tests.sign_in import sign_in
from tests.new_device import new_device
from tests.archive_device import archive_device
from tests.delete_device import delete_device

# WEBDRIVERS
webdriver = chromedriver.ChromeDriver()
webdriver.maximize()


def quit():
    webdriver.quit()
    root.quit()


# BEGIN
root = Tk()
root.iconbitmap("icon.ico")
root.title("KMI Automation Testing")
root.state("zoomed")
frm = ttk.Frame(root, padding=24)
frm.grid()
ttk.Button(frm, text="Sign In Case", command=sign_in.SignInCase(webdriver.driver).run).grid(column=0, row=1)
ttk.Button(frm, text="New Device", command=new_device.NewDeviceCase(webdriver.driver).run).grid(column=0, row=2)
ttk.Button(frm, text="Archive Device", command=archive_device.ArchiveDeviceCase(webdriver.driver).run).grid(column=0, row=3)
ttk.Button(frm, text="Delete Device", command=delete_device.DeleteDeviceCase(webdriver.driver).run).grid(column=0, row=4)
ttk.Button(frm, text="Quit", command=quit).grid(column=0, row=5)
root.mainloop()
# END
