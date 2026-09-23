"""A large check mark entering an open approval circle.
Construction: circle-check. None; the open ring and extended check are retained.
Keyshape CIRCLE; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c4f5ba1f-68f6-4541-ad2f-2718ffc31448'
SOURCE_PATH = 'icon_set/work/todo-references/food allegic vegan meal 2_c4f5ba1f-68f6-4541-ad2f-2718ffc31448.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'food-allegic-vegan-meal-2'
    keyshape = Keyshape.CIRCLE
    # Declared visible-ink extrema: (2, 2, 46, 46).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('food', 'allegic', 'vegan', 'meal', '2')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def build(self):

        # Plan: cardinal three-quarter circle plus an independently drawn check.
        self.add_arc('ring-top',(4,24),(24,4),radius_x=20)
        self.add_arc('ring-bottom',(24,44),(4,24),radius_x=20)
        self.add_arc('ring-right',(44,24),(24,44),radius_x=20)
        self.add_contour('ring','ring-right','ring-bottom','ring-top')
        self.add_polyline('check',(15,22),(24,32),(36,8))
