"""food allegic vegan meal 1.
Paired peanut lobes flank the diagonal prohibition slash.
Square; reflected lobe geometry keeps more than8 centerline units from the slash.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='588d68f8-b31a-4c4c-97e2-20473cedb4a3'
SOURCE_PATH = 'pictographic-primitives/food/food allegic vegan meal 1_588d68f8-b31a-4c4c-97e2-20473cedb4a3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='food-allergen-free'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('food', 'allegic', 'vegan', 'meal', '1')

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

    def build(self) -> None:
        self.add_line('slash',(6,6),(42,42))
        self.add_arc('upper-lobe',(18,6),(34,22),radius_x=16)
        self.add_arc('upper-small-lobe',(34,22),(42,30),radius_x=8)
        self.add_contour('upper-peanut','upper-lobe','upper-small-lobe')
        self.add_arc('lower-lobe',(6,18),(22,34),radius_x=16,sweep=False)
        self.add_arc('lower-small-lobe',(22,34),(30,42),radius_x=8,sweep=False)
        self.add_contour('lower-peanut','lower-lobe','lower-small-lobe')

# Repair plan: Paired peanut lobes flank the diagonal prohibition slash.
# Omissions: Small shell marks omitted.
# Construction references: Supplied reference; no additional useful Lucide match used.
# Keyshape and proportions: Square; reflected lobe geometry keeps more than8 centerline units from the slash.
