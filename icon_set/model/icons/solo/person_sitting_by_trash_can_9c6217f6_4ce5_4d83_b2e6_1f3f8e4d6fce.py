"""A bowed person sits with knees drawn up beside a lidded bin. Lucide person-standing informs reduced limbs; no useful exact seated-scene match. Bin ribs, fingers, and extra clothing folds are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce'
SOURCE_PATH = 'pictographic-primitives/users/user homeless poverty_9c6217f6-4ce5-4d83-b2e6-1f3f8e4d6fce.svg'
AUTHOR = 'gpt-6'


class PersonSittingByTrashCan(Solo48):
    icon_id = 'person-sitting-by-trash-can'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/users"
    aliases = ()
    keywords = ('homeless', 'poverty', 'person', 'sitting', 'trash', 'bin', 'street', 'despair')

    def circle(self,name,cx,cy,r):
        pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        ids=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            eid=name+'-'+str(i);self.add_arc(eid,a,b,radius_x=r);ids.append(eid)
        self.add_contour(name,*ids,closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); person right, bin left.
        self.circle('head',34,12,6)
        self.add_arc('back',(32,27),(42,37),radius_x=10)
        self.add_line('back-low',(42,37),(42,42))
        self.add_line('seat',(42,42),(34,42))
        self.add_contour('seated-back','back','back-low','seat')
        self.add_polyline('legs',(34,42),(30,33),(25,42))
        self.add_polyline('arms',(32,27),(26,31),(30,33))
        self.relate('connect','seated-back','legs')
        self.relate('connect','seated-back','arms')
        self.relate('connect','arms','legs')
        self.add_polyline('bin',(6,24),(8,42),(16,42),(18,24))
        self.add_polyline('lid',(6,24),(12,24),(18,24))
        self.add_line('lid-handle',(12,18),(12,24))
        self.relate('connect','bin','lid')
        self.relate('connect','lid','lid-handle')
