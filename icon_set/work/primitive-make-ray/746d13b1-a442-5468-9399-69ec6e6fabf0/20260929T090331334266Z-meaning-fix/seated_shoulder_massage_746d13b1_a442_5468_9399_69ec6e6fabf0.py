"""Place a taller therapist behind the seated recipient, with two bent arms reaching the upper shoulders."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '746d13b1-a442-5468-9399-69ec6e6fabf0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-shoulder-massage/20260929T085457Z-thuan-mac/reference/thai massage_746d13b1-a442-5468-9399-69ec6e6fabf0.svg'
AUTHOR = "gpt-6"

class RevisedIcon(Solo48):
    icon_id = 'seated-shoulder-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people" 
    aliases = ()
    keywords = ('thai massage',)
    # Symbol plan: Place a taller therapist behind the seated recipient, with two bent arms reaching the upper shoulders.
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

        self.circle('therapist-head',12,8,4)
        self.add_line('therapist-torso',(12,20),(12,34))
        self.path('therapist-legs',(7,44),(12,34),(17,44))
        self.circle('client-head',34,16,4)
        self.path('client-torso',(34,28),(34,31),(32,35),((35,39),4,4,False,False),(42,39),(42,44))
        self.path('near-arm',(12,20),(23,24),(30,28))
        self.path('far-arm',(12,26),(22,31),(29,31))
        self.add_line('seat',(25,44),(36,44))
        self.relate('connect','therapist-torso','therapist-legs')
        self.relate('connect','therapist-torso','near-arm')
        self.relate('connect','therapist-torso','far-arm')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('recipient',head='client-head',torso='client-torso-0',torso_junction='start')
     
