"""Hera in a robe holding a scepter with a round finial. Lucide user-round informs the portrait hierarchy; keep long hair and held staff, omit folds and fingers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3cc211c-c349-5d3c-aa71-4240df4f9762'
SOURCE_PATH = 'pictographic-primitives/religion/hera_f3cc211c-c349-5d3c-aa71-4240df4f9762.svg'
AUTHOR = 'gpt-6'

class HeraHoldingScepter(Solo48):
    icon_id = 'hera-holding-scepter'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('hera', 'goddess', 'scepter', 'greek', 'mythology', 'figure')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44); held scepter is deliberately rightward.
        self.oval('head',16,11,7)
        self.add_line('hair',(9,11),(8,20));self.relate('connect','head','hair')
        self.add_polyline('gown',(13,27),(8,44),(27,44),(25,34),(23,27),(13,27))
        self.add_line('arm',(25,34),(37,34));self.relate('connect','arm','gown')
        self.oval('finial',37,7,3)
        self.add_polyline('scepter',(37,10),(37,34),(37,44))
        self.relate('connect','scepter','finial');self.relate('connect','scepter','arm')
