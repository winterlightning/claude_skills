"""Modern Air Purifier Device — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f9ddf567-958c-4ad6-b315-91f3bace55cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air purifier 1_f9ddf567-958c-4ad6-b315-91f3bace55cf.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'modern-air-purifier-device-batch-033'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('modern-air-purifier-device',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Rounded upright purifier and three gently undulating repeated vents, 10-unit pitch; extrema (8,4)-(40,44).

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

        rect('body',8,4,40,44)
        for i,y in enumerate((14,24,34)):
            self.add_bezier(f'vent-{i}',(18,y),((21,y-3),(27,y+3),(30,y)))
