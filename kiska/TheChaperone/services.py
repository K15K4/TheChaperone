
def photo_сar(instance, file):
    return 'photo_cars/{0}/{1}'.format(instance.id_Car, file)


def photo_mark(instance, file):
    return 'photo_mark/{0}/{1}'.format(instance.id_Car, file)
