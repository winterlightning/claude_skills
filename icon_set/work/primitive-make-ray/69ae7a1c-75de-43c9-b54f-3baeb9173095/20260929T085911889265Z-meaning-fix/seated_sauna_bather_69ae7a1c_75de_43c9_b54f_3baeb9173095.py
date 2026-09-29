"""Use a relaxed seated pose on a continuous bench and three rising steam strokes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69ae7a1c-75de-43c9-b54f-3baeb9173095'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-sauna-bather/20260929T085457Z-thuan-mac/reference/sauna heat person_69ae7a1c-75de-43c9-b54f-3baeb9173095.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-sauna-bather'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('sauna heat person',)
    # Symbol plan: Use a relaxed seated pose on a continuous bench and three rising steam strokes.
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

        self.circle('head',15,11,5)
        self.path('torso',(15,24),(12,30),((16,34),4,4,False,False),(28,34),(35,44))
        self.path('arm',(15,24),(22,29),(27,29))
        self.path('bench',(6,44),(6,36),(20,36))
        for j,x in enumerate((29,36,43)):
            self.path(f'steam-{j}',(x,5),((x,11),4,5,True,False),((x,17),4,5,False,False))
        self.relate('connect','torso','arm')
        self.mark_human_figure('bather',head='head',torso='torso-0',torso_junction='start')
     
