from pytarjimon import tarjima

def tarjima_qilish(matn, til):
    return tarjima(text=matn, language=til)

x = tarjima_qilish(matn="Ushbu dastur yordamida siz so'zlarni istalgan tilga tarjima qila olishingiz mumkin!", til="ru")
print(x)