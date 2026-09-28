"""A bust with a circular lower-right relationship badge.
Plan: SQUARE fits the large detached head, shoulders and badge.
Reduction: Neck detail omitted; lower hem shortened to leave clear space beside the badge.
Construction: human_ref/user.svg: round head and broad shoulders.
Layout: Head bottom centerline y22 and shoulder top y30 provide exactly four units of ink clearance. Badge deliberately occludes the right shoulder."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb0291a2-d110-4e0e-9cb6-552c49ef98d5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/step uncle_eb0291a2-d110-4e0e-9cb6-552c49ef98d5.svg'
AUTHOR = "gpt-6"
PLAN = 'Bald male bust with circular lower-right relationship badge.'
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: round head, broad shoulders, detached 4-unit ink gap'

class Drawing(Solo48):
    icon_id = 'step-uncle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('step', 'uncle')

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
        self.add_line('hem',(6,42),(21,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')

    def build(self):
        self.bust_body()
        self.circle('head',22,14,8)
        # Head bottom y=22; shoulder centerline y=30; ink gap=30-22-4=4.
