"""heart user, re-authored as one complete SOLO48 composition.
Symbol plan is recorded in build(); paired shapes share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e7e97355-bccb-465c-ae55-5037fd70d291'
SOURCE_PATH = 'icon_set/work/todo-references/heart user_e7e97355-bccb-465c-ae55-5037fd70d291.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'heart-user'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('heart user',)

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
        self.add_arc('left-shoulder',(6,15),(10,27),radius_x=20,sweep=False)
        self.add_line('point-1',(10,27),(24,42))
        self.add_line('point-2',(24,42),(38,27))
        self.add_arc('right-shoulder',(38,27),(42,15),radius_x=20,sweep=False)
        self.add_arc('right-lobe',(42,15),(24,15),radius_x=9,sweep=False)
        self.add_contour('heart','left-lobe','left-shoulder','point-1','point-2','right-shoulder','right-lobe',closed=True)

    def build(self):
        # Human reference: human_ref/user.svg; circle head, open rounded shoulders.
        # Head bottom=23, shoulder top=31: 8 centerline / exactly 4 ink units.
        self.heart()
        self.circle('head',24,20,3)
        self.add_arc('shoulders',(18,35),(30,35),radius_x=6,radius_y=4)

# Declared visible keyshape extremes: (4, 4, 44, 44).
