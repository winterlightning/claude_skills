"""Hand-authored 4WD drivetrain lettering.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape HRECT_M; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: None; all three characters retained.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1dfab6f7-a053-5aee-8d2b-b99c63e6f3df'
SOURCE_PATH = 'pictographic-primitives/transportation/four wheel drive_1dfab6f7-a053-5aee-8d2b-b99c63e6f3df.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='four-wheel-drive'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('four', 'wheel', 'drive')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, w, h, r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}';ids.append(eid)
            if i%2:self.add_arc(eid,pts[i],pts[(i+1)%8],radius_x=r)
            else:self.add_line(eid,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        self.add_polyline('four',(4,10),(4,28),(12,28),(12,10))
        self.add_line('four-stem',(12,28),(12,38));self.relate('connect','four','four-stem')
        self.add_polyline('w',(20,10),(20,38),(25,30),(30,38),(30,10))
        self.add_line('d-stem',(39,10),(39,38))
        self.add_arc('d-bowl',(39,10),(39,38),radius_x=5,radius_y=14)
        self.relate('connect','d-stem','d-bowl')

