"""A stern devil face with paired horns and a rounded jaw. Omit separate ears and lip outlines; preserve horns, slanted eyes and frown; round the chin for mouth clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a9464dc-1290-56cf-b8d5-c118466dbc1a'
SOURCE_PATH = 'pictographic-primitives/religion/devil head_6a9464dc-1290-56cf-b8d5-c118466dbc1a.svg'
AUTHOR = 'gpt-6'


class HornedDevilFace(Solo48):
    icon_id = 'horned-devil-face'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('devil', 'horn', 'face', 'demon', 'ear', 'scowl')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Live VRECT envelope: centerline (8,4)-(40,44).
        self.add_polyline('crown',(8,18),(8,4),(16,12),(32,12),(40,4),(40,18))
        self.add_arc('jaw',(40,18),(8,18),radius_x=16,radius_y=26)
        self.relate('connect','crown','jaw')
        for side in (-1,1):
            self.add_line('eye-'+str(side),(24+side*7,22),(24+side*4,23))
        self.add_arc('frown',(20,32),(28,32),radius_x=6)
