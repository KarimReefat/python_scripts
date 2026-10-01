import os , time, win32pdh,win32api, win32con

def GetProcessID( name ) :
    object = "Process"
    items, instances = win32pdh.EnumObjectItems( None, None, object,
                                                 win32pdh.PERF_DETAIL_WIZARD )
    val = None
    if name in instances :
        hq = win32pdh.OpenQuery()
        hcs = [ ]
        item = "ID Process"
        path = win32pdh.MakeCounterPath( ( None, object, name, None, 0, item ) )
        hcs.append( win32pdh.AddCounter( hq, path ) )
        win32pdh.CollectQueryData( hq )
        time.sleep( 0.01 )
        win32pdh.CollectQueryData( hq )
        for hc in hcs:
            type, val = win32pdh.GetFormattedCounterValue( hc, win32pdh.PDH_FMT_LONG )
            win32pdh.RemoveCounter( hc )

        win32pdh.CloseQuery( hq )
        return val
 
    
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

path = r"C:\4\test\t"

exe_files_path = []

for a in os.listdir(path):
    if a[-4:] == ".exe":
        exe_files_path.append(path + "\\" + a)

for a in exe_files_path:
    os.system(a)
    time.sleep(2)
    click(600,460)
    click(600,460)
    #click(600,460)
    time.sleep(20)
    click(665,335)
    #click(665,335)
    time.sleep(5)
    click(600,460)    
    time.sleep(5)
