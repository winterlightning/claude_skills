"""Star Bullet List — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9f5352-9a81-538a-850f-d9262de8b416'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/list stars_cd9f5352-9a81-538a-850f-d9262de8b416.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'star-bullet-list'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('star', 'bullet', 'list')

    def build(self):
        # Plan: a three-member vertical series of five spokes and list lines.
        # Extremes (8,6)-(42,42); intrinsic list layout, no useful exact Lucide match.
        for i,y in enumerate((8,24,40)):
            n=f'bullet-{i}'
            ends=((12,y-4),(8,y),(16,y),(9,y+4),(15,y+4))
            for j,end in enumerate(ends):
                self.add_line(f'{n}-{j}',(12,y),end)
            for j in range(5):
                for k in range(j+1,5): self.relate('connect',f'{n}-{j}',f'{n}-{k}')
            self.add_line(f'row-{i}',(26,y),(40,y))


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

