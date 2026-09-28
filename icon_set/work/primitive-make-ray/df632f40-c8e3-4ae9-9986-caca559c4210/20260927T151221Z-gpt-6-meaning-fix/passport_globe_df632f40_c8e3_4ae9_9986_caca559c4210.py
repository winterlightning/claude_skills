"""passport globe.
Rounded passport with a divided circular globe emblem and a partial background globe.
Square accommodates offset objects. Rounded cover clears the background arc; globe diameter12 keeps both enclosed halves open.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df632f40-c8e3-4ae9-9986-caca559c4210'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__passport-globe/20260927T143814Z-thuan-mac-1/reference/passport globe_df632f40-c8e3-4ae9-9986-caca559c4210.svg'
AUTHOR = "gpt-6"
PLAN = 'Rounded passport with a divided circular globe emblem and a partial background globe.'
CONSTRUCTION_REFERENCES = 'No additional useful local Lucide match used for this revision.'
OMISSIONS = 'Background continent and globe meridians omitted; one equator retained.'

class Drawing(Solo48):
    icon_id = 'passport-globe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('passport', 'globe')

    def circle(self, name, cx, cy, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=3):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; members.append(part)
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
        for j in range(len(members)):
            self.relate('connect',members[j],members[(j+1)%len(members)])

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self) -> None:
        self.add_arc('world-top',(6,20),(20,6),radius_x=14)
        self.add_line('world-side',(6,20),(6,28))
        self.relate('connect','world-top','world-side')
        self.add_arc('world-bottom',(6,28),(14,34),radius_x=8,radius_y=6,sweep=False)
        self.relate('connect','world-bottom','world-side')
        self.box('passport',14,14,28,28,8)
        self.relate('connect','world-bottom','passport-5')
        self.circle('globe',28,28,6)
        self.add_line('equator',(22,28),(34,28))
        self.relate('connect','globe','equator')

# Repair plan: Rounded passport with a divided circular globe emblem and a partial background globe.
# Omissions: Background continent and globe meridians omitted; one equator retained.
# Construction references: No additional useful local Lucide match used for this revision.
# Keyshape and proportions: Square accommodates offset objects. Rounded cover clears the background arc; globe diameter12 keeps both enclosed halves open.

# Revision comparison: The background globe in the rejected drawing stopped as an open hook.
# Revision: Continued the globe outline behind the passport to restore the two-object arrangement.
