"""Shoe Storage Rack Organizer.

Plan: Retained the open rack, upper and lower compartments and the right-facing shoe on its middle shelf. Simplified the shoe upper and shared the sole with the shelf.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28268293-e5fb-4119-b758-b0cd92d8e4dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shoe rack_28268293-e5fb-4119-b758-b0cd92d8e4dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shoe-resting-on-open-rack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('shoe', 'resting', 'on', 'open', 'rack')

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

        poly('rack',(8,44),(8,4),(40,4),(40,44))
        for y in (12,32,40):line('shelf-'+str(y),(8,y),(40,y));join('shelf-'+str(y),'rack')
        path('shoe',(16,32),[('L',(16,21)),('C',(24,22),(19,24),(22,24)),('C',(32,24),(27,24),(32,20)),('L',(32,32))]);join('shoe','shelf-32')
