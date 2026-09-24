"""A young-person bust with a circular relationship badge.
Repair plan: Removed small hair pocket; shortened hem clears badge. Head center (22,14), radius 8, shoulders y=30 give exactly 4 units of detached ink gap.
Omissions: Interior hairline and neck; detached head follows human reference.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cd254b93-0bc0-4673-bae6-ab625d673425'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/step son_cd254b93-0bc0-4673-bae6-ab625d673425.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'step-son'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('step', 'son')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-upper', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-lower', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, left, top, right, bottom, r):
        # One rounded rectangle definition owns all matching corners.
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8]; member=f'{name}-{i}'
            if i%2: self.add_arc(member,start,end,radius_x=r)
            else: self.add_line(member,start,end)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        ends = [(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):
            self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def bust_body(self):
        # Shared shoulder radii; badge occludes the right shoulder and hem.
        self.add_line('body-left',(6,42),(6,40))
        self.add_arc('shoulder-left',(6,40),(16,30),radius_x=10)
        self.add_line('shoulder-top',(16,30),(24,30))
        self.add_arc('shoulder-right',(24,30),(30,36),radius_x=6)
        self.add_contour('shoulders','body-left','shoulder-left','shoulder-top','shoulder-right')
        self.add_line('hem',(6,42),(23,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')

    def build(self):
        self.bust_body()
        self.circle('head',22,14,8)
        # Head bottom y=22, own shoulders y=30: exactly 4 units of ink gap.
