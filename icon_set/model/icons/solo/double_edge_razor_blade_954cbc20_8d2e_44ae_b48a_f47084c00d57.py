"""Double-Edge Razor Blade.

Symbol plan: Double-edge razor blade with mirrored end notches and a central rounded slot. Orient horizontally and omit the tiny slot extensions and end ticks.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide blade match; reconstruct the source as one symmetric notched blade with a clear central opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '954cbc20-8d2e-44ae-b48a-f47084c00d57'
SOURCE_PATH = 'pictographic-primitives/beauty/razor tool_954cbc20-8d2e-44ae-b48a-f47084c00d57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'double-edge-razor-blade'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('razor', 'blade', 'shaving', 'barber', 'grooming', 'cutting', 'tool', 'edge')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w//2,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+w//2,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            curves={2,4,7,9}
            for j in range(10):
                a,b=pts[j],pts[(j+1)%10]
                if a==b: continue
                if j in curves: arc(n+str(j),a,b,r)
                else: line(n+str(j),a,b)
            join(n,*(n+str(j) for j in range(10) if pts[j]!=pts[(j+1)%10]),closed=True)


        path('blade',(4,8),(44,8),(44,16),(40,16),(40,32),(44,32),(44,40),(4,40),(4,32),(8,32),(8,16),(4,16),(4,8),closed=True)
        box('slot',17,20,14,8,2)
