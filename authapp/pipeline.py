from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_max_orig')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex'] == 2:
        user.shopuserprofile.gender = ShopUserProfile.MALE
    elif data['sex'] == 1:
        ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['photo_max_orig']:
        photo_link = data['photo_max_orig']
        photo_response = requests.get(photo_link)
        user_photo_path = f'users_avatars/{user.pk}.jpg'
        with open(f'media/{user_photo_path}', 'wb') as photo_file:
            photo_file.write(photo_response.content)
        user.avatar = user_photo_path

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().date().year - bdate.year
        if age < 18:
            # shopuserprofiles = ShopUserProfile.objects.filter(user=user)
            # for shopuserprofile in shopuserprofiles:
            #     shopuserprofile.delete()
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.age = age
    user.save()
