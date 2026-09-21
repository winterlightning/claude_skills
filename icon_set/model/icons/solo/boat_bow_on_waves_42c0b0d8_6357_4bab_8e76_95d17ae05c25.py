"""Front View Boat on Water.

Plan: Front boat hull with cabin and waterline. Bounds4,8,44,40.
Construction reference: ship.
Final review: Omitted wave detail to preserve hull, cabin and bow.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42c0b0d8-6357-4bab-8e76-95d17ae05c25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boatload_42c0b0d8-6357-4bab-8e76-95d17ae05c25.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boat-bow-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('boat', 'bow', 'on', 'waves')

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

        poly('hull',(4,22),(24,16),(44,22),(38,36),(24,40),(10,36),closed=True)
        poly('cabin',(12,20),(12,8),(36,8),(36,20));join('cabin','hull')
        line('bow',(24,16),(24,40));join('bow','hull')
