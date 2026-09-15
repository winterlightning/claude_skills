"""Muslim Reader Holding Open Book.

Symbol plan: Capped reader behind a broad open book with a central fold. Simplify hanging side cloth and omit page text.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Lucide book-open: two broad pages with a shared fold; human_ref/user.svg: round head/shoulders. Jaw bottom20, bodytop24: current avatar zero ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3dbfbc82-fe7f-46ee-b193-539e5dd1a202'
SOURCE_PATH = 'pictographic-primitives/avatars/muslim reading quraan_3dbfbc82-fe7f-46ee-b193-539e5dd1a202.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'muslim-reader-holding-open-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('reading', 'book', 'muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

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

        arc('crown',(16,12),(32,12),8)
        arc('jaw',(32,12),(16,12),8)
        join('head','crown','jaw',closed=True)
        line('cap',(16,12),(32,12));connect('cap','head')
        arc('body-shoulder-l',(8,28),(24,24),16,4)
        arc('body-shoulder-r',(24,24),(40,28),16,4)
        join('body','body-shoulder-l','body-shoulder-r')
        connect('head','body')
        path('book',(8,28),(24,32),(40,28),(40,40),(24,44),(8,40),(8,28),closed=True)
        line('fold',(24,32),(24,44));connect('fold','book');connect('body','book')
