"""A broad stone bridge with one clear rounded arch and a single smooth water wave. Give the deck and arch genuine space.
References: Lucide bridge and supplied stone bridge; simplified single arch requested in feedback.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'

class ArchedStoneBridgeVariant2(Solo48):
    icon_id = 'arched-stone-bridge-v2'
    variant_of = 'arched-stone-bridge'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('arched', 'stone', 'bridge')

    def build(self):
        # Symbol plan: A broad stone bridge with one clear rounded arch and a single smooth water wave. Give the deck and arch genuine space.

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
        line('deck',(4,8),(44,8))
        path('bridge',(4,8),[('L',(4,27)),('L',(14,27)),('L',(14,26)),('A',(34,26),10,10,True),('L',(34,27)),('L',(44,27)),('L',(44,8))]);join('deck','bridge')
        path('water',(4,38),[('A',(24,38),10,2,True),('A',(44,38),10,2,False)])
