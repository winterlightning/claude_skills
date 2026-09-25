"""Group of Two People.

Plan: HRECT_L, centerline extremes (4, 8, 44, 40); 48 x 48, stroke 4.
Two equal circular heads and broad paired shoulder arches retain the two-person subject.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: Shared human_ref/user.svg bust construction and local Lucide users-round; human-reference.md proportions..
Circular jaw to shoulder top is exactly 4 centerline units, giving the shared bust ink tangency; this is not a detached stick-figure neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ba5d5a7-9511-4125-be0c-1c52ca129a78'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crewmen_6ba5d5a7-9511-4125-be0c-1c52ca129a78.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-people-with-curved-necklines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    human_construction = "bust"
    aliases = ()
    keywords = ('two', 'people', 'with', 'curved', 'necklines')

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

        for j,x in enumerate([12,36]):
         circle(f'head-{j}',x,14,6)
         path(f'body-{j}',(x-8,40),[('L',(x-8,32)),('A',(x,24),8,8,True),('A',(x+8,32),8,8,True),('L',(x+8,40))]);join(f'head-{j}',f'body-{j}')
