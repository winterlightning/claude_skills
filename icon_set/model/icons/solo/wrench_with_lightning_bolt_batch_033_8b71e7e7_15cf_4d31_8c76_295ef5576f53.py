"""Wrench with Lightning Bolt — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/flash wrench_8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'wrench-with-lightning-bolt-batch-033'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("symbol", "other", "primitives-generate")
    aliases = ('wrench-with-lightning-bolt',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Integrated diagonal wrench and lightning-shaped lower handle; single contour; extrema (8,4)-(40,44).

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

        self.add_bezier('head-back',(30,4),((17,4),(14,10),(18,20)))
        self.add_line('handle-back',(18,20),(8,32))
        self.add_arc('heel',(8,32),(16,40),radius_x=8,sweep=False)
        self.add_polyline('bolt',(16,40),(28,30),(24,44),(40,26),(28,28),(34,22))
        self.add_bezier('head-outside',(34,22),((40,18),(40,15),(40,12)))
        self.add_polyline('jaw',(40,12),(32,18),(24,12),(30,4))
        self.contours.clear()
        self.add_contour('outline','head-back','handle-back','heel',*[f'bolt-{i}' for i in range(1,6)],'head-outside',*[f'jaw-{i}' for i in range(1,4)],closed=True)
