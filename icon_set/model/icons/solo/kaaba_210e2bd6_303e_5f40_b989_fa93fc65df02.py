"""The Kaaba seen at a front corner, with a band wrapping around two walls. Lucide box informs shared corner nodes; preserve the building silhouette and upper band."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '210e2bd6-303e-5f40-b989-fa93fc65df02'
SOURCE_PATH = 'pictographic-primitives/religion/islamic kaaba_210e2bd6-303e-5f40-b989-fa93fc65df02.svg'
AUTHOR = 'gpt-6'

class Kaaba(Solo48):
    icon_id = 'kaaba'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('kaaba', 'islam', 'building', 'mecca', 'cube', 'shrine')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (8,4)-(40,44), mirrored walls around corner x=24.
        self.add_polyline('outline',(24,4),(40,9),(40,19),(40,39),(24,44),(8,39),(8,19),(8,9),closed=True)
        self.add_polyline('band',(8,19),(24,14),(40,19))
        self.add_line('corner',(24,14),(24,44))
        self.relate('connect','outline','band');self.relate('connect','outline','corner');self.relate('connect','band','corner')
