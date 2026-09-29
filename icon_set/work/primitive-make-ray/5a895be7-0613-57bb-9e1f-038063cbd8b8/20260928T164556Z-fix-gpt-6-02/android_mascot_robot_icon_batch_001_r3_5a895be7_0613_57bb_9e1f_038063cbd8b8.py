"""android.
Before review: The squat dome, short torso and cramped leg gap made the mascot heavier than the original.
Feedback: Manual fix request
Revision: Raised the dome, lengthened the blank torso and widened the separation of the rounded legs while retaining the reference’s armless blank face.
Construction: Lucide bot: clear head/body hierarchy; reference owns mascot silhouette.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a895be7-0613-57bb-9e1f-038063cbd8b8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__android-mascot-robot-icon-batch-001-r3/20260928T164556Z-thuan-mac/reference/android_5a895be7-0613-57bb-9e1f-038063cbd8b8.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'android-mascot-robot-icon-batch-001-r3'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('android',)
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

        path('outline',(8,20),[((12,12),10,10,True),((36,12),20,20,True),((40,20),10,10,True),(40,32),((36,36),4,4,True),(36,40),((28,40),4,4,True),(28,36),(20,36),(20,40),((12,40),4,4,True),(12,36),((8,32),4,4,True),(8,20)],True)
        line('seam',(8,20),(40,20));join('outline','seam')
        line('antenna-left',(12,12),(8,4));line('antenna-right',(36,12),(40,4))
        join('antenna-left','outline');join('antenna-right','outline')
