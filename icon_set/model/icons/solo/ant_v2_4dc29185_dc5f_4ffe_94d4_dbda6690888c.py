"""Three recognizable body segments linked on a vertical axis. Four leg strokes preserve the prior feedback to remove the middle pair; antennae and remaining legs mirror.
References: Lucide bug: coherent body and mirrored limb attachments; supplied ant and saved feedback.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'pictographic-primitives/animals/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'gpt-6'

class AntVariant2(Solo48):
    icon_id = 'ant-v2'
    variant_of = 'ant'
    variant_label = 'Reconstructed solo drawing after rejection'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('ant',)

    def build(self):
        # Symbol plan: Three recognizable body segments linked on a vertical axis. Four leg strokes preserve the prior feedback to remove the middle pair; antennae and remaining legs mirror.

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
        circle('head',24,12,5)
        circle('abdomen',24,36,8)
        line('thorax',(24,17),(24,28));join('head','thorax');join('thorax','abdomen')
        for side in (-1,1):
         x=lambda d:24+side*d
         poly(f'antenna-{side}',(x(4),9),(x(9),4),(x(16),4));join('head',f'antenna-{side}')
         poly(f'front-leg-{side}',(24,22),(x(12),18),(x(16),12));join('thorax',f'front-leg-{side}')
         poly(f'rear-leg-{side}',(24,28),(x(12),34),(x(16),44));join('thorax',f'rear-leg-{side}');join('abdomen',f'rear-leg-{side}')
        join('front-leg--1','front-leg-1');join('rear-leg--1','rear-leg-1')
