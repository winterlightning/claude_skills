"""Handheld Paint Spray Gun.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The spray gun keeps a broad grip and hanging paint reservoir; a short mark indicates its spray direction.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7b717ca-423a-41ee-ad70-88e50f6aa4d6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paint sprayer_c7b717ca-423a-41ee-ad70-88e50f6aa4d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paint-spray-gun-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('paint', 'spray', 'gun', 'bottle')

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

        rect('housing',6,6,22,12,3)
        poly('grip',(10,18),(6,34),(15,34),(19,18));join('grip','housing')
        poly('feed',(28,15),(32,19),(32,26));join('feed','housing')
        rect('reservoir',26,26,16,16,4);join('feed','reservoir')
        line('spray',(38,12),(42,12))
