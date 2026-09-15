"""Curved Arrow Up with Chevron.

Symbol plan: Curved directional arrow and matching detached chevron. Reduce the thick outlined arrow to the standard round stroke; preserve the bend and repeated direction.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1af59dcf-a018-5eec-944c-8b905cfe18b7'
SOURCE_PATH = 'pictographic-primitives/arrows/navigation direction top_1af59dcf-a018-5eec-944c-8b905cfe18b7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-arrow-up-with-chevron'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

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

        up=True
        def pt(x,y): return (48-x,48-y) if up else (x,y)
        arc('bend',pt(40,4),pt(24,20),16,s=False)
        line('shaft',pt(24,20),pt(24,28));join('route','bend','shaft')
        path('head',pt(8,16),pt(24,28),pt(40,16));connect('route','head')
        path('chevron',pt(8,32),pt(24,44),pt(40,32))
