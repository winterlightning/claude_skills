"""Spreadsheet Duplication Diagram — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b3a3a8e-aa1a-48df-9509-872ac7bd10a7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/duplicate spreadsheet_6b3a3a8e-aa1a-48df-9509-872ac7bd10a7.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'spreadsheet-duplication-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('spreadsheet', 'duplication', 'diagram')

    def build(self):
        # Plan: two open table edges, cell dividers, two directed row connections.
        # Extremes (6,6)-(42,42); Lucide table: regular grid and simple borders.
        for side in (0,1):
            p=lambda x,y:(x,y) if side==0 else (48-x,y)
            n=f'table-{side}'
            self.add_polyline(n,p(6,6),p(14,6),p(14,16),p(14,32),p(14,42),p(6,42))
            for j,y in enumerate((16,32)):
                self.add_line(f'{n}-row-{j}',p(6,y),p(14,y))
                self.relate('connect',n,f'{n}-row-{j}')
            self.add_line(n+'-outer',p(6,16),p(6,32))
            for j in range(2): self.relate('connect',n+'-outer',f'{n}-row-{j}')
        for i,y in enumerate((16,32)):
            flip=False and i==0
            p=lambda x,y:(48-x,y) if flip else (x,y)
            n=f'arrow-{i}'
            self.add_line(n+'-shaft',p(14,y),p(25,y))
            self.add_polyline(n+'-head',p(21,y-4),p(25,y),p(21,y+4))
            self.relate('connect',n+'-shaft',n+'-head')
            self.relate('connect',n+'-shaft','table-1' if flip else 'table-0')
            self.relate('connect',n+'-shaft',f'table-{1 if flip else 0}-row-{i}')


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

