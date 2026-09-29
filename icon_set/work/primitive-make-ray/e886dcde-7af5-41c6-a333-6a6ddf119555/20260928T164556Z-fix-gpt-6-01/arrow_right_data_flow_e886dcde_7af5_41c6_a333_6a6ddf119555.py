"""coding apps website big data arrow.
Before review: The central arrow was too short with a tiny head, and broad flattened U shapes dominated the data rows.
Feedback: Manual fix request
Revision: Lengthened the arrow, opened its head and narrowed the U interruptions; retained repeated ticks in both rows.
Construction: Lucide arrow-right: long shaft and open equal-arm head.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 HRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e886dcde-7af5-41c6-a333-6a6ddf119555'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-right-data-flow/20260928T164556Z-thuan-mac/reference/coding apps website big data arrow_e886dcde-7af5-41c6-a333-6a6ddf119555.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'arrow-right-data-flow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('coding', 'apps', 'website', 'big', 'data', 'arrow')
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

        for side in (-1,1):
            y=lambda d:24+side*d
            prefix='top' if side<0 else 'bottom'
            for j,x in enumerate((4,12,20)):
                line(f'{prefix}-tick-{j}',(x,y(16)),(x,y(11)))
            path(prefix+'-u',(32,y(16)),[(32,y(10)),((44,y(10)),6,5,side>0),(44,y(16))])
        line('shaft',(4,24),(34,24));poly('head',(28,18),(34,24),(28,30));join('shaft','head')
