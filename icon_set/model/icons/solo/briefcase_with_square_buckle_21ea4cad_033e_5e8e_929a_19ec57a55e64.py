"""Briefcase with Square Buckle.

Symbol plan: Rounded briefcase with top handle, a divided flap and centered square buckle. Drop the narrow double outer shell.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide briefcase-business original and atomic-debug: rounded shell, attached handle and one shared flap boundary.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '21ea4cad-033e-5e8e-929a-19ec57a55e64'
SOURCE_PATH = 'pictographic-primitives/business/products briefcase_21ea4cad-033e-5e8e-929a-19ec57a55e64.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'briefcase-with-square-buckle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('briefcase', 'case', 'luggage', 'business', 'work', 'handle', 'office', 'bag')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)


        line('case-top-left',(10,16),(16,16));line('case-top-middle',(16,16),(32,16));line('case-top-right',(32,16),(38,16))
        arc('case-ne',(38,16),(42,20),4)
        line('case-right-upper',(42,20),(42,26));line('case-right-lower',(42,26),(42,38))
        arc('case-se',(42,38),(38,42),4);line('case-bottom',(38,42),(10,42))
        arc('case-sw',(10,42),(6,38),4)
        line('case-left-lower',(6,38),(6,26));line('case-left-upper',(6,26),(6,20));arc('case-nw',(6,20),(10,16),4)
        join('case','case-top-left','case-top-middle','case-top-right','case-ne','case-right-upper','case-right-lower','case-se','case-bottom','case-sw','case-left-lower','case-left-upper','case-nw',closed=True)
        line('handle-left',(16,16),(16,8));arc('handle-nw',(16,8),(18,6),2)
        line('handle-top',(18,6),(30,6));arc('handle-ne',(30,6),(32,8),2)
        line('handle-right',(32,8),(32,16));join('handle','handle-left','handle-nw','handle-top','handle-ne','handle-right');connect('handle','case')
        box('buckle',20,26,8,8,1)
        line('flap-left',(6,26),(20,26));line('flap-right',(28,26),(42,26))
        connect('flap-left','buckle');connect('flap-right','buckle');connect('flap-left','case');connect('flap-right','case')
