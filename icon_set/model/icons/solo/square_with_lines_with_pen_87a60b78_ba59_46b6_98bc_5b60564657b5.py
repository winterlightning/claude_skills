"""Straight diagonal pencil edges and a separate writing baseline; Lucide pencil-line informs the clean tip and barrel."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '87a60b78-ba59-46b6-98bc-5b60564657b5'
SOURCE_PATH = 'pictographic-primitives/symbol/square with lines with pen_87a60b78-ba59-46b6-98bc-5b60564657b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-with-lines-with-pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('square', 'with', 'lines', 'with', 'pen')

    def build(self):
        # Plan: Straight diagonal pencil edges and a separate writing baseline; Lucide pencil-line informs the clean tip and barrel.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('pencil',(6,42),(10,30),(34,6),(42,14),(18,38),closed=True)
        line('baseline',(27,42),(42,42))
