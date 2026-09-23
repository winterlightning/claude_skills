"""A standing person beside a location pin and street lines.
Plan: Left aligned figure, right pin, two road levels. Head radius 4; torso starts exactly 8 below its lower centerline.
Keyshape: SQUARE; extrema follow the profile contract.
References: supplied reference SVG; human_ref/user.svg and human_ref/full_body_ref.png: circular heads and smooth shoulders or limbs; lucide/original/map-pin.svg and atomic-debug/map-pin.svg: rounded crown and pointed base
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6498afd8-8355-4072-b42d-b96eef9111b1'
SOURCE_PATH = 'icon_set/work/todo-references/street view_6498afd8-8355-4072-b42d-b96eef9111b1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'street-view'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('street', 'view')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=4):
        # One owning rectangle; four equal tangent corner arcs.
        points = [(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                  (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,p,q,radius_x=r)
            else: self.add_line(n,p,q)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        # Four rays share the true intersection node.
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        ids=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));ids.append(n)
        for i,a in enumerate(ids):
            for b in ids[i+1:]: self.relate('connect',a,b)

    def build(self):

        self.circle('head',14,10,4)
        self.add_line('torso',(14,22),(14,32))
        self.add_polyline('arms',(6,30),(6,26),(10,22),(14,22),(18,22),(22,26),(22,30))
        self.add_polyline('legs',(8,42),(14,32),(20,42))
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_arc('pin-top',(28,14),(42,14),radius_x=7)
        self.add_polyline('pin-point',(42,14),(35,26),(28,14))
        self.add_contour('pin','pin-top','pin-point-1','pin-point-2',closed=True)
        self.add_dot('pin-hole',(35,13))
        self.add_line('road-near',(28,42),(42,42))
        self.add_line('road-far',(30,34),(40,34))
