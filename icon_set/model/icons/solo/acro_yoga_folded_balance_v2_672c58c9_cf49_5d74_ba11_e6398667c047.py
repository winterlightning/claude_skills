"""Two people in a folded supporting balance; shared hand/foot contacts form the acro pose while each head is paired with its actual torso.
References: Shared full_body_ref.png and supplied two-person folded balance.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '672c58c9-cf49-5d74-ba11-e6398667c047'
SOURCE_PATH = 'pictographic-primitives/sports/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg'
AUTHOR = 'gpt-6'

class AcroYogaFoldedBalanceVariant2(Solo48):
    icon_id = 'acro-yoga-folded-balance-v2'
    variant_of = 'acro-yoga-folded-balance'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('acro', 'yoga', 'folded', 'balance')

    def build(self):
        # Symbol plan: Two people in a folded supporting balance; shared hand/foot contacts form the acro pose while each head is paired with its actual torso.

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
        circle('lower-head',10,36,4)
        line('lower-torso',(22,36),(34,36));self.mark_human_figure('base-person',head='lower-head',torso='lower-torso',torso_junction='start')
        poly('lower-legs',(34,36),(42,30),(42,42));join('lower-legs','lower-torso')
        poly('base-arm',(22,36),(22,22),(30,22));join('base-arm','lower-torso')
        circle('upper-head',36,10,4)
        line('upper-torso',(24,10),(12,10));self.mark_human_figure('flyer',head='upper-head',torso='upper-torso',torso_junction='start')
        poly('folded-legs',(12,10),(6,18),(18,22));join('folded-legs','upper-torso')
        poly('flyer-arm',(24,10),(22,22),(30,22));join('flyer-arm','upper-torso');join('flyer-arm','base-arm')
