"""An Egyptian eye with a pupil, descending mark and sweeping cheek line. The Lucide eye informs the smooth almond contour. Omit the separate brow and iris to preserve a clear pupil at native size."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47736496-ebae-4a72-9ecf-0abb894a8255'
SOURCE_PATH = 'pictographic-primitives/religion/eye mythology_47736496-ebae-4a72-9ecf-0abb894a8255.svg'
AUTHOR = 'gpt-6'


class EgyptianMythologicalEye(Solo48):
    icon_id = 'egyptian-mythological-eye'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    categories = ("primitives", "religion")
    aliases = ()
    keywords = ('eye', 'egyptian', 'mythology', 'iris', 'pupil', 'eyebrow', 'symbol')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Almond-eye silhouette, exact live HRECT centerline box (4,8)-(44,40).
        self.add_arc('lid-top',(4,20),(44,20),radius_x=25,radius_y=30)
        self.add_arc('lid-bottom-right',(44,20),(24,32),radius_x=25,radius_y=30)
        self.add_arc('lid-bottom-left',(24,32),(4,20),radius_x=25,radius_y=30)
        self.add_contour('eye','lid-top','lid-bottom-right','lid-bottom-left',closed=True)
        self.add_dot('pupil',(24,20))
        self.add_line('tear',(44,20),(44,40))
        self.relate('connect','eye','tear')
        self.add_arc('flourish',(24,32),(12,40),radius_x=18)
        self.relate('connect','eye','flourish')
