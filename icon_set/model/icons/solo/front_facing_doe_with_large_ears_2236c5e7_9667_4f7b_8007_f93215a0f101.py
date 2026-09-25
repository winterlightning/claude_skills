"""Female Deer Face.

Plan: Doe with spreading pointed ears and tapered rounded muzzle, bounds8,4,40,44. Drop tiny eyes; retain ears and nose.
Construction reference: No useful local Lucide match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2236c5e7-9667-4f7b-8007-f93215a0f101'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/doe_2236c5e7-9667-4f7b-8007-f93215a0f101.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'front-facing-doe-with-large-ears'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('front', 'facing', 'doe', 'with', 'large', 'ears')

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

        path('face',(16,18),[('C',(32,18),(20,14),(28,14)),('C',(30,36),(36,22),(32,30)),('C',(24,44),(28,41),(26,44)),('C',(18,36),(22,44),(20,41)),('C',(16,18),(16,30),(12,22))],True)
        path('ear-left',(16,18),[('C',(8,4),(8,16),(8,8)),('C',(16,18),(18,6),(20,12))],True)
        path('ear-right',(32,18),[('C',(40,4),(28,12),(30,6)),('C',(32,18),(40,8),(40,16))],True)
        join('face','ear-left');join('face','ear-right')
        line('nose',(23,25),(25,25))
