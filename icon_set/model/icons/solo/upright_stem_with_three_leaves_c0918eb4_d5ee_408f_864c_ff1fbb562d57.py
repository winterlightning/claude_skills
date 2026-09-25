"""Growing Plant Sprout.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Three pointed leaves join a common upright stem; the lower right leaf preserves the asymmetric growth pattern.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: sprout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0918eb4-d5ee-408f-864c-ff1fbb562d57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beanstalk_c0918eb4-d5ee-408f-864c-ff1fbb562d57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-stem-with-three-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('upright', 'stem', 'with', 'three', 'leaves')

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

        poly('stem',(24,4),(24,16),(24,28),(24,40),(24,44))
        path('leaf-left',(24,16),[('C',(8,4),(10,16),(8,10)),('C',(24,16),(18,4),(24,8))],True);join('leaf-left','stem')
        path('leaf-right-top',(24,16),[('C',(40,4),(24,8),(30,4)),('C',(24,16),(40,10),(38,16))],True);join('leaf-right-top','stem');join('leaf-right-top','leaf-left')
        path('leaf-right-low',(24,40),[('C',(40,28),(24,32),(30,28)),('C',(24,40),(40,36),(34,40))],True);join('leaf-right-low','stem')
