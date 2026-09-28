"""Separated Spreadsheet Rows — independently authored for batch 49."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0dfc3e66-f572-4961-ab0a-b37e1dd66822'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/split subset spreadsheet_0dfc3e66-f572-4961-ab0a-b37e1dd66822.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'separated-spreadsheet-rows'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('separated', 'spreadsheet', 'rows')

    def build(self):
        # Plan: three columns, upper two-row table and lower one-row table;
        # double-headed connectors share exact table-edge endpoints.
        # VRECT_L extrema (8,4)-(40,44). Lucide table informs regular cells.
        for i,(y,h) in enumerate(((4,16),(36,8))):
            n=f'band-{i}'
            self.rectangle(n,8,y,32,h, attachments=tuple((x,v) for x in (18,30) for v in (y,y+h)) + tuple((x,20 if i==0 else 36) for x in (14,34)) + (((8,12),(40,12)) if i==0 else ()))
            for j,x in enumerate((18,30)):
                self.add_polyline(f'{n}-cell-{j}',(x,y),(x,12),(x,y+h)) if i==0 else self.add_line(f'{n}-cell-{j}',(x,y),(x,y+h))
                self.relate('connect',n,f'{n}-cell-{j}')
        self.add_polyline('upper-row',(8,12),(18,12),(30,12),(40,12))
        self.relate('connect','upper-row','band-0')
        for j in range(2): self.relate('connect','upper-row',f'band-0-cell-{j}')
        for i,x in enumerate((14,34)):
            n=f'arrow-{i}'
            self.add_line(n+'-shaft',(x,20),(x,36))
            self.add_polyline(n+'-top',(x-4,24),(x,20),(x+4,24))
            self.add_polyline(n+'-bottom',(x-4,32),(x,36),(x+4,32))
            for suffix in ('-top','-bottom'): self.relate('connect',n+'-shaft',n+suffix)
            for j,suffix in enumerate(('-top','-bottom')):
                self.relate('connect',n+'-shaft',f'band-{j}')
                self.relate('connect',n+suffix,f'band-{j}')

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

