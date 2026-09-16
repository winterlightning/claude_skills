"""A square mounting eye connects to a narrow vertical shank that bends into a large open hook. The hook curves down and around before ending in an upward-facing left tip.
Symbol plan: Square mounting eye, short vertical shank and an open curved hook. Use tangent quarter arcs at the neck and a wide elliptical bowl; retain the square eye as the identifying feature.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: no useful hook match. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fd80bcd7-73ab-4b8e-8a28-7672b7384731'
SOURCE_PATH = 'pictographic-primitives/construction/hook_fd80bcd7-73ab-4b8e-8a28-7672b7384731.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'crane-hook-with-square-mount'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('crane', 'hook', 'with', 'square', 'mount')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_polyline('mount',(18,6),(30,6),(30,18),(24,18),(18,18),closed=True)
        self.add_line('shank',(24,18),(24,22))
        self.add_arc('neck',(24,22),(30,28),radius_x=6,sweep=False)
        self.add_arc('hook-right',(30,28),(42,35),radius_x=12,radius_y=7)
        self.add_arc('hook-bottom',(42,35),(6,35),radius_x=18,radius_y=7)
        self.add_line('tip',(6,35),(6,29))
        self.add_contour('hook','shank','neck','hook-right','hook-bottom','tip');self.relate('connect','hook','mount')
