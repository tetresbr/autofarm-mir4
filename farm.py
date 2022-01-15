from time import sleep
import datetime
import win32gui, win32ui, win32con
import os
from config import *

if farmar == 1:

    if mobs == 8:  
        agra = 1

    if mobs == 7:
        agra = 2

    if mobs == 6:
        agra = 3

    if mobs == 5:
        agra = 4

    if mobs == 4:
        agra = 5

    if mobs == 3:
        agra = 6

    if mobs == 2:
        agra = 7

    if mobs == 1:
        agra = 8


def main():
    window_name = "Mir4G[0]"
    hwnd = win32gui.FindWindow(None, window_name)
    win = win32ui.CreateWindowFromHandle(hwnd)

    print("================================= AUTO FARM ==================================")
    print("==============================================================================")
    print("=================================== Tetres ===================================")
    print("============== DOE VIA PIX d1d14bdc-9dfe-4281-a49e-c1a8f5dcfa67 ==============")
    print("==============================================================================")
    print("==============================================================================")
    print("================== " + str(datetime.datetime.now())+" Bot iniciado  ==================")
    print("==============================================================================")

    count = 0
    while count < 1:
        
        if farmar == 1:
            #TAB
            win.SendMessage(win32con.WM_KEYDOWN, 0x09, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x09, 0)
            sleep(0.01)
            win.SendMessage(win32con.WM_KEYUP, 0x09, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x09, 0)

            #PGDN
            f = 0
            while f < agra:
                win.SendMessage(win32con.WM_KEYDOWN, 0x22, 0)
                sleep(0.01)
                win.SendMessage(win32con.WM_KEYUP, 0x22, 0)
                f = f+1

            #F
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x46, 0)

        #Desvio
        if desvio == 1:
            win.SendMessage(win32con.WM_KEYDOWN, 0xA0, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0xA0, 0)
            #sleep(0.01)
            win.SendMessage(win32con.WM_KEYUP, 0xA0, 0)
            win.SendMessage(win32con.WM_KEYUP, 0xA0, 0)
            #print(str(datetime.datetime.now())+" - Desvio[Shift]")

        #ULT
        if ult == 1:
            win.SendMessage(win32con.WM_KEYDOWN, 0x52, 0)
            win.SendMessage(win32con.WM_KEYDOWN, 0x52, 0)
            #sleep(0.01)
            win.SendMessage(win32con.WM_KEYUP, 0x52, 0)
            win.SendMessage(win32con.WM_KEYUP, 0x52, 0)
            #print(str(datetime.datetime.now())+" - Ult[R]")
        sleep(tempo)



def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

main()