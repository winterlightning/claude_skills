"""pantyhose: standalone SOLO48 repair.
Plan: Stockinged legs, one bent across the other.
Keyshape: VRECT_L; shared dimensions and nodes own repeated elements.
Reduction: Widened bent calf, rebalanced the rear shin, and omitted fine wrinkles. Asymmetric crossing pose preserved.
Lucide originals and atomic-debug construction reference: none.
human_ref/full_body_ref.png informs coherent bent limb anatomy. No head; detached-head rule does not apply.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f422872b-42cf-4b74-aa1f-bf870f557d7a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pantyhose/20260927T143814Z-thuan-mac-1/reference/pantyhose_f422872b-42cf-4b74-aa1f-bf870f557d7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pantyhose'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('pantyhose',)

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
        self.add_contour(name,*members,closed=True)

    def letter_p(self, name, x, y, w, h):
        # Stem and semicircular bowl share explicit shoulder nodes.
        mid=y+h//2; rr=h//4
        self.add_polyline(name+'-stem',(x,y+h),(x,mid),(x,y),(x+w-rr,y))
        self.add_arc(name+'-bowl',(x+w-rr,y),(x+w-rr,mid),radius_x=rr)
        self.add_line(name+'-return',(x+w-rr,mid),(x,mid))
        self.relate('connect',name+'-stem',name+'-bowl')
        self.relate('connect',name+'-bowl',name+'-return')
        self.relate('connect',name+'-return',name+'-stem')

    def build(self):
        # One waistband and two separated full-length hosiery legs.
        self.add_polyline('tights',(14,4),(34,4),(40,14),(40,44),(30,44),(30,18),
                          (18,18),(18,44),(8,44),(8,14),closed=True)

# Revision comparison: The rejected drawing read as a single tangled bent leg rather than a pair of hosiery legs.
# Revision: Redrew one waistband with two long, separated legs.
