"""Speech-bubble roundel enclosing a reduced camera and lens; rounded camera shoulder owns the lens spacing; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ebd83bf-e427-4d49-ad4c-1a39e24b1006'
SOURCE_PATH = 'pictographic-primitives/logos/dailybooth logo_4ebd83bf-e427-4d49-ad4c-1a39e24b1006.svg'
AUTHOR = 'gpt-6'

class DailyboothLogo(Solo48):
    icon_id = 'dailybooth-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('dailybooth', 'camera', 'photo', 'logo', 'brand', 'social', 'speech-bubble')

    def build(self):
        from ._symmetry_curves import poly
        # A camera aperture inside the original speech-balloon concept.
        poly(self,'bubble',(6,6),(42,6),(42,42),(30,38),(6,38),closed=True)
        poly(self,'camera',(14,14),(34,14),(34,30),(14,30),closed=True)
        self.add_dot('aperture',(24,22))
