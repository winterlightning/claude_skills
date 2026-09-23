"""A human portrait inside a frame between two detached horizontal rules.
Construction: square-user-round. Facial detail omitted as in the original; shoulder width reduced for the frame.
Keyshape VRECT_L; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1dccf6db-d157-5a7b-98f3-d179b8bf43ee'
SOURCE_PATH = 'icon_set/work/todo-references/frame human_1dccf6db-d157-5a7b-98f3-d179b8bf43ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frame-human'
    keyshape = Keyshape.VRECT_L
    # Declared visible-ink extrema: (6, 2, 42, 46).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('frame', 'human')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    # Human construction reference: icon_set/references/human_ref/user.svg
    def build(self):

        # Plan: mirror the bust around x=24; retain two detached frame rules.
        self.add_line('top-rule',(8,4),(40,4))
        self.add_line('bottom-rule',(8,44),(40,44))
        self.rect('frame',8,13,32,22)
        # Human reference supplies round head and broad, mirrored shoulders.
        # Source has a continuous neck: detached-head gap is not applicable.
        self.add_arc('crown',(19,22),(29,22),radius_x=5)
        self.add_arc('jaw-right',(29,22),(27,26),radius_x=5)
        self.add_bezier('neck-shoulder-right',(27,26),((25,31),(34,29),(34,35)))
        self.add_line('base',(34,35),(14,35))
        self.add_bezier('neck-shoulder-left',(14,35),((14,29),(23,31),(21,26)))
        self.add_arc('jaw-left',(21,26),(19,22),radius_x=5)
        self.add_contour('portrait','crown','jaw-right','neck-shoulder-right',
                         'base','neck-shoulder-left','jaw-left',closed=True)
        self.relate('connect','portrait','frame')
