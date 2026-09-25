"""Woman Head Avatar — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '223acbcd-fc0d-46aa-a05a-cd4a9693b0b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/women_223acbcd-fc0d-46aa-a05a-cd4a9693b0b8.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'woman-head-avatar-batch-033'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('woman-head-avatar',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Blank circular-jaw face under center-parted long hair; shared axis24; extrema (8,4)-(40,44).

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

        self.add_arc('crown',(8,20),(40,20),radius_x=16)
        self.add_line('outer-right',(40,20),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('hair-base',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('outer-left',(8,40),(8,20))
        self.add_contour('hair','crown','outer-right','br','hair-base','bl','outer-left',closed=True)
        self.add_bezier('part-left',(24,14),((23,17),(20,19),(17,19)))
        self.add_line('face-left',(17,19),(17,26))
        self.add_arc('jaw',(17,26),(31,26),radius_x=7,sweep=False)
        self.add_line('face-right',(31,26),(31,19))
        self.add_bezier('part-right',(31,19),((28,19),(25,17),(24,14)))
        self.add_contour('face','part-left','face-left','jaw','face-right','part-right',closed=True)
