"""A left-pointing boot with an upward-right wing. Keep the boot toe, shaft and wing silhouette with two large feather divisions; omit the toe seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae6aea45-56ab-4362-b344-f9eaac8f45cb'
SOURCE_PATH = 'pictographic-primitives/religion/hermes boots_ae6aea45-56ab-4362-b344-f9eaac8f45cb.svg'
AUTHOR = 'gpt-6'

class WingedBoot(Solo48):
    icon_id = 'winged-boot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('boot', 'wing', 'hermes', 'footwear', 'feather', 'mythology')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42), left-pointing boot and right-rising wing.
        self.add_line('shaft-rim',(16,10),(8,14))
        self.add_line('shaft',(8,14),(14,28))
        self.add_arc('ankle',(14,28),(10,34),radius_x=7)
        self.add_arc('toe',(10,34),(10,42),radius_x=4,sweep=False)
        self.add_line('sole',(10,42),(28,36))
        self.add_arc('heel',(28,36),(30,28),radius_x=8,sweep=False)
        self.add_contour('boot','shaft-rim','shaft','ankle','toe','sole','heel')
        self.add_polyline('wing-leading',(14,28),(26,12),(42,6))
        self.add_arc('wing-tip',(42,6),(30,18),radius_x=12)
        self.add_arc('wing-lower',(30,18),(30,28),radius_x=5)
        self.add_contour('wing-trailing','wing-tip','wing-lower')
        self.add_line('feather',(30,18),(26,18))
        self.relate('connect','wing-leading','wing-trailing')
        self.relate('connect','wing-leading','boot')
        self.relate('connect','wing-trailing','boot')
        self.relate('connect','feather','wing-trailing')
