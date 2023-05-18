
def get_path_upload_photo_workers(instance, file):
    """
    Построение пути к файлу format: (media)/photo_user/photo.format
    """
    return 'photo/{0}/{1}'.format(instance.id_photo, file)