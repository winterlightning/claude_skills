"""Radio with Tuning Window and Dial.

Symbol plan: Rounded radio with a pill-shaped tuning window, small circular dial and T antenna. Remove microticks and the short aerial tip above its crossbar.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Lucide radio-receiver original and atomic-debug also informed tangent quarter-circle casing corners during final review. Supplied tuning window and dial; shared rounded-rectangle and circle construction defines the intrinsic radio controls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'f2ad1e63-d598-4795-8244-e077843ef1a1'
SOURCE_PATH = 'pictographic-primitives/audio/radio search station_f2ad1e63-d598-4795-8244-e077843ef1a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radio-with-tuning-window-and-dial'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('radio', 'broadcast', 'audio', 'receiver', 'antenna', 'speaker', 'signal', 'tuning')

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

        def casing(n,x,y,w,h,ax,r=4):
            line(n+'-top-left',(x+r,y),(ax,y));line(n+'-top-right',(ax,y),(x+w-r,y))
            arc(n+'-ne',(x+w-r,y),(x+w,y+r),r)
            line(n+'-right',(x+w,y+r),(x+w,y+h-r));arc(n+'-se',(x+w,y+h-r),(x+w-r,y+h),r)
            line(n+'-bottom',(x+w-r,y+h),(x+r,y+h));arc(n+'-sw',(x+r,y+h),(x,y+h-r),r)
            line(n+'-left',(x,y+h-r),(x,y+r));arc(n+'-nw',(x,y+r),(x+r,y),r)
            edges=[n+'-'+suffix for suffix in ('top-left','top-right','ne','right','se','bottom','sw','left','nw')]
            for a,b in zip(edges,edges[1:]+edges[:1]):connect(a,b)

        casing('body',4,16,40,24,24)
        box('window',12,24,12,8,4)
        circle('dial',34,28,2)
        line('antenna',(24,16),(24,8));connect('antenna','body-top-left');connect('antenna','body-top-right')
        path('crossbar',(16,8),(24,8),(32,8));connect('crossbar','antenna')
