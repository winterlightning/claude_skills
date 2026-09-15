'Palette: one smooth asymmetric contour, with a broad flowing grip and three paint marks. Lucide palette informs tangent-continuous bowl and grip.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013'
SOURCE_PATH = 'icons-json/design/palette_bbefdc9a-3d87-4d40-aa0f-2e2fa5ec2013.json'
AUTHOR = 'gpt-6'

class Palette(Solo48):
    icon_id = 'palette'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('palette', 'design')

    def build(self) -> None:
        # Lucide palette: smooth outer bowl and broad inward thumb transition.
        # Intentional asymmetric grip; SQUARE extrema x=6/42, y=6/42.
        self.add_bezier('outline',(24,6),((34,6),(42,13),(42,22)),((42,28),(38,30),(32,30)),((26,30),(25,42),(18,42)),((11,42),(6,35),(6,27)),((6,15),(13,6),(24,6)))
        self.add_contour('body','outline',closed=True)
        self.add_dot('paint-left',(15,27))
        self.add_dot('paint-top',(20,16))
        self.add_dot('paint-right',(31,17))
