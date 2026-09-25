"""Female User Profile Avatar.

Plan: Circular jaw radius7; shoulders top29 and jawbottom25 give zero visible ink gap. Hair remains a distinct identifying silhouette; bounds8,4,40,44. Simplify sleeve seams.
Construction reference: human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70680864-6c30-4596-a23a-894be18bdc1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/step aunt_70680864-6c30-4596-a23a-894be18bdc1d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-woman-with-rounded-bob'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('front', 'facing', 'woman', 'with', 'rounded', 'bob')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        self.add_arc('jaw',(17,18),(31,18),radius_x=7,radius_y=7,sweep=False)
        self.add_bezier('fringe-right',(31,18),((31,16),(24,16),(22,12)))
        self.add_bezier('fringe-left',(22,12),((20,16),(17,16),(17,18)))
        self.add_contour('face','jaw','fringe-right','fringe-left',closed=True)
        line('body-left-side',(8,44),(8,37))
        self.add_arc('body-left-shoulder',(8,37),(16,29),radius_x=8)
        line('body-top',(16,29),(32,29))
        self.add_arc('body-right-shoulder',(32,29),(40,37),radius_x=8)
        line('body-right-side',(40,37),(40,44))
        self.add_contour('shoulders','body-left-side','body-left-shoulder','body-top','body-right-shoulder','body-right-side')
        join('face','shoulders')
        path('hair',(8,37),[("L",(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),("L",(40,37))])
        join('hair','shoulders')
