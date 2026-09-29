"""toys clown.
Before review: The head sat too high and the neck ribbons were detached blobs instead of flowing strands.
Feedback: Manual fix request
Revision: Enlarged the round blank face, refined the three-lobed side hair and attached two smooth curling ribbons to the jaw.
Construction: human_ref/user.svg: circular head; source supplies side hair and ribbon curls.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 HRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e2bcf431-3007-4ec7-b2de-330eff155339'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__clown-head-with-side-hair/20260928T164649Z-thuan-mac/reference/toys clown_e2bcf431-3007-4ec7-b2de-330eff155339.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'clown-head-with-side-hair'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('toys', 'clown')
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

        # Circular head split at exact integer 5-12-13 attachment nodes.
        nodes=[(24,8),(36,16),(37,21),(36,26),(29,33),(24,34),(19,33),(12,26),(11,21),(12,16),(24,8)]
        path('head',nodes[0],[(p,13,13,True) for p in nodes[1:]],True)
        path('hair-left',(12,16),[((8,17),4,4,False),((8,25),4,4,False),((12,26),4,4,False)])
        path('hair-right',(36,16),[((40,17),4,4,True),((40,25),4,4,True),((36,26),4,4,True)])
        join('hair-left','head');join('hair-right','head')
        path('ribbon-left',(19,33),[((17,37),4,4,False),((18,40),3,3,True)])
        path('ribbon-right',(29,33),[((31,37),4,4,True),((30,40),3,3,False)])
        join('ribbon-left','head');join('ribbon-right','head')
