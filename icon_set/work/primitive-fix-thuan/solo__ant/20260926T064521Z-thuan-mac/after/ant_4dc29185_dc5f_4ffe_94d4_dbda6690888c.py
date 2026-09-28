"""A clear head and broad abdomen linked by a thorax; two mirrored pairs of legs retain the requested removal of the middle pair.
References: Lucide bug and supplied ant; saved request for four leg strokes.
Authored directly on SOLO48; original retained for comparison."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ant/20260926T064521Z-thuan-mac/reference/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'claude-opus-5-5'

class Ant(Solo48):
    icon_id = 'ant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('ant',)

    def build(self):
        # Symbol plan: A clear head and broad abdomen linked by a thorax; two mirrored pairs of legs retain the requested removal of the middle pair.

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
        # Revision per review: the middle legs sit higher and curve upward, the lower legs curve
        # downward. The legs leave the thorax at (24, 22), exactly 8 from both the r5 head (bottom
        # (24, 14)) and the r7 abdomen (top (24, 30)) on the centre line, first horizontally and
        # then sweeping up to (8, 14)/(40, 14); the lower legs leave the abdomen's sides and sweep
        # down to (8, 44)/(40, 44).
        circle('head',24,9,5);circle('abdomen',24,37,7)
        line('thorax-upper',(24,14),(24,22));line('thorax-lower',(24,22),(24,30))
        self.add_contour('thorax','thorax-upper','thorax-lower')
        join('head','thorax');join('thorax','abdomen')
        for side in (-1,1):
         x=lambda d:24+side*d
         poly(f'antenna-{side}',(x(4),6),(x(7),4),(x(14),4));join('head',f'antenna-{side}')
         self.add_bezier(f'middle-leg-{side}',(24,22),((x(8),22),(x(14),20),(x(16),14)));join('thorax',f'middle-leg-{side}')
         self.add_bezier(f'lower-leg-{side}',(x(7),37),((x(11),37),(x(15),40),(x(16),44)));join('abdomen',f'lower-leg-{side}')
        join('middle-leg--1','middle-leg-1')
