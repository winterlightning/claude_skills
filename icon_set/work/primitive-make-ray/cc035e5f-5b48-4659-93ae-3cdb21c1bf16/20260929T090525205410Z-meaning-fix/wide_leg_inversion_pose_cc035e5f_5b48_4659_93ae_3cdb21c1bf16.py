"""Restore raised spread legs, a short inverted torso, low head, and two bent forearms reaching the floor."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cc035e5f-5b48-4659-93ae-3cdb21c1bf16'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__wide-leg-inversion-pose/20260929T085457Z-thuan-mac/reference/wide seat inversion pose_cc035e5f-5b48-4659-93ae-3cdb21c1bf16.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'wide-leg-inversion-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('wide seat inversion pose',)
    # Symbol plan: Restore raised spread legs, a short inverted torso, low head, and two bent forearms reaching the floor.
    # Construction: human_ref/full_body_ref.png

    def path(self, name, start, *segments, closed=False):
        ids = []
        point = start
        for j, segment in enumerate(segments):
            eid = f"{name}-{j}"
            if len(segment) == 2:
                self.add_line(eid, point, segment)
                end = segment
            else:
                end, rx, ry, sweep, large = segment
                self.add_arc(eid, point, end, radius_x=rx, radius_y=ry,
                             sweep=sweep, large_arc=large)
            ids.append(eid)
            point = end
        self.add_contour(name, *ids, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), ((x+r,y),r,r,True,False),
                  ((x-r,y),r,r,True,False), closed=True)

    def oval(self, name, x, y, rx, ry):
        self.path(name, (x-rx,y), ((x+rx,y),rx,ry,True,False),
                  ((x-rx,y),rx,ry,True,False), closed=True)

    def box(self, name, x1,y1,x2,y2,r=3):
        self.path(name, (x1+r,y1), (x2-r,y1),
                  ((x2,y1+r),r,r,True,False), (x2,y2-r),
                  ((x2-r,y2),r,r,True,False), (x1+r,y2),
                  ((x1,y2-r),r,r,True,False), (x1,y1+r),
                  ((x1+r,y1),r,r,True,False), closed=True)

    def build(self):

        self.path('legs',(8,4),(24,22),(40,4))
        self.add_line('torso',(24,22),(24,26))
        self.circle('head',24,39,5)
        self.path('left-arm',(24,26),(12,26),(8,34),(11,42))
        self.path('right-arm',(24,26),(36,26),(40,34),(37,42))
        self.relate('connect','legs','torso')
        self.relate('connect','torso','left-arm')
        self.relate('connect','torso','right-arm')
        self.mark_human_figure('inverted-person',head='head',torso='torso',torso_junction='end')
     
