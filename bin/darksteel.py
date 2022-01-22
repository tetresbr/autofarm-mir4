from time import sleep
import datetime
import win32gui, win32ui, win32con, win32api


def main():
    game = int(input("Qual o seu client? 1-Mir4g[0] / 2-Mir4g[1] / 3-Mir4g[2]"))
    if game == 1:
        game = "Mir4G[0]"
    if game == 2:
        game = "Mir4G[1]"
    if game == 3:
        game = "Mir4G[2]"
    print(game)
    window_name = game
    hwnd = win32gui.FindWindow(None, window_name)
    #hwnd = get_inner_windows(hwnd)['Edit']
    win = win32ui.CreateWindowFromHandle(hwnd)
    count = 0
    while count < 1:
        #e
        win.SendMessage(win32con.WM_KEYDOWN, 0x45, 0)
        print("click no e - "+str(datetime.datetime.now()))
        #sleep(0.05)




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