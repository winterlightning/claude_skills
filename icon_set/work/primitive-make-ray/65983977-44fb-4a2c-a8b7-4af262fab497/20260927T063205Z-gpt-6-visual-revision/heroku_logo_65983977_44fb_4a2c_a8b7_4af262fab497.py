"""Fresh SOLO48 revision of heroku-logo from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '65983977-44fb-4a2c-a8b7-4af262fab497'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__heroku-logo/20260927T061852Z-thuan-mac-1/reference/heroku logo_65983977-44fb-4a2c-a8b7-4af262fab497.svg'
AUTHOR = "gpt-6"

class HerokuLogo(Solo48):
    icon_id = 'heroku-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('heroku', 'cloud', 'hosting', 'letter-h', 'logo', 'brand', 'platform')

    def build(self) -> None:

        box(self,'frame',6,6,42,42,4)
        poly(self,'h-stem',(16,15),(16,33))
        path(self,'h-shoulder',(16,25),('L',(28,25)),('A',4,4,True,(32,29)),('L',(32,33)))
        line(self,'leaf',(28,16),(32,15))
        contacts(self)
