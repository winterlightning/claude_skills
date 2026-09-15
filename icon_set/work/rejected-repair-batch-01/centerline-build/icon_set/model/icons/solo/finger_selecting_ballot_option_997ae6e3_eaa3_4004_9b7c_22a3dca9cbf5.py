"""Raised index finger operates ballot choices; option rectangles reduced to strokes and thumb kept bent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '997ae6e3-eaa3-4004-9b7c-22a3dca9cbf5'
SOURCE_PATH = 'pictographic-primitives/school-learning/election online voting_997ae6e3-eaa3-4004-9b7c-22a3dca9cbf5.svg'
AUTHOR = 'gpt-6'


class FingerSelectingBallotOption(Solo48):
    icon_id = 'finger-selecting-ballot-option'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('finger', 'ballot', 'selection', 'vote', 'interface', 'election')

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

        self.add_polyline('option-box',(6,6),(14,6),(14,14),(6,14),closed=True)
        self.add_line('option-top',(24,10),(42,10))
        self.add_line('option-bottom',(32,24),(42,24))
        self.add_arc('fingertip',(14,27),(22,27),radius_x=4)
        self.add_polyline('hand-left',(14,27),(14,34),(6,30))
        self.add_polyline('hand-right',(22,27),(22,32),(31,35),(31,42))
        self.add_line('thumb',(6,30),(6,38))
        self.add_line('palm',(6,38),(10,42))
        self.relate('connect','thumb','palm')
        self.relate('connect','fingertip','hand-left')
        self.relate('connect','fingertip','hand-right')
        self.relate('connect','thumb','hand-left')
