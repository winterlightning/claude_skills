"""Wooden Picket Fence — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'db8f7209-535a-41cd-8b31-f6af4d662ecb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fence_db8f7209-535a-41cd-8b31-f6af4d662ecb.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'wooden-picket-fence-batch-033'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('wooden-picket-fence',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Three identical pointed pickets, two connecting rails, shared 16-unit pitch; extrema (4,8)-(44,40).

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

        for j,x in enumerate((4,20,36)):
            self.add_polyline(f'board-{j}',(x,40),(x,32),(x,22),(x,16),(x+4,8),(x+8,16),(x+8,22),(x+8,32),(x+8,40),closed=True)
        for i,y in enumerate((22,32)):
            for j,(a,b) in enumerate(((12,20),(28,36))):
                self.add_line(f'rail-{i}-{j}',(a,y),(b,y))
                self.relate('connect',f'rail-{i}-{j}',f'board-{j}')
                self.relate('connect',f'rail-{i}-{j}',f'board-{j+1}')
