"""Oxygen Cylinder with T Valve.

Symbol plan: Rounded upright cylinder with a simple T valve, centered on the same axis. Drop the extra neck seam.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f86557da-1cc7-4eae-8fd9-4d5f68f015ce'
SOURCE_PATH = 'pictographic-primitives/beauty/oxygen tank_f86557da-1cc7-4eae-8fd9-4d5f68f015ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oxygen-cylinder-with-t-valve'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('oxygen', 'cylinder', 'tank', 'gas', 'valve', 'medical', 'storage', 'equipment')

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

        box('cylinder',8,16,32,28,8)
        line('stem',(24,4),(24,16));path('valve',(16,4),(24,4),(32,4))
        connect('stem','valve');connect('stem','cylinder')
