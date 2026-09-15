"""Sorting arrow beside a clear 1-over-9 pair; consistent line terminals and a round 9 counter, kept as solo.
References: Lucide arrow-down-0-1: numeric sorting layout.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '774a187b-a625-438b-9b84-1427193ca713'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arrange number_774a187b-a625-438b-9b84-1427193ca713.svg'
AUTHOR = 'gpt-6'

class ArrangeNumberVariant2(Solo48):
    icon_id = 'arrange-number-v2'
    variant_of = 'arrange-number'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('arrange', 'number')

    def build(self):
        # Symbol plan: Sorting arrow beside a clear 1-over-9 pair; consistent line terminals and a round 9 counter, kept as solo.

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
        poly('arrow',(8,32),(14,40),(20,32));line('shaft',(14,4),(14,40));join('shaft','arrow')
        poly('one',(32,8),(36,4),(36,17))
        circle('nine',35,31,5);path('tail',(40,31),[('L',(40,36)),('A',(32,44),8,8,True)]);join('nine','tail')
