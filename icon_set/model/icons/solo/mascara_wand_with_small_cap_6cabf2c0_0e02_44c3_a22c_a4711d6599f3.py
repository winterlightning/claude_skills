"""Mascara Wand with Small Cap.

Symbol plan: Left wand with two repeated bristle bars, capsule handle; right removable cap. Drop the third bristle and seam for clearance.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide paint-roller: simple capsule ends and shared handle attachment.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '6cabf2c0-0e02-44c3-a22c-a4711d6599f3'
SOURCE_PATH = 'pictographic-primitives/beauty/mascara small_6cabf2c0-0e02-44c3-a22c-a4711d6599f3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mascara-wand-with-small-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('mascara', 'wand', 'with', 'small', 'cap')

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

        box('handle',8,28,12,16,6)
        path('shaft',(14,4),(14,12),(14,28))
        connect('shaft','handle')
        for j,y in enumerate((4,12)):
            path('bristle-'+str(j),(8,y),(14,y),(20,y))
            connect('shaft','bristle-'+str(j))
        box('cap',30,4,10,16,5)
