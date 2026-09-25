"""Roller Coaster and Ferris Wheel.

Plan: Ferris wheel above curving coaster track, natural amusement scene; bounds6,6,42,42. Four spokes and three supports.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cf656a0-7a4a-4dd2-9361-da20c0c4b28b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/theme park_9cf656a0-7a4a-4dd2-9361-da20c0c4b28b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'roller-coaster-ferris-wheel-reference-9cf656a0'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('roller', 'coaster', 'ferris', 'wheel', 'reference', '9cf656a0')

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

        circle('wheel',32,14,8)
        poly('spoke-v',(32,6),(32,14),(32,22));poly('spoke-h',(24,14),(32,14),(40,14));join('spoke-v','wheel');join('spoke-h','wheel');join('spoke-v','spoke-h')
        path('track',(6,42),[('L',(6,34)),('C',(12,26),(6,26),(8,26)),('C',(32,32),(20,26),(22,32)),('L',(42,32)),('L',(42,42))])
        line('base',(6,42),(42,42));join('base','track')
        line('support',(16,27),(16,42));join('support','track');join('support','base')
        line('stand',(32,22),(32,32));join('stand','wheel');join('stand','track')
