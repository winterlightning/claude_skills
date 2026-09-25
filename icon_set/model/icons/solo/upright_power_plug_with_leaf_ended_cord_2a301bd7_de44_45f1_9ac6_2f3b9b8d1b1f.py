"""Eco Friendly Power Plug.

Symbol plan: Plug and leaf joined physically by a looping cord; shared prong spacing and rounded bowl.
Keyshape SQUARE: visible ink extremes (4, 4, 44, 44); stroke centerlines inset 2.
Lucide construction reference: plug and leaf.
Source is visual subject evidence; geometry is freshly authored at 48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a301bd7-de44-45f1-9ac6-2f3b9b8d1b1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/ecology/clean car charging cable_2a301bd7-de44-45f1-9ac6-2f3b9b8d1b1f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upright-power-plug-with-leaf-ended-cord'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    aliases = ()
    keywords = ('plug', 'leaf', 'cord', 'power', 'energy', 'electric', 'green', 'ecology')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def arc(n,a,b,rx,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=sweep)
        def contour(n,*parts,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members) & set(parts)]
            self.add_contour(n,*parts,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r:
                poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            contour(n,*(n+str(i) for i in range(8)),closed=True)
        poly('plug-top',(26,14),(30,14),(38,14),(42,14))
        arc('plug-right',(42,14),(34,26),8,12)
        arc('plug-left',(34,26),(26,14),8,12)
        contour('plug','plug-top-1','plug-top-2','plug-top-3','plug-right','plug-left',closed=True)
        for i,x in enumerate((30,38)): line('prong'+str(i),(x,6),(x,14))
        line('cord-top',(34,26),(34,32))
        arc('cord-loop',(34,32),(14,32),10)
        contour('cord','cord-top','cord-loop')
        arc('leaf-left',(14,14),(6,24),8,10,sweep=False)
        arc('leaf-base',(6,24),(14,32),8,8,sweep=False)
        arc('leaf-right',(14,32),(14,14),12,12,sweep=False)
        contour('leaf','leaf-left','leaf-base','leaf-right',closed=True)
        # Only true shared endpoints are physical connections. No proximity exemptions.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate("connect",a.element_id,b.element_id)
