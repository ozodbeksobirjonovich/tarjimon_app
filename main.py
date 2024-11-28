from pytarjimon import tarjima

def tarjima_qilish(matn, til):
    return tarjima(text=matn, language=til)

x = tarjima_qilish(matn="Salom! Hamma ishlaringiz yaxshimi?", til="ko")
print(x)