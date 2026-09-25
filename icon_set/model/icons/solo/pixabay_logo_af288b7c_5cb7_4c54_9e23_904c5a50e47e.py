"""Camera in front of an angled photo; intrinsic photo/camera subject. Lucide camera informs lens and stepped body; omit tiny indicator."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af288b7c-5cb7-4c54-9e23-904c5a50e47e'
SOURCE_PATH = 'pictographic-primitives/logos/pixabay logo_af288b7c-5cb7-4c54-9e23-904c5a50e47e.svg'
AUTHOR = 'gpt-6'

class PixabayLogo(Solo48):
    icon_id = 'pixabay-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('pixabay', 'camera', 'photos', 'stock', 'logo', 'brand', 'images')

    def build(self):
        # Plan: Camera in front of an angled photo; intrinsic photo/camera subject. Lucide camera informs lens and stepped body; omit tiny indicator.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('camera',(6,42),(6,18),(12,18),(12,14),(20,14),(20,18),(32,18),(32,42),closed=True)
        circle('lens',19,30,3)
        self.add_polyline('photo',(24,6),(42,12),(41,36))

