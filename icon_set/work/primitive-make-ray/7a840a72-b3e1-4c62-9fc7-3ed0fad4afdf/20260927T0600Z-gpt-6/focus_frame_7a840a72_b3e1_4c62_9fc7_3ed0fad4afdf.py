'focus-frame: independent smooth-curve repair.\n\nConstruction: Square frame around a smaller square; identical circular corner geometry.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/square.svg and atomic-debug/square.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__focus-frame/20260927T055558Z-thuan-mac-1/reference/focus frame_7a840a72-b3e1-4c62-9fc7-3ed0fad4afdf.svg'
AUTHOR = "gpt-6"


class FocusFrame(Solo48):
    icon_id = 'focus-frame'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('focus', 'frame', 'photography')
    keyshape = Keyshape.SQUARE

    def build(self) -> None:
        # Four mirrored open brackets, rounded only at the outer corners.
        specs=[('tl',(16,6),(10,6),(6,10),(6,16),False),('tr',(32,6),(38,6),(42,10),(42,16),True),('br',(42,32),(42,38),(38,42),(32,42),True),('bl',(16,42),(10,42),(6,38),(6,32),True)]
        for name,a,b,c,d,sweep in specs:
            self.add_line(name+'-a',a,b)
            self.add_arc(name+'-corner',b,c,radius_x=4,radius_y=4,sweep=sweep)
            self.add_line(name+'-b',c,d)
            self.add_contour(name,name+'-a',name+'-corner',name+'-b')

