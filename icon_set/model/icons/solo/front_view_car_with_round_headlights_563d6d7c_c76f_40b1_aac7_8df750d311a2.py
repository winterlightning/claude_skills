"""Front Facing Car.

Plan: Symmetric windshield, bumper, round headlights and tires. Bounds4,8,44,40.
Construction reference: car-front.
Final review: Enlarged bumper for two headlight marks.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '563d6d7c-c76f-40b1-aac7-8df750d311a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/drive_563d6d7c-c76f-40b1-aac7-8df750d311a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-view-car-with-round-headlights'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('front', 'view', 'car', 'with', 'round', 'headlights')

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

        rect('bumper',4,18,40,18,3)
        poly('windshield',(8,18),(14,8),(34,8),(40,18));join('windshield','bumper')
        line('tire-left',(10,36),(10,40));line('tire-right',(38,36),(38,40));join('tire-left','bumper');join('tire-right','bumper')
        line('light-left',(14,27),(14,27));line('light-right',(34,27),(34,27))
