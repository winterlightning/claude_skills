"""Two peanut kernels crossed by an allergy prohibition slash.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Small secondary veins omitted to reduce crowding.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='588d68f8-b31a-4c4c-97e2-20473cedb4a3'
SOURCE_PATH='icon_set/work/todo-references/food allegic vegan meal 1_588d68f8-b31a-4c4c-97e2-20473cedb4a3.svg'
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

    def build(self):

        self.add_line('slash',(6,6),(42,42))
        self.add_bezier('upper-leaves',(18,10),((22,0),(38,6),(32,20)),((45,13),(46,28),(38,30)))
        self.add_bezier('lower-leaves',(10,18),((0,22),(6,38),(20,32)),((13,45),(28,46),(30,38)))
        self.add_line('vein-upper',(24,16),(27,13))
        self.add_line('vein-lower',(13,27),(16,24))

