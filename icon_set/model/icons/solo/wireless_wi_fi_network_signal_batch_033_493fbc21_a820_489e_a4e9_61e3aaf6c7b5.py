"""Wireless Wi-Fi Network Signal — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '493fbc21-a820-489e-a4e9-61e3aaf6c7b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/electric waves_493fbc21-a820-489e-a4e9-61e3aaf6c7b5.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'wireless-wi-fi-network-signal-batch-033'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('wireless-wi-fi-network-signal',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Three nested waves and one hollow point; shared axis 24; extrema (4,8)-(44,40).

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

        for i,(l,r,top,end) in enumerate(((4,44,8,15),(12,36,18,21),(19,29,28,29))):
            self.add_bezier(f'wave-{i}',(l,end),((l+4,top),(20,top),(24,top)),((28,top),(r-4,top),(r,end)))
        circle('point',24,38,2)
