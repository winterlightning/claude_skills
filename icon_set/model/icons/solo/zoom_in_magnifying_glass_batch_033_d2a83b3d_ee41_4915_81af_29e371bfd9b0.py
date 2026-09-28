"""Zoom In Magnifying Glass — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd2a83b3d-ee41-4915-81af-29e371bfd9b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/magnifying glass with plus_d2a83b3d-ee41-4915-81af-29e371bfd9b0.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'zoom-in-magnifying-glass-batch-033'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("symbol", "state", "other", "primitives-generate")
    aliases = ('zoom-in-magnifying-glass',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Circular magnifier with centered plus and diagonal handle; extrema (6,6)-(42,42).

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

        # Radius 15 lens, with a true handle attachment at the lower-right diagonal point.
        self.add_arc('lens-a',(30,33),(6,21),radius_x=15,large_arc=True)
        self.add_arc('lens-b',(6,21),(30,33),radius_x=15)
        self.add_contour('lens','lens-a','lens-b',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','lens','handle')
        self.add_polyline('horizontal',(15,21),(21,21),(27,21))
        self.add_polyline('vertical',(21,15),(21,21),(21,27))
        self.relate('connect','horizontal','vertical')
