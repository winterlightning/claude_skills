"""A diagonal wood saw with a rounded closed handle and circular grip aperture. Bounds (6,6)-(42,42); broad blade has two smooth tooth scallops.
Construction reference: Lucide wrench: diagonal tool balance; source waved blade and handle opening.
Omissions: Small oblong handle opening simplified to a circular aperture; fine teeth reduced to two scallops."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH = 'pictographic-primitives/tools/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='wavy-tooth-wood-saw'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/tools"
    aliases=()
    keywords=('tools', 'wood', 'saw')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('handle',(12,18),[('L',(24,18)),('A',(30,24),6,6,True),('L',(30,30)),('L',(30,36)),('A',(24,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,24)),('A',(12,18),6,6,True)],True)
        oval('opening',18,30,3,3)
        path('blade',(24,18),[('L',(38,6)),('L',(42,10)),('L',(42,17)),('C',(37,23),(42,22),(40,23)),('C',(30,30),(37,28),(34,30))]);join('blade','handle')
