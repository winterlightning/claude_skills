"""Matched hooks, round beads and symmetric diamond drops using shared series geometry.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
No useful exact Lucide match inspected; supplied reference guided the geometric reconstruction.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '513ef66c-4b4f-5bab-8e0c-b825fb43e517'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/accessories earrings oriental_513ef66c-4b4f-5bab-8e0c-b825fb43e517.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='drop-earrings-with-diamond-beads'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'accessories'
    aliases=()
    keywords=('accessories earrings oriental',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        for x in (12,36):
         n=f'earring-{x}'
         path(n+'-hook',(x-6,12),[('A',(x+6,12),6,6,True),('A',(x,18),6,6,True)])
         circle(n+'-bead',x,22,4)
         poly(n+'-drop',(x,26),(x+6,34),(x,42),(x-6,34),(x,26))
         join(n+'-bead',n+'-drop')
         join(n+'-hook',n+'-bead')
