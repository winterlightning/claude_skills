"""The rejected glider is an angular airplane symbol with upright wing shapes; the source has a long diagonal wing across a low fuselage and a single raised tail. Restore the diagonal crossing and rounded wing/fuselage ends.
Plan: HRECT_L; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: Lucide plane: coherent wing/body contours, rounded nose. Deliberate perspective asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '249c7e0d-99c5-4ccf-8b85-f5f836768f7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__glider-in-three-quarter-view-batch-057/20260929T105027Z-thuan-mac/reference/glider_249c7e0d-99c5-4ccf-8b85-f5f836768f7b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'glider-in-three-quarter-view-batch-057'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('glider', 'in', 'three', 'quarter', 'view', 'batch', '057')

    def build(self):

        def path(n,start,*commands,closed=False):
            here=start; members=[]
            for j,cmd in enumerate(commands):
                k=f'{n}-{j}';kind,end,*args=cmd
                if kind=='L': self.add_line(k,here,end)
                elif kind=='A': self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def bez(n,a,*parts):self.add_bezier(n,a,*parts)
        def arc(n,a,b,r,ry=None,s=True):self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(a,b):self.relate('connect',a,b)
        def rect(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        path('wing',(8,32),('L',(16,26)),('L',(24,21)),('L',(40,10)),('C',(44,12),(44,8),(44,8)),('L',(44,18)),('L',(31,29)),('L',(18,40)),('C',(8,36),(12,40),(8,40)),('L',(8,32)),closed=True)
        path('tail',(16,26),('L',(6,22)),('L',(4,8)),('L',(10,8)),('L',(16,20)),('L',(24,21)));join('tail','wing')
        bez('nose',(24,21),((35,21),(42,24),(42,28)),((42,33),(36,31),(31,29)));join('nose','wing')
