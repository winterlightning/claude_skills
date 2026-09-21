"""Podcast Audio Signal Waves.

Plan: Concentric broadcast arcs centered at24,24, radii20 and11. Circular head and short capsule torso maintain an exact 8 centerline head/body gap. Fine torso taper omitted.
Construction reference: human_ref/user.svg circular head; Lucide radio concentric arcs
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b3931b1-7ea5-41ce-812e-586577765e74'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apple podcast logo_4b3931b1-7ea5-41ce-812e-586577765e74.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'podcast-figure-with-concentric-waves'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('podcast', 'figure', 'with', 'concentric', 'waves')

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

        path('outer',(8,36),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True)])
        path('inner',(13,24),[('A',(24,13),11,11,True),('A',(35,24),11,11,True)])
        circle('head',24,24,2)
        path('torso',(20,38),[('A',(28,38),4,4,True),('L',(28,40)),('A',(20,40),4,4,True),('L',(20,38))],True)
