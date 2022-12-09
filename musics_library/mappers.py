from musics_library.domain import Music,ID,Name,Artist,RecordCompany,Genre,EANCode,Username,Price
from dateutil import parser
import musics_library.services as services


class MusicMapper:
    @staticmethod
    def map_cd(res):
        created_at = parser.parse(res['created_at'])
        updated_at = parser.parse(res['updated_at'])
        cd = Music( \
            id=ID(res['id']), \
            name=Name(res['name']), \
            artist=Artist(res['artist']), \
            record_company=RecordCompany(res['record_company']), \
            genre=Genre(res['genre']), \
            ean_code=EANCode(res['ean_code']), \
            published_by=Username(res['user']), \
            price=Price.parse(res['price']), \
            created_at=created_at, \
            updated_at=updated_at
        )
        return cd

class AuthenticatedUserMapper:
    @staticmethod
    def map_auth_user(res):
        return services.AuthenticatedUser(res.json()["key"], ID(res.json()['user']['id']),
                                 Username(res.json()['user']['username']))