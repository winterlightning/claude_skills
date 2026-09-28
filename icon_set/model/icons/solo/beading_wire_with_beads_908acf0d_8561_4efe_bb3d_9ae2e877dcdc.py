"""One continuous U-shaped wire carries three consistent rounded beads. The strand joins each bead at its midpoint and remains clear between beads.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '908acf0d-8561-4efe-bb3d-9ae2e877dcdc'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/diy bead_908acf0d-8561-4efe-bb3d-9ae2e877dcdc.svg'
AUTHOR = 'gpt-6'

class BeadingWireWithBeads(Solo48):
    icon_id = 'beading-wire-with-beads'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('beading', 'wire', 'with', 'beads')

    def build(self):
        # Symbol plan: One continuous U-shaped wire carries three consistent rounded beads. The strand joins each bead at its midpoint and remains clear between beads.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        box('left-bead',4,8,16,20,4);box('bottom-bead',18,28,30,40,4);box('right-bead',32,8,44,20,4)
        path('wire-left',(10,20),[('L',(10,26)),('A',(18,34),8,8,False)]);join('wire-left','left-bead');join('wire-left','bottom-bead')
        path('wire-right',(30,34),[('A',(38,26),8,8,False),('L',(38,20))]);join('wire-right','bottom-bead');join('wire-right','right-bead')
