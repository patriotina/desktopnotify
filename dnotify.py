import notify2

ICON_PATH = '/home/patriot/pypr/desktopnotify/cube3.ico'

notify2.init("Notify me")
n = notify2.Notification('Notifying notificator', icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(5000)

n.update('Msg 4 U: ', 'hellllllllloooooo')
n.show()