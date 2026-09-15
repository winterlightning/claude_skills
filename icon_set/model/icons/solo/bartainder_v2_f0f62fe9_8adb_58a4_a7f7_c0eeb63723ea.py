"""A bartender holds a stemmed cocktail in one bent arm. The circular head follows the vertical torso axis with exactly four units of detached ink clearance.
References: Shared full_body_ref.png for limbs and exact detached head; supplied bartender subject.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea'
SOURCE_PATH = 'pictographic-primitives/avatars/bartainder_f0f62fe9-8adb-58a4-a7f7-c0eeb63723ea.svg'
AUTHOR = 'gpt-6'

class BartainderVariant2(Solo48):
    icon_id = 'bartainder-v2'
    variant_of = 'bartainder'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/occupations'
    aliases = ()
    keywords = ('bartainder',)

    def build(self):
        # Symbol plan: A bartender holds a stemmed cocktail in one bent arm. The circular head follows the vertical torso axis with exactly four units of detached ink clearance.

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
        circle('head',12,14,6)
        line('torso',(12,28),(12,40));self.mark_human_figure('bartender',head='head',torso='torso',torso_junction='start')
        poly('left-arm',(12,28),(4,36),(4,40));poly('serving-arm',(12,28),(24,36),(36,36));join('torso','left-arm');join('torso','serving-arm');join('left-arm','serving-arm')
        poly('glass',(28,16),(44,16),(36,28),closed=True);line('stem',(36,28),(36,36));join('glass','stem');join('stem','serving-arm')
