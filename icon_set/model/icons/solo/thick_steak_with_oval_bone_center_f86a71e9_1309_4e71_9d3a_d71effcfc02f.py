"""Fresh Raw Bone-In Beef Steak.

Plan: Asymmetric broad steak with a round bone and lower thickness seam. Bounds4,8,44,40.
Construction reference: beef.
Final review: Omitted lower thickness seam; retained asymmetrical steak and bone.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f86a71e9-1309-4e71-9d3a-d71effcfc02f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steak_f86a71e9-1309-4e71-9d3a-d71effcfc02f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thick-steak-with-oval-bone-center'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('thick', 'steak', 'with', 'oval', 'bone', 'center')

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

        path('steak',(4,24),[('C',(18,8),(4,14),(10,8)),('C',(34,18),(28,8),(28,16)),('C',(44,26),(40,18),(44,20)),('C',(24,40),(44,36),(34,40)),('C',(4,24),(10,40),(4,34))],True)
        circle('bone',18,22,4)
