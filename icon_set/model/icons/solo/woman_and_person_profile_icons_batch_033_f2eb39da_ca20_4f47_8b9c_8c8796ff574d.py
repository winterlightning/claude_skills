"""Woman and Person Profile Icons — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f2eb39da-ca20-4f47-8b9c-8c8796ff574d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two users woman_f2eb39da-ca20-4f47-8b9c-8c8796ff574d.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'woman-and-person-profile-icons-batch-033'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('woman-and-person-profile-icons',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Foreground woman with long hair and smaller background bust. Shared human user.svg proportions; detached head/shoulder gap 8 centerline units. Extrema (8,4)-(40,44).

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

        circle('front-head',14,18,6)
        circle('back-head',34,10,6)
        self.add_line('hair-left',(8,18),(8,25))
        self.add_line('hair-right',(20,18),(20,25))
        self.relate('connect','front-head','hair-left')
        self.relate('connect','front-head','hair-right')
        self.add_bezier('front-left',(8,44),((8,35),(9,32),(14,32)))
        self.add_bezier('front-right',(14,32),((20,32),(28,32),(28,36)))
        self.add_line('front-side',(28,36),(28,44))
        self.add_contour('front-body','front-left','front-right','front-side')
        self.add_bezier('back-left',(28,36),((28,28),(28,24),(34,24)))
        self.add_bezier('back-right',(34,24),((38,24),(40,29),(40,36)))
        self.add_contour('back-body','back-left','back-right')
        self.relate('connect','front-body','back-body')
