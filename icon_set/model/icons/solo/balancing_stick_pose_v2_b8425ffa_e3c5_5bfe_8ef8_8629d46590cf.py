"""One horizontal torso, forward arm and rear raised leg with a supporting leg at the hip. Circular head lies along the upper-torso axis with exactly four units of detached ink gap.
References: Shared full_body_ref.png: coherent torso/limbs and exact detached head gap; source balance pose.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8425ffa-e3c5-5bfe-8ef8-8629d46590cf'
SOURCE_PATH = 'pictographic-primitives/sports/yoga balancing stick pose_b8425ffa-e3c5-5bfe-8ef8-8629d46590cf.svg'
AUTHOR = 'gpt-6'

class BalancingStickPoseVariant2(Solo48):
    icon_id = 'balancing-stick-pose-v2'
    variant_of = 'balancing-stick-pose'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('balancing', 'stick', 'pose')

    def build(self):
        # Symbol plan: One horizontal torso, forward arm and rear raised leg with a supporting leg at the hip. Circular head lies along the upper-torso axis with exactly four units of detached ink gap.

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
        circle('head',12,20,4)
        line('torso',(24,20),(34,20));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        path('raised-arm',(24,20),[('L',(24,12)),('A',(20,8),4,4,False),('L',(4,8))]);join('torso','raised-arm')
        line('rear-leg',(34,20),(44,20));line('support-leg',(34,20),(28,40));join('torso','rear-leg');join('torso','support-leg');join('rear-leg','support-leg')
