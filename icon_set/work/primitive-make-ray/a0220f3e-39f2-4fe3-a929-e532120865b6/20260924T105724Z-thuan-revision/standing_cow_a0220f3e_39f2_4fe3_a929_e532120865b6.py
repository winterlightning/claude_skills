"""Left-facing cow with broad muzzle, small horn, rounded rump and belly; simplified two legs and tail retain the source silhouette. No exact Lucide cow match; related animal contour principles."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a0220f3e-39f2-4fe3-a929-e532120865b6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-cow/20260924T105724Z-thuan-mac/reference/cattle_a0220f3e-39f2-4fe3-a929-e532120865b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-cow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('standing', 'cow')

    def build(self):
        # Plan: Left-facing cow with broad muzzle, small horn, rounded rump and belly; simplified two legs and tail retain the source silhouette. No exact Lucide cow match; related animal contour principles.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path('body',(10,12),[('L',(9,8)),('C',(22,14),(14,12),(17,14)),('L',(38,14)),('A',(44,20),6,6,True),('L',(44,22)),('A',(36,30),8,8,True),('L',(18,30)),('C',(10,22),(13,30),(12,25)),('L',(6,23)),('C',(4,19),(4,23),(4,22)),('L',(10,12))],True)
        line('front-leg',(18,30),(18,40));join('body','front-leg')
        poly('hind-leg',(36,30),(38,34),(38,40));join('body','hind-leg')
        path('tail',(44,22),[('L',(44,32))]);join('body','tail')
