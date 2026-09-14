"""Lucide square-pen informs diagonal pencil. Two ballot choices remain; cross retained; pencil tilted closer to vertical to open clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8baf23d7-4390-4407-a5c3-c22b45141f27'
SOURCE_PATH = 'pictographic-primitives/school-learning/election_8baf23d7-4390-4407-a5c3-c22b45141f27.svg'
AUTHOR = 'gpt-6'


class PencilMarkingBallot(Solo48):
    icon_id = 'pencil-marking-ballot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "society/elections"
    aliases = ()
    keywords = ('pencil', 'ballot', 'vote', 'cross', 'election', 'marking')

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

        self.add_polyline('empty-box',(6,6),(14,6),(14,14),(6,14),closed=True)
        self.add_polyline('marked-box',(6,22),(26,22),(26,42),(6,42),closed=True)
        self.add_line('cross-a',(14,30),(18,34))
        self.add_line('cross-b',(14,34),(18,30))
        self.relate('connect','cross-a','cross-b')
        self.add_polyline('pencil',(37,26),(33,17),(34,6),(42,8),(40,19),closed=True)
