"""Redraw the crescent as two tangent circular arcs with generous middle width and clear rounded tips. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1f947813-75bf-523b-bb36-5f6abbd3d57b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crescent-moon/20260927T032242Z-thuan-mac-1/reference/astrology moon_1f947813-75bf-523b-bb36-5f6abbd3d57b.svg'
AUTHOR = "gpt-6"

class CrescentMoon(Solo48):
    icon_id = 'crescent-moon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('moon', 'crescent', 'lunar', 'night', 'astrology', 'symbol', 'sky', 'phase')

    def build(self) -> None:
        # Two broad nested bows meet at pointed upper and lower tips.
        self.add_bezier('outer-upper',(6,6),((24,6),(42,12),(42,24)))
        self.add_bezier('outer-lower',(42,24),((42,36),(24,42),(6,42)))
        self.add_bezier('inner-lower',(6,42),((24,38),(30,31),(30,24)))
        self.add_bezier('inner-upper',(30,24),((30,17),(24,10),(6,6)))
        self.add_contour('crescent','outer-upper','outer-lower','inner-lower','inner-upper',closed=True)

