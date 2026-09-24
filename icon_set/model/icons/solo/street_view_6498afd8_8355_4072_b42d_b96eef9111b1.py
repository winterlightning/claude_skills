"""A standing person beside a map pin and road lines.
Plan: SQUARE fits the left figure and upper-right pin.
Reduction: Body reduced to a stick figure; arms raised and legs opened to separate the limbs.
Construction: human_ref/full_body_ref.png: outlined head and coherent limbs; source map pin.
Layout: Marked person: head bottom y14, torso start y22, exactly four units of detached head-body ink gap. Pin and road sit to the right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6498afd8-8355-4072-b42d-b96eef9111b1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_36/street view_6498afd8-8355-4072-b42d-b96eef9111b1.svg'
AUTHOR = "gpt-6"
PLAN = 'Standing person beside a map pin and short road line.'
CONSTRUCTION_REFERENCE = 'human_ref/full_body_ref.png and map-pin: outlined head, connected limbs, pointed marker'

class Drawing(Solo48):
    icon_id = 'street-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('street', 'view')

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
        self.add_line('hem',(6,42),(36,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','hem','badge-lower')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')

    def build(self):
        # Human reference: outlined head, coherent torso and round-ended limbs.
        self.circle('head',12,10,4)
        self.add_line('torso',(12,22),(12,32))
        self.add_polyline('arms',(6,26),(12,22),(18,26))
        self.add_polyline('legs',(6,42),(12,32),(20,42))
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Exact emitted gap: torso 22 - head bottom 14 - stroke 4 = 4 ink units.
        self.add_arc('pin-top',(24,15),(42,15),radius_x=9)
        points=[(42,15),(42,18),(33,26),(24,18),(24,15)]
        for j in range(4): self.add_line(f'pin-edge-{j}',points[j],points[j+1])
        self.add_contour('pin','pin-top',*[f'pin-edge-{j}' for j in range(4)],closed=True)
        self.add_dot('pin-center',(33,15))
        self.add_line('road',(33,34),(42,34))
        self.add_line('ground',(6,42),(42,42))
        self.relate('connect','ground','legs')
