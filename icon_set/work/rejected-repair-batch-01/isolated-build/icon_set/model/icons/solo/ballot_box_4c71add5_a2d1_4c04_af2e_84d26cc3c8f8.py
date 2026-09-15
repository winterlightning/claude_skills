"""Blank slip entering a broad box; front-view construction omits shallow perspective top."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c71add5-a2d1-4c04-af2e-84d26cc3c8f8'
SOURCE_PATH = 'pictographic-primitives/school-learning/election 1_4c71add5-a2d1-4c04-af2e-84d26cc3c8f8.svg'
AUTHOR = 'gpt-6'


class BallotBox(Solo48):
    icon_id = 'ballot-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('ballot', 'box', 'vote', 'election', 'poll', 'democracy')

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

        self.add_polyline('box',(8,26),(8,44),(40,44),(40,26),(32,26))
        self.add_line('lid-left',(8,26),(16,26))
        self.relate('connect','box','lid-left')
        self.add_polyline('ballot',(16,26),(20,4),(36,4),(32,26),(16,26))
        self.relate('connect','box','ballot')
        self.relate('connect','lid-left','ballot')
