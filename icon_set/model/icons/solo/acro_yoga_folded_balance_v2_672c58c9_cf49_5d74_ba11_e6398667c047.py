"""A folded upper person balances at the supporting hand of a seated lower person. Each head follows its own neck direction; broad open limb shapes replace the cramped angular loops.
References: Shared full_body_ref.png and supplied two-person folded acro-yoga pose.
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
        # Symbol plan: A folded upper person balances at the supporting hand of a seated lower person. Each head follows its own neck direction; broad open limb shapes replace the cramped angular loops.

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
        circle('lower-head',10,38,4)
        line('lower-torso',(22,38),(34,38));self.mark_human_figure('base-person',head='lower-head',torso='lower-torso',torso_junction='start')
        path('lower-legs',(34,38),[('L',(38,38)),('A',(42,34),4,4,False),('L',(42,32))]);join('lower-legs','lower-torso')
        line('supporting-arm',(22,38),(22,22));join('supporting-arm','lower-torso')
        circle('upper-head',34,22,4)
        self.add_bezier('upper-torso',(22,22),((14,22),(22,14),(22,6)))
        self.mark_human_figure('flyer',head='upper-head',torso='upper-torso',torso_junction='start')
        poly('folded-leg',(22,6),(6,14),(6,22));join('folded-leg','upper-torso');join('supporting-arm','upper-torso')
