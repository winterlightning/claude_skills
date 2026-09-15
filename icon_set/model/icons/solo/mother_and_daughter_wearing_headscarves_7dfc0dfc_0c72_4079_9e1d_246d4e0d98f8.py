"""Mother and Daughter Wearing Headscarves.

Symbol plan: Adult and smaller child in pointed headscarves; shared circular-jaw vocabulary and soft shoulders. Omit nested face borders and sleeve seams. Each detached head/body ink gap is exactly4.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg and full_body_ref.png: circular jaws and broad shoulders. Child bottom28/top36, mother bottom22/top30: 4-unit ink gaps; natural size asymmetry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim mom daughter_7dfc0dfc-0c72-4079-9e1d-246d4e0d98f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mother-and-daughter-wearing-headscarves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('mother', 'daughter', 'muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)

        for n,cx,cy,r,top,ry in [('child',10,22,6,36,4),('mother',36,14,8,30,10)]:
            line(n+'-hood-l',(cx-r,cy),(cx,cy-r))
            line(n+'-hood-r',(cx,cy-r),(cx+r,cy))
            arc(n+'-jaw',(cx+r,cy),(cx-r,cy),r)
            join(n+'-head',n+'-hood-l',n+'-hood-r',n+'-jaw',closed=True)
            arc(n+'-shoulders',(cx-r,40),(cx+r,40),r,ry)
