"""Restore a broad circular rotation loop with a clear arrow and smooth sweeping internal curve.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: VRECT_L for the subject's natural orientation.
Construction: Lucide rotate-cw: coherent curved loop and open arrowhead.
Reduction: No defining feature omitted; intentional open upper-right loop retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '30e56ade-c3d8-5998-a5e2-8711b05ffd45'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__deepfake-rotate/20260925T083122Z-thuan-mac/reference/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Allow a 2-unit wider loop than VRECT_L so the rotation mark remains circular rather than an elongated oval. The 48px canvas and 4px stroke are retained; loop, arrow and inner sweep are clear at native size in both themes.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'df6ee87dcbfe64d898df1524504aef0a1e82f4e044e925693a5d5acd48c7e5e5'}
    icon_id = 'deepfake-rotate'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('deepfake', 'rotate')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('loop',(36,13),[('C',(42,26),(40,17),(42,21)),('C',(39,36),(42,30),(41,33)),('C',(24,44),(35,41),(30,44)),('A',(6,26),18,18,True),('C',(12,12),(6,20),(8,15)),('C',(28,10),(17,8),(23,10))])
        poly('arrow',(22,4),(28,10),(22,16));join('arrow','loop')
        path('sweep',(12,12),[('C',(39,36),(15,25),(27,35))]);join('sweep','loop')
