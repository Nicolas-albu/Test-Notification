import notify2

notify2.init("notification on desktop")

title_of_notification = str(input("Título da notificação: "))
text_of_notification = str(input("Texto da notificação: "))
interval_of_time_of_notification = str(input("Intervalo de tempo em segundos entre notificações: "))

notificator = notify2.Notification(f"{title_of_notification}", f"{text_of_notification}", "notification-message-im")
notificator.show()