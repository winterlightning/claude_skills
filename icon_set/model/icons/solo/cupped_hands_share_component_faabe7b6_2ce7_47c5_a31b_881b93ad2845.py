"""Full reference: three linked sharing nodes held above mirrored cupped hands. Lucide hand informs clean curved palms. Restore share symbol missing from rejected drawing; fingers reduced to single coherent strokes.
Keyshape VRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'faabe7b6-2ce7-47c5-a31b-881b93ad2845'
SOURCE_PATH = 'pictographic-primitives/school-learning/e learning share_faabe7b6-2ce7-47c5-a31b-881b93ad2845.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cupped-hands-share-component'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/school-learning"
    aliases=()
    keywords=('cupped', 'hands', 'share', 'component')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        circle('share-top',24,7,3);circle('share-left',14,19,3);circle('share-right',34,19,3)
        line('link-left',(24,10),(14,16));line('link-right',(24,10),(34,16))
        for a,b in [('share-top','link-left'),('share-left','link-left'),('share-top','link-right'),('share-right','link-right')]:join(a,b)
        for j,s in enumerate((-1,1)):
            def p(x,y):return (24+s*x,y)
            path(f'hand-{j}',p(16,29),[('L',p(16,32)),('C',p(8,40),p(16,36),p(8,36)),('L',p(8,44))])
            path(f'thumb-{j}',p(8,40),[('C',p(4,32),p(8,36),p(6,34))]);join(f'hand-{j}',f'thumb-{j}')
        join('link-left','link-right')
