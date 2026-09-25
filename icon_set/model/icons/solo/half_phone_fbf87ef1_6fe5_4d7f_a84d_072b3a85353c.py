"""half phone, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fbf87ef1-6fe5-4d7f-a84d-072b3a85353c'
SOURCE_PATH = 'icon_set/work/todo-references/half phone_fbf87ef1-6fe5-4d7f-a84d-072b3a85353c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'half-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ()
    keywords = ('half phone',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)

    def rounded(self,n,x,y,w,h,r):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=points[i],points[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def heart(self):
        # Paired nine-unit lobes and mirrored lower shoulders.
        self.add_arc('left-lobe',(24,15),(6,15),radius_x=9,sweep=False)
        self.add_arc('left-shoulder',(6,15),(10,25),radius_x=14,sweep=False)
        self.add_line('point-1',(10,25),(24,42))
        self.add_line('point-2',(24,42),(38,25))
        self.add_arc('right-shoulder',(38,25),(42,15),radius_x=14,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Open-bottom phone shell; mirrored upper corners and centered speaker.
        self.add_line('left',(8,44),(8,10))
        self.add_arc('tl',(8,10),(14,4),radius_x=6)
        self.add_line('top',(14,4),(34,4))
        self.add_arc('tr',(34,4),(40,10),radius_x=6)
        self.add_line('right',(40,10),(40,44))
        self.add_contour('shell','left','tl','top','tr','right')
        self.add_line('speaker',(20,13),(28,13))

# Declared visible keyshape extremes: (6, 2, 42, 46).
