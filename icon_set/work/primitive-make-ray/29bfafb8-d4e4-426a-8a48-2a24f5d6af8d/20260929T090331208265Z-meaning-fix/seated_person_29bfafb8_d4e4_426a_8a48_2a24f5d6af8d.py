"""Put both bent legs in front of a rounded seated hip and extend a relaxed arm over the knees."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '29bfafb8-d4e4-426a-8a48-2a24f5d6af8d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-person/20260929T085457Z-thuan-mac/reference/sitting_29bfafb8-d4e4-426a-8a48-2a24f5d6af8d.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-person'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('sitting',)
    # Symbol plan: Put both bent legs in front of a rounded seated hip and extend a relaxed arm over the knees.
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

        self.circle('head',20,9,5)
        self.path('torso', (20,22), (20,25), ((15,38),11,14,False,False),
                  ((21,40),6,5,False,False), (29,34), (38,44))
        self.path('arm', (20,22), (32,22), (32,27))
        self.path('near-leg', (21,40), (28,40), (31,44))
        self.relate('connect','torso','arm')
        self.relate('connect','torso','near-leg')
        self.mark_human_figure('person',head='head',torso='torso-0',torso_junction='start')
     
