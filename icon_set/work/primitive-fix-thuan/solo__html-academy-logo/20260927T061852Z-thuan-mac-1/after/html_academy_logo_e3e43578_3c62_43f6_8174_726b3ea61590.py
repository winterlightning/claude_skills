"""Fresh SOLO48 revision of html-academy-logo from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e3e43578-3c62-43f6-8174-726b3ea61590'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__html-academy-logo/20260927T061852Z-thuan-mac-1/reference/html academy logo_e3e43578-3c62-43f6-8174-726b3ea61590.svg'
AUTHOR = 'gpt-6'

class HtmlAcademyLogo(Solo48):
    icon_id = 'html-academy-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('html-academy', 'education', 'coding', 'logo', 'brand', 'web', 'course')

    def build(self) -> None:

        poly(self,'shield',(24,6),(42,9),(42,33),(24,42),(6,33),(6,9),closed=True)
        poly(self,'slab',(6,24),(24,14),(42,24),(24,30),closed=True)
        line(self,'spine',(24,30),(24,42))
        contacts(self)
