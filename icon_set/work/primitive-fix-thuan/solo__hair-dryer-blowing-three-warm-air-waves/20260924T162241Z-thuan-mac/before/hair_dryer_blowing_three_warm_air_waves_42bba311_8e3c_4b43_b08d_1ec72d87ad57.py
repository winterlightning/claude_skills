"""Handheld Hair Dryer with Heat.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The dryer body and side handle remain clear beside three short warm-air marks. The rear vent and long wave shapes are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42bba311-8e3c-4b43-b08d-1ec72d87ad57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dryer_42bba311-8e3c-4b43-b08d-1ec72d87ad57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hair-dryer-blowing-three-warm-air-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hair', 'dryer', 'blowing', 'three', 'warm', 'air', 'waves')

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

        path('dryer',(16,6),[('L',(30,6)),('L',(30,24)),('L',(20,24)),('L',(24,42)),('L',(12,42)),('L',(10,24)),('C',(6,16),(6,24),(6,20)),('A',(16,6),10,10,True)],True)
        for j,y in enumerate([8,18,28]):path(f'air-{j}',(40,y),[('C',(42,y+2),(40,y+3),(42,y-1))])
