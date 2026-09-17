"""Square Rotation Arrows — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a18765e0-5f96-4d22-bfa9-e6a07ead13c2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize arrows square_a18765e0-5f96-4d22-bfa9-e6a07ead13c2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'square-rotation-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('square', 'rotation', 'arrows')

    def build(self):
        # Plan: two half-turn copies, smooth corner and shared arrow endpoint.
        # Extremes (6,6)-(42,42); Lucide repeat-2: coherent bent shafts.
        for i in range(2):
            p=lambda x,y:(y,48-x) if i==0 else (48-y,x)
            n=f'arrow-{i}'
            self.add_line(n+'-side',p(6,30),p(6,20))
            self.add_arc(n+'-bend',p(6,20),p(14,12),radius_x=8)
            self.add_line(n+'-shaft',p(14,12),p(32,12))
            self.add_contour(n+'-body',n+'-side',n+'-bend',n+'-shaft')
            self.add_polyline(n+'-head',p(26,6),p(32,12),p(26,18))
            self.relate('connect',n+'-body',n+'-head')


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

