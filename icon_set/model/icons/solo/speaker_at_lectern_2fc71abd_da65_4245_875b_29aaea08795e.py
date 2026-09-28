"""Lucide user-round: small circular head and arched shoulders; tapered lectern retained, small plaque omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fc71abd-da65-4245-875b-29aaea08795e'
SOURCE_PATH = 'pictographic-primitives/school-learning/election speech_2fc71abd-da65-4245-875b-29aaea08795e.svg'
AUTHOR = 'gpt-6'


class SpeakerAtLectern(Solo48):
    icon_id = 'speaker-at-lectern'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "school-learning"
    categories = ("school-learning", "primitives")
    aliases = ()
    keywords = ('speaker', 'lectern', 'podium', 'speech', 'person', 'presentation')

    def circle(self, name, x, y, r):
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        ids=[]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(j)
            self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def bust(self, name, x, y, r=2, width=5):
        self.circle(name+'-head',x,y,r)
        self.add_arc(name+'-sl',(x-width,y+7),(x,y+r),radius_x=width,radius_y=7-r)
        self.add_arc(name+'-sr',(x,y+r),(x+width,y+7),radius_x=width,radius_y=7-r)
        self.add_contour(name+'-shoulders',name+'-sl',name+'-sr')
        self.relate('connect',name+'-head',name+'-shoulders')

    def build(self) -> None:
        # Bounds are derived from the live SOLO48 contract, not the stale skill table.

        self.circle('head',24,7,3)
        self.add_arc('shoulders',(14,28),(34,28),radius_x=10,radius_y=8)
        self.add_polyline('ledge',(8,28),(14,28),(34,28),(40,28))
        self.add_polyline('lectern',(14,28),(17,44),(31,44),(34,28))
        self.relate('connect','shoulders','ledge')
        self.relate('connect','lectern','ledge')
        self.relate('connect','shoulders','lectern')
