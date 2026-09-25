"""Skull with Crossed Bones — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb0c2575-3757-4901-bb6b-1d9b04b3a433'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/skull_bb0c2575-3757-4901-bb6b-1d9b04b3a433.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'skull-with-crossed-bones'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('skull', 'with', 'crossed', 'bones')

    def build(self):
        # Plan: mirrored cranium and jaw with two eye dots and four bone ends.
        # SQUARE extrema (6,6)-(42,42). Lucide skull guides the jaw silhouette.
        # Human user.svg reviewed; skull has no torso or detached head/body gap.
        self.add_bezier('crown',(14,14),((19,9),(29,9),(34,14)))
        self.add_bezier('right-cheek',(34,14),((38,18),(40,29),(32,32)))
        self.add_polyline('jaw',(32,32),(32,38),(24,38),(16,38),(16,32))
        self.add_bezier('left-cheek',(16,32),((8,29),(10,18),(14,14)))
        self.contours.pop()
        self.add_contour('skull','crown','right-cheek',*[f'jaw-{i}' for i in range(1,5)],'left-cheek',closed=True)
        for side in (-1,1):
            self.add_dot('eye-'+str(side),(24+side*5,23))
            for lower in (False,True):
                n=f'bone-{side}-{lower}'
                start=(24+side*8,32) if lower else (24+side*10,14)
                self.add_line(n,start,(24+side*18,42 if lower else 6))
                self.relate('connect',n,'skull')
        self.add_line('tooth',(24,30),(24,38))
        self.relate('connect','tooth','skull')

    def rectangle(self, name, x, y, w, h, attachments=()):
        # Split receiving edges at actual attachment nodes; one joined contour.
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
        nodes=[]
        for start,end in zip(corners,corners[1:]+corners[:1]):
            dx,dy=end[0]-start[0],end[1]-start[1]
            inside=[p for p in attachments if (p[0]-start[0])*dy == (p[1]-start[1])*dx
                    and 0 < (p[0]-start[0])*dx+(p[1]-start[1])*dy < dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-start[0])*dx+(p[1]-start[1])*dy)
            nodes.extend([start]+inside)
        self.add_polyline(name,*nodes,closed=True)

    def capsule(self, name, x, y, w, h):
        r = h // 2
        self.add_line(name+'-top', (x+r,y), (x+w-r,y))
        self.add_arc(name+'-right', (x+w-r,y), (x+w-r,y+h), radius_x=r)
        self.add_line(name+'-bottom', (x+w-r,y+h), (x+r,y+h))
        self.add_arc(name+'-left', (x+r,y+h), (x+r,y), radius_x=r)
        self.add_contour(name, *[name+s for s in ('-top','-right','-bottom','-left')], closed=True)

