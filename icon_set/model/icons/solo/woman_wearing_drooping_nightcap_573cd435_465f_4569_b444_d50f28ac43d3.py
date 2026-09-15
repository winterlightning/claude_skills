"""Woman Wearing Drooping Nightcap.

Symbol plan: Isolated circular lower face under a drooping cap and small pompom. Omit crowded hair wings and keep the cap bend; deliberate accessory asymmetry.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: human_ref/user.svg: circular face vocabulary. This source is a head-only portrait, so no invented body or detached-head gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '573cd435-465f-4569-b444-d50f28ac43d3'
SOURCE_PATH = 'pictographic-primitives/avatars/pajamas woman_573cd435-465f-4569-b444-d50f28ac43d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-wearing-drooping-nightcap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('nightcap', 'person', 'portrait', 'head', 'bust', 'clothing', 'hair', 'face', 'avatar')

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

        arc('jaw',(32,32),(12,32),10)
        path('brim',(6,32),(12,32),(32,32))
        connect('jaw','brim')
        line('hat-left',(6,32),(6,18))
        arc('hat-crown-l',(6,18),(18,6),12)
        line('hat-top',(18,6),(28,6))
        arc('hat-crown-r',(28,6),(40,18),12)
        path('hat-fold',(40,18),(32,18),(32,32))
        join('hat','hat-left','hat-crown-l','hat-top','hat-crown-r','hat-fold-1','hat-fold-2')
        self.contours=[c for c in self.contours if c.contour_id!='hat-fold']
        connect('hat','brim');connect('hat','jaw')
        circle('pompom',40,20,2);connect('pompom','hat')
