"""Beetle with six distinct legs and a wing seam inside an open, inward-curving shell. SOLO48 SQUARE; extremes (2,2)-(46,46)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6e35530-888b-4ddb-ab14-ab2f3f1591c8'
SOURCE_PATH = 'pictographic-primitives/animals/insect earth_e6e35530-888b-4ddb-ab14-ab2f3f1591c8.svg'
AUTHOR = 'gpt-6'


class BeetleInCoiledShell(Solo48):
    icon_id = 'beetle-in-coiled-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('insect', 'beetle', 'shell', 'coil', 'spiral', 'cocoon', 'bug', 'nest')

    def build(self) -> None:
        # Open spiral wraps a larger beetle with six legs and a clear wing seam.
        self.add_arc('shell-crown', (24,2), (46,24), radius_x=22)
        self.add_arc('shell-base', (46,24), (24,46), radius_x=22)
        self.add_arc('shell-left', (24,46), (2,24), radius_x=22)
        self.add_arc('shell-curl', (2,24), (14,12), radius_x=12)
        self.add_contour('shell', 'shell-crown', 'shell-base', 'shell-left', 'shell-curl')
        self.add_arc('head-a', (24,18),(27,21),radius_x=3)
        self.add_arc('head-b', (27,21),(24,24),radius_x=3)
        self.add_arc('head-c', (24,24),(21,21),radius_x=3)
        self.add_arc('head-d', (21,21),(24,18),radius_x=3)
        self.add_contour('head','head-a','head-b','head-c','head-d',closed=True)
        self.add_line('body-top-1',(21, 24),(24, 24))
        self.add_line('body-top-2',(24, 24),(27, 24))
        self.add_arc('corner-tr',(27,24),(30,27),radius_x=3)
        self.add_line('side-r-1',(30, 27),(30, 31))
        self.add_line('side-r-2',(30, 31),(30, 35))
        self.add_arc('corner-br',(30,35),(27,38),radius_x=3)
        self.add_line('body-bottom-1',(27, 38),(24, 38))
        self.add_line('body-bottom-2',(24, 38),(21, 38))
        self.add_arc('corner-bl',(21,38),(18,35),radius_x=3)
        self.add_line('side-l-1',(18, 35),(18, 31))
        self.add_line('side-l-2',(18, 31),(18, 27))
        self.add_arc('corner-tl',(18,27),(21,24),radius_x=3)
        self.add_contour('body','body-top-1','body-top-2','corner-tr','side-r-1','side-r-2','corner-br','body-bottom-1','body-bottom-2','corner-bl','side-l-1','side-l-2','corner-tl',closed=True)
        self.relate('connect','head','body')
        self.add_line('seam',(24,24),(24,38))
        self.relate('connect','body','seam')
        for side in (-1,1):
            label='left' if side<0 else 'right'
            self.add_line('antenna-'+label,(24+side*3,21),(24+side*4,14))
            self.relate('connect','head','antenna-'+label)
            self.add_line('leg-top-'+label,(24+side*6,27),(24+side*11,23))
            self.add_line('leg-mid-'+label,(24+side*6,31),(24+side*13,31))
            self.add_line('leg-low-'+label,(24+side*6,35),(24+side*7,37))
            for row in ('top','mid','low'):
                self.relate('connect','body','leg-'+row+'-'+label)
