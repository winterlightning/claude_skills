"""A short rounded mounting block hangs beneath a wide horizontal beam. A slender hook descends from the block, bending right and curling around into an open upward-facing end.
Symbol plan: Wide single-stroke beam over a central mounting block and one open J hook. Shared beam and block nodes preserve true attachment. Omit the duplicate beam edge to reserve a long shank and broad bowl.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: no useful hook match. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1a7e6b5d-f481-539b-99c2-cd5e777fe71e'
SOURCE_PATH = 'pictographic-primitives/construction/lift hook_1a7e6b5d-f481-539b-99c2-cd5e777fe71e.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'lifting-hook-below-horizontal-beam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('lifting', 'hook', 'below', 'horizontal', 'beam')

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

        self.add_polyline('beam',(4,8),(16,8),(32,8),(44,8))
        self.add_polyline('block',(16,8),(16,16),(24,16),(32,16),(32,8));self.relate('connect','beam','block')
        self.add_line('shank',(24,16),(24,22))
        self.add_arc('neck',(24,22),(28,26),radius_x=4,sweep=False)
        self.add_arc('hook-right',(28,26),(40,33),radius_x=12,radius_y=7)
        self.add_arc('hook-bottom',(40,33),(8,33),radius_x=16,radius_y=7)
        self.add_line('tip',(8,33),(8,27));self.add_contour('hook','shank','neck','hook-right','hook-bottom','tip');self.relate('connect','hook','block')
