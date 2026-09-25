"""A tilted red blood cell with a smooth outer disc and a central depression.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; tangent quarter-circle construction.
Omissions: None
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0a49c99-174d-4d2d-ac7c-9636f2302170'
SOURCE_PATH = 'pictographic-primitives/health/red blood cell strem 1_b0a49c99-174d-4d2d-ac7c-9636f2302170.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='red-blood-cell-strem-1'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "health"
    categories = ("health", "primitives")
    aliases=()
    keywords=('red', 'blood', 'cell', 'strem', '1')

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
        # Alternating quarter circles are tangent at all four joins; diagonal mass is intentional.
        self.path('cell',(6,30),[('A',(18,42),12,12,False),('A',(42,18),24,24,False),('A',(30,6),12,12,False),('A',(6,30),24,24,False)],True)
        self.path('depression',(16,27),[('A',(21,32),5,5,False),('A',(32,21),11,11,False),('A',(27,16),5,5,False),('A',(16,27),11,11,False)],True)
