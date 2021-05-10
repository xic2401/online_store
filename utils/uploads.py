import uuid

def upload_instance(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return f'uploads/{instance.__class__.__name__}/{filename[2:3]}/{filename}'