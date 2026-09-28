"""Group of Three People.

Plan: HRECT_L, centerline extremes (4, 8, 44, 40); 48 x 48, stroke 4.
Three circular heads and rounded shoulder arches preserve the team; the central figure is taller.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: Shared human_ref/user.svg bust construction and local Lucide users-round; human-reference.md proportions..
Circular jaw to shoulder top is exactly 4 centerline units, giving the shared bust ink tangency; this is not a detached stick-figure neck.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70088ee7-6460-4eaa-9a2a-4afe242b0f1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/horde_70088ee7-6460-4eaa-9a2a-4afe242b0f1b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-person-team-busts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    human_construction = "bust"
    aliases = ()
    keywords = ('three', 'person', 'team', 'busts')

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

        for j,(x,y,r,end) in enumerate([(8,14,3,36),(24,12,4,40),(40,14,3,36)]):
         circle(f'head-{j}',x,y,r);top=y+r+4
         path(f'body-{j}',(x-4,end),[('L',(x-4,top+4)),('A',(x,top),4,4,True),('A',(x+4,top+4),4,4,True),('L',(x+4,end))]);join(f'head-{j}',f'body-{j}')
