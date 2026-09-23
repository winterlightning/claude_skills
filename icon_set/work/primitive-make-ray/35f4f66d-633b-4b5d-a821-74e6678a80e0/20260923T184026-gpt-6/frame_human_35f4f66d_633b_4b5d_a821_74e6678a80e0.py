"""A human portrait in a frame with top and bottom bands.
Construction: square-user-round. No facial details; rounded reference neck translated to shared circular-head vocabulary.
Keyshape SQUARE; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '35f4f66d-633b-4b5d-a821-74e6678a80e0'
SOURCE_PATH = 'icon_set/work/todo-references/frame human_35f4f66d-633b-4b5d-a821-74e6678a80e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'frame-human'
    keyshape = Keyshape.SQUARE
    # Declared visible-ink extrema: (4, 4, 44, 44).
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

        # Plan: outer frame, two integral rails, circular head and mirrored bust.
        self.rect('frame',6,6,36,36)
        for y in (14,34):
            self.add_line('rail-'+str(y),(6,y),(42,y))
            self.relate('connect','frame','rail-'+str(y))
        # Human reference supplies round head and broad, mirrored shoulders.
        # Source has a continuous neck: detached-head gap is not applicable.
        self.add_arc('crown',(19,22),(29,22),radius_x=5)
        self.add_arc('jaw-right',(29,22),(27,26),radius_x=5)
        self.add_bezier('neck-shoulder-right',(27,26),((25,31),(34,29),(34,34)))
        self.add_line('base',(34,34),(14,34))
        self.add_bezier('neck-shoulder-left',(14,34),((14,29),(23,31),(21,26)))
        self.add_arc('jaw-left',(21,26),(19,22),radius_x=5)
        self.add_contour('portrait','crown','jaw-right','neck-shoulder-right',
                         'base','neck-shoulder-left','jaw-left',closed=True)
        self.relate('connect','portrait','frame')
        self.relate('connect','portrait','rail-34')
