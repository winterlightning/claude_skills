"""A smooth headlamp, three equal beams and a curved upper direction indicator. The lamp face is reduced to leave genuine separation from the indicator.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '60239e6a-5e58-4c70-a436-9fa4c1208587'
SOURCE_PATH = 'pictographic-primitives/transportation/adaptive light 1_60239e6a-5e58-4c70-a436-9fa4c1208587.svg'
AUTHOR = 'gpt-6'

class AdaptiveHeadlight(Solo48):
    icon_id = 'adaptive-headlight'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('adaptive', 'headlight')

    def build(self):
        # Symbol plan: A smooth headlamp, three equal beams and a curved upper direction indicator. The lamp face is reduced to leave genuine separation from the indicator.

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
        path('lamp',(30,22),[('A',(30,40),14,9,True),('L',(30,22))],True)
        for j in range(3):line(f'beam-{j}',(4,20+10*j),(17,16+10*j))
        path('turn',(24,8),[('L',(36,8)),('A',(44,16),8,8,True)])
        poly('tip',(38,14),(44,16),(44,8));join('turn','tip')
