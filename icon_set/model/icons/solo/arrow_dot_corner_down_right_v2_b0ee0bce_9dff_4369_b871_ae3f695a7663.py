"""Equal diagonal dashes feed one right-angle arrowhead with matching arms; keep as solo.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b0ee0bce-9dff-4369-b871-ae3f695a7663'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot corner down right_b0ee0bce-9dff-4369-b871-ae3f695a7663.svg'
AUTHOR = 'gpt-6'

class ArrowDotCornerDownRightVariant2(Solo48):
    icon_id = 'arrow-dot-corner-down-right-v2'
    variant_of = 'arrow-dot-corner-down-right'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'dot', 'corner', 'down', 'right')

    def build(self):
        # Symbol plan: Equal diagonal dashes feed one right-angle arrowhead with matching arms; keep as solo.

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
        line('dash-0',(6,6),(10,10));line('dash-1',(16,16),(20,20));line('shaft',(26,26),(42,42))
        poly('head',(24,42),(42,42),(42,24));join('shaft','head')
