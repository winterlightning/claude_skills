"""Staggered Timeline Bars — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '454d7fdd-f4e2-46b3-bc2a-ccc3fe6e5baa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/workflow gantt chart_454d7fdd-f4e2-46b3-bc2a-ccc3fe6e5baa.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'staggered-timeline-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('staggered', 'timeline', 'bars')

    def build(self):
        # Plan: three equal-height staggered bars and one shared vertical guide.
        # Extremes (8,4)-(40,44). Table's aligned divisions inform the joins.
        for i,(x,y,w) in enumerate(((8,4,24),(12,20,24),(16,36,24))):
            n=f'bar-{i}'
            self.rectangle(n,x,y,w,8, attachments=((24,y),(24,y+8)))
            self.add_line(n+'-guide',(24,y),(24,y+8))
            self.relate('connect',n,n+'-guide')
        for i,(a,b) in enumerate(((12,20),(28,36))):
            n=f'guide-{i}'
            self.add_line(n,(24,a),(24,b))
            for j in (i,i+1):
                self.relate('connect',n,f'bar-{j}')
                self.relate('connect',n,f'bar-{j}-guide')


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

