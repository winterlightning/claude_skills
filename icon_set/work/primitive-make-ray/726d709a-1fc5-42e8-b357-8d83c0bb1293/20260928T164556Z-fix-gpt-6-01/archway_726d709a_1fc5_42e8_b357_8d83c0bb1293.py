"""archway.
Before review: The shallow opening and very short vertical legs read more like a horseshoe than a doorway.
Feedback: Manual fix request
Revision: Extended the straight jambs and rebuilt concentric semicircular arches with uniform masonry thickness.
Construction: No useful direct Lucide archway match; concentric circular construction from source.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '726d709a-1fc5-42e8-b357-8d83c0bb1293'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__archway/20260928T164556Z-thuan-mac/reference/archway_726d709a-1fc5-42e8-b357-8d83c0bb1293.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'archway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('archway',)
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

        path('arch',(6,42),[(6,24),((42,24),18,18,True),(42,42),(34,42),(34,24),((14,24),10,10,False),(14,42),(6,42)],True)
