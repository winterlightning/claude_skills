"""Wireless Signal Waves — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e84a88d0-3ca7-4537-a4d9-b98932585c2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/electric waves_e84a88d0-3ca7-4537-a4d9-b98932585c2f.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'wireless-signal-waves-batch-033'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('wireless-signal-waves',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Three centered wave strokes, decreasing spans; no dot; extrema (4,10)-(44,38).

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x0,y0,x1,y1,r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8];eid=f'{name}-{i}';ids.append(eid)
                if i%2:self.add_arc(eid,p,q,radius_x=r)
                else:self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        for i,(l,r,top,end) in enumerate(((4,44,10,18),(12,36,23,28),(18,30,35,38))):
            self.add_bezier(f'wave-{i}',(l,end),((l+5,top),(19,top),(24,top)),((29,top),(r-5,top),(r,end)))
