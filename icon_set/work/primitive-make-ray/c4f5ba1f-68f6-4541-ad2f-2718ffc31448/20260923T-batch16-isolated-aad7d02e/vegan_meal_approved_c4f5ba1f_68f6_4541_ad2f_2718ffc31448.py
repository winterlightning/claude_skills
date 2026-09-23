"""Circular approval mark with a rising check.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape CIRCLE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: No semantic elements omitted.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c4f5ba1f-68f6-4541-ad2f-2718ffc31448'
SOURCE_PATH='icon_set/work/todo-references/food allegic vegan meal 2_c4f5ba1f-68f6-4541-ad2f-2718ffc31448.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vegan-meal-approved'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('food', 'allegic', 'vegan', 'meal', '2')

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

        self.add_arc('ring',(24,4),(44,24),radius_x=20,large_arc=True,sweep=False)
        self.add_polyline('check',(14,22),(24,32),(36,8))

