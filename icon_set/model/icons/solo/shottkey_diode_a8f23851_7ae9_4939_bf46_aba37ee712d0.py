"""Diagonal electronic component with a clean rectangular body and two aligned leads.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; single joined rectangle.
Omissions: Tiny corner bevels simplified to round stroke joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a8f23851-7ae9-4939-bf46-aba37ee712d0'
SOURCE_PATH = 'pictographic-primitives/electronics/shottkey diode_a8f23851-7ae9-4939-bf46-aba37ee712d0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='shottkey-diode'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases=()
    keywords=('shottkey', 'diode')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # Body and leads share the diagonal axis; deliberate 45-degree orientation.
        self.add_polyline('body',(14,26),(26,14),(30,18),(34,22),(22,34),(18,30),closed=True)
        self.add_line('lead-top',(30,18),(42,6));self.add_line('lead-bottom',(18,30),(6,42))
        self.relate('connect','lead-top','body');self.relate('connect','lead-bottom','body')
