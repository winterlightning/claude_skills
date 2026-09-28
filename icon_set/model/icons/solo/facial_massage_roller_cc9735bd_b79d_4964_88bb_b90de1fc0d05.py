"""Facial Massage Roller.

Symbol plan: Horizontal capsule roller, mirrored open Y support, center handle. Drop the pinched roller waist.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide paint-roller: broad roller capsule and coherent support.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'cc9735bd-b79d-4964-88bb-b90de1fc0d05'
SOURCE_PATH = 'pictographic-primitives/beauty/massage stick roll_cc9735bd-b79d-4964-88bb-b90de1fc0d05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'facial-massage-roller'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('facial', 'massage', 'roller')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if a==b: continue
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            join(n,*(n+str(i) for i in range(8) if pts[i]!=pts[(i+1)%8]),closed=True)

        box('roller',8,4,32,12,6)
        path('support',(8,10),(8,23),(24,31),(40,23),(40,10))
        connect('support','roller')
        line('handle',(24,31),(24,44))
        connect('handle','support')
