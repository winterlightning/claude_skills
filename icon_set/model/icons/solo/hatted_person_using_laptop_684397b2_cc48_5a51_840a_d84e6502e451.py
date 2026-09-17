"""Hatted Person Using Laptop.

Symbol plan: Mirror hat and face about x24, head lower extreme20 and shoulders28 for detached ink gap4. Laptop occludes lower torso. Centerline extremes (8,4)-(40,44).
References: original SOURCE_PATH; Lucide pencil/gavel/hat-glasses for coherent
outlines and shared attachment nodes; human_ref/user.svg for circular heads
and rounded shoulders. Omit tiny decorative face, emblem and robe marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '684397b2-cc48-5a51-840a-d84e6502e451'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/hacker laptop_684397b2-cc48-5a51-840a-d84e6502e451.svg'
AUTHOR = 'gpt-6'

class HattedPersonUsingLaptop(Solo48):
    icon_id = 'hatted-person-using-laptop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('hatted', 'person', 'using', 'laptop')

    def build(self):
        axis=24
        self.add_polyline('hat',(16,12),(18,4),(30,4),(32,12))
        self.add_polyline('brim',(10,12),(16,12),(32,12),(38,12))
        self.relate('connect','hat','brim')
        self.add_arc('face',(32,12),(16,12),radius_x=8)
        self.relate('connect','face','brim')
        self.relate('connect','face','hat')
        self.add_arc('shoulder-left',(16,36),(24,28),radius_x=8)
        self.add_arc('shoulder-right',(24,28),(32,36),radius_x=8)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.add_polyline('laptop',(8,36),(16,36),(32,36),(40,36),(38,44),(10,44),closed=True)
        self.relate('connect','shoulders','laptop')
