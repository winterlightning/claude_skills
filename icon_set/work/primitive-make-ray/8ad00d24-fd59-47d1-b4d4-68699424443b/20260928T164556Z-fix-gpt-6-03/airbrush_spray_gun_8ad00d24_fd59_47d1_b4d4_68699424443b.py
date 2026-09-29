"""airbrush.
Before review: The upright trapezoid cup and angular grip lost the tilted paint reservoir and natural airbrush profile.
Feedback: Manual fix request
Revision: Restored the tilted rounded paint cup, tapered nozzle, rounded grip and curved trigger.
Construction: No useful exact Lucide match; source supplies the tilted cup and grip.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ad00d24-fd59-47d1-b4d4-68699424443b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__airbrush-spray-gun/20260928T164556Z-thuan-mac/reference/airbrush_8ad00d24-fd59-47d1-b4d4-68699424443b.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'airbrush-spray-gun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('airbrush',)
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

        path('body',(6,30),[(12,26),(20,26),(37,26),((42,31),5,5,True),(38,34),(41,40),('C',(38,42),(41,42),(40,42)),(34,42),(29,34),(25,34),(12,34),(6,30)],True)
        poly('cup',(24,6),(36,12),(30,20),(24,17),(18,14),closed=True)
        line('neck',(24,17),(20,26));join('neck','body');join('neck','cup')
        path('trigger',(25,34),[((19,41),7,7,True),(17,40)])
        join('trigger','body')
