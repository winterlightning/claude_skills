# Variant of beetle-in-coiled-shell; parent file remains unchanged.
"""Beetle with six distinct legs and a wing seam inside an open, inward-curving shell. SOLO48 SQUARE; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e6e35530-888b-4ddb-ab14-ab2f3f1591c8'
SOURCE_PATH = 'pictographic-primitives/animals/insect earth_e6e35530-888b-4ddb-ab14-ab2f3f1591c8.svg'
AUTHOR = 'gpt-6'

class BeetleInCoiledShellVariant2(Solo48):
    icon_id = 'beetle-in-coiled-shell-v2'
    variant_of = 'beetle-in-coiled-shell'
    variant_label = 'Roomier spacing — review 01'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('insect', 'beetle', 'shell', 'coil', 'spiral', 'cocoon', 'bug', 'nest')

    def build(self):
        # Open shell on the CIRCLE keyshape, centerline radius 20.
        self.add_arc('shell-top',(24,6),(42,24),radius_x=20)
        self.add_arc('shell-bottom',(42,24),(24,42),radius_x=20)
        self.add_arc('shell-left',(24,42),(6,24),radius_x=20)
        self.add_contour('shell','shell-top','shell-bottom','shell-left')
        self.add_arc('head-a',(22,20),(26,20),radius_x=2)
        self.add_arc('head-b',(26,20),(22,20),radius_x=2)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('body-top',(22,22),(26,22))
        self.add_arc('body-ne',(26,22),(28,24),radius_x=2)
        self.add_line('body-right-a',(28,24),(28,26))
        self.add_line('body-right-b',(28,26),(28,30))
        self.add_arc('body-se',(28,30),(26,32),radius_x=2)
        self.add_line('body-bottom',(26,32),(22,32))
        self.add_arc('body-sw',(22,32),(20,30),radius_x=2)
        self.add_line('body-left-a',(20,30),(20,26))
        self.add_line('body-left-b',(20,26),(20,24))
        self.add_arc('body-nw',(20,24),(22,22),radius_x=2)
        self.add_contour('body','body-top','body-ne','body-right-a','body-right-b','body-se','body-bottom','body-sw','body-left-a','body-left-b','body-nw',closed=True)
        self.relate('connect','head','body')
        for side in (-1,1):
            x=lambda n:24+side*n
            self.add_line(f'antenna-{side}',(x(2),20),(x(3),14))
            self.relate('connect','head',f'antenna-{side}')
            for label,start,end in [('top',(x(4),24),(x(7),18)),('middle',(x(4),26),(x(9),26)),('bottom',(x(4),30),(x(6),34))]:
                name=f'leg-{side}-{label}'
                self.add_line(name,start,end)
                self.relate('connect','body',name)
