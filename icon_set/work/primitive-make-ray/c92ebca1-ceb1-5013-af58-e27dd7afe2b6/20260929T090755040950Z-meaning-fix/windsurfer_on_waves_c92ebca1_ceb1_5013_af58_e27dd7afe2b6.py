"""Show a wind-filled sail, hand gripping the boom, bent surfing legs, an angled board and a low wave."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c92ebca1-ceb1-5013-af58-e27dd7afe2b6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__windsurfer-on-waves/20260929T085457Z-thuan-mac/reference/sport windsurfing_c92ebca1-ceb1-5013-af58-e27dd7afe2b6.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'windsurfer-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('sport windsurfing',)
    # Symbol plan: Show a wind-filled sail, hand gripping the boom, bent surfing legs, an angled board and a low wave.
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

        self.path('sail',(8,32),((29,4),31,32,True,False),(22,33),(8,32),closed=True)
        self.add_line('mast',(29,4),(21,36))
        self.circle('head',39,12,4)
        self.path('torso',(39,24),(39,26),(35,28))
        self.path('arm',(39,24),(31,24),(25,20))
        self.path('legs',(27,36),(29,31),(35,28),(42,32),(42,36))
        self.path('board',(5,36),(44,36))
        self.path('wave',(5,44),((15,44),8,4,False,False),((25,44),8,4,True,False),
                  ((35,44),8,4,False,False),((43,44),8,4,True,False))
        self.relate('connect','mast','sail')
        self.relate('connect','torso','arm')
        self.relate('connect','torso','legs')
        self.mark_human_figure('surfer',head='head',torso='torso-0',torso_junction='start')
     
