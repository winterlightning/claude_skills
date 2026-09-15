"""A person balances on one leg with the torso and rear leg extended horizontally and the arms reaching forward above the head. A larger head follows the horizontal torso axis.
Reference: Shared human_ref/full_body_ref.png; balancing stick / Warrior III action. Head outline to neck: 13 minus radius 5 equals 8 centerline units, leaving 4 units of ink clearance.
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8425ffa-e3c5-5bfe-8ef8-8629d46590cf'
SOURCE_PATH = 'pictographic-primitives/sports/yoga balancing stick pose_b8425ffa-e3c5-5bfe-8ef8-8629d46590cf.svg'
AUTHOR = 'gpt-6'

class BalancingStickPoseVariant3(Solo48):
    icon_id = 'balancing-stick-pose-v3'
    variant_of = 'balancing-stick-pose-v2'
    variant_label = 'Revised after specific drawing feedback, 16 September'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('balancing', 'stick', 'pose')

    def build(self):
        # Symbol plan: A person balances on one leg with the torso and rear leg extended horizontally and the arms reaching forward above the head. A larger head follows the horizontal torso axis.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('head',(7,21),[('A',(17,21),5,5,True),('A',(7,21),5,5,True)],True)
        line('torso',(25,21),(34,21));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        path('arms',(25,21),[('L',(25,13)),('C',(20,8),(25,10),(23,8)),('L',(4,8))]);join('arms','torso')
        line('raised-leg',(34,21),(44,21));line('standing-leg',(34,21),(28,40));join('raised-leg','torso');join('standing-leg','torso');join('raised-leg','standing-leg')
