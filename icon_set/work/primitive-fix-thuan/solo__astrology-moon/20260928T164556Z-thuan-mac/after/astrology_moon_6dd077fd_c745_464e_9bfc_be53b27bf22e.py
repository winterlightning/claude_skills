"""astrology moon.
Before review: The crescent was an elongated D with flattened tips, unlike the round lunar outline.
Feedback: Manual fix request
Revision: Replaced the elliptical-looking outline with a circular outer lunar arc and a smooth concave inner arc.
Construction: Lucide moon: coherent circular crescent contours; retained source direction.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 VRECT_L; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6dd077fd-c745-464e-9bfc-be53b27bf22e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__astrology-moon/20260928T164556Z-thuan-mac/reference/astrology moon_6dd077fd-c745-464e-9bfc-be53b27bf22e.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'astrology-moon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('astrology', 'moon')
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

        self.add_arc('outer',(8,8),(8,40),radius_x=20,radius_y=20,large_arc=True,sweep=True)
        self.add_arc('inner',(8,40),(8,8),radius_x=16,radius_y=16,sweep=False)
        self.add_contour('moon','outer','inner',closed=True)
