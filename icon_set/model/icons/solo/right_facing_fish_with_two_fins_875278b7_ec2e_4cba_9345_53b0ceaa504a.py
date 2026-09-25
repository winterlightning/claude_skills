"""Simple Carp Fish Symbol.

Plan: Rounded fish body, forked tail and upper/lower fins retained in one coherent silhouette. Omitted the tight gill line and tiny mouth notch. Keyshape HRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide fish: shared fins, tapered body and open tail; no tiny eye or mouth notch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '875278b7-ec2e-4cba-9345-53b0ceaa504a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carp_875278b7-ec2e-4cba-9345-53b0ceaa504a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-facing-fish-with-two-fins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('right', 'facing', 'fish', 'with', 'two', 'fins')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('fish',(14,24),[('C',(24,14),(18,17),(21,14)),('L',(24,8)),('C',(34,14),(30,8),(32,12)),('C',(44,24),(40,16),(42,20)),('C',(34,34),(42,28),(40,32)),('C',(24,40),(32,36),(30,40)),('L',(24,34)),('C',(14,24),(21,34),(18,31)),('L',(4,34)),('L',(4,14)),('L',(14,24))],True)
