"""collard.
Before review: The leaf was squat and the vein arms met at almost the same height rather than alternating.
Feedback: Manual fix request
Revision: Rebuilt a taller gently lobed leaf with staggered left/right veins and a clear lower stem.
Construction: Lucide leaf: one coherent blade and sparse branching vein structure.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9fd1fed0-8147-4343-8f7f-8d36e34e9107'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__collard-leaf-with-alternating-veins/20260928T164649Z-thuan-mac/reference/collard_9fd1fed0-8147-4343-8f7f-8d36e34e9107.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'collard-leaf-with-alternating-veins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('collard',)
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('leaf',(24,4),[('C',(33,10),(29,4),(29,8)),('C',(38,19),(38,11),(39,14)),('C',(40,27),(37,23),(40,23)),('C',(30,37),(40,31),(34,34)),('C',(24,40),(28,39),(27,40)),('C',(18,37),(21,40),(20,39)),('C',(8,27),(14,34),(8,31)),('C',(10,19),(8,23),(11,23)),('C',(15,10),(9,14),(10,11)),('C',(24,4),(19,8),(19,4))],True)
        poly('stem',(24,12),(24,22),(24,30),(24,40),(24,44));join('stem','leaf')
        line('left-vein',(17,16),(24,22));line('right-vein',(24,30),(31,24));join('left-vein','stem');join('right-vein','stem')
