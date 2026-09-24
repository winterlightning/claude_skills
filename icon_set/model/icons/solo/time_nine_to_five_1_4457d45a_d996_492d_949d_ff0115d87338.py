"""Circular clock-return arrow with a smooth three-quarter circle continuing into a rounded lower-right sweep. Lucide clock informs circular geometry; the diagonal hand follows the reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4457d45a-d996-492d-949d-ff0115d87338'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time nine to five 1_4457d45a-d996-492d-949d-ff0115d87338.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'time-nine-to-five-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'nine', 'to', 'five', '1')

    def build(self):
        # Plan: Circular clock-return arrow with a smooth three-quarter circle continuing into a rounded lower-right sweep. Lucide clock informs circular geometry; the diagonal hand follows the reference.
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
        path('rim',(24,42),[('A',(6,24),18,18,True),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(34,39),(42,30),(39,36))])
        poly('arrow',(34,30),(34,39),(42,39));join('arrow','rim')
        line('hand',(22,26),(30,18))
