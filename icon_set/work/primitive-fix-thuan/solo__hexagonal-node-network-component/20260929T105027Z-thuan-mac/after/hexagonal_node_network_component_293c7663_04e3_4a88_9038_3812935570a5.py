"""The rejected migration network omits the upward arrow and internal chevrons. Restore an upward migration arrow within the connected network; simplify chevron repetition for spacing.
Plan: SQUARE; exact SOLO48 centerline envelope, stroke4, integer coordinates.
Construction: No exact Lucide migration match: shared node radii, symmetric edges and upward arrow; repeated chevrons reduced to one.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '293c7663-04e3-4a88-9038-3812935570a5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hexagonal-node-network-component/20260929T105027Z-thuan-mac/reference/migration hub_293c7663-04e3-4a88-9038-3812935570a5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hexagonal-node-network-component'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hexagonal', 'node', 'network', 'component')

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
        for n,x,y in [('ul',9,17),('ur',39,17),('ll',9,32),('lr',39,32),('bottom',24,39)]:circle(n,x,y,3)
        line('left',(9,20),(9,29));join('left','ul');join('left','ll')
        line('right',(39,20),(39,29));join('right','ur');join('right','lr')
        line('lower-left',(12,32),(21,39));join('lower-left','ll');join('lower-left','bottom')
        line('lower-right',(36,32),(27,39));join('lower-right','lr');join('lower-right','bottom')
        poly('arrow',(20,12),(24,6),(28,12));line('shaft',(24,6),(24,24));join('arrow','shaft')
