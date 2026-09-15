"""An arched faucet with a lever, downward outlet and two spaced falling drops. The spout and stem are one smooth thick outline.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6244934-fcab-4b97-a0d0-7bb5ba491549'
SOURCE_PATH = 'pictographic-primitives/wayfinding/water fountain jet_c6244934-fcab-4b97-a0d0-7bb5ba491549.svg'
AUTHOR = 'gpt-6'

class ArchedTapSprayingWaterVariant2(Solo48):
    icon_id = 'arched-tap-spraying-water-v2'
    variant_of = 'arched-tap-spraying-water'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('arched', 'tap', 'spraying', 'water')

    def build(self):
        # Symbol plan: An arched faucet with a lever, downward outlet and two spaced falling drops. The spout and stem are one smooth thick outline.

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=f'{n}-{j}'
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
        path('tap',(8,44),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,24)),('L',(30,24)),('L',(30,20)),('A',(18,20),6,6,False),('L',(18,44)),('L',(8,44))],True)
        line('drop-0',(30,36),(30,40));line('drop-1',(40,36),(40,40))
