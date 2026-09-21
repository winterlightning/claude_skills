"""Ginger Turmeric Root.

Plan: VRECT_L, centerline extremes (8, 4, 40, 44); 48 x 48, stroke 4.
Unequal bulbous branches preserve the rhizome silhouette. Fine skin creases are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: No useful local Lucide match was found..
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33f2476f-ecf5-4ac2-bbd6-dc321214dfa7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/turmeric_33f2476f-ecf5-4ac2-bbd6-dc321214dfa7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'turmeric-root-33f2476f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('turmeric', 'root', '33f2476f')

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

        path('root',(8,36),[('C',(14,24),(8,30),(10,26)),('C',(20,8),(20,20),(18,14)),('C',(28,4),(20,4),(24,4)),('C',(30,20),(32,4),(32,14)),('C',(36,16),(34,20),(32,16)),('C',(40,22),(40,14),(40,18)),('C',(26,30),(40,30),(32,30)),('C',(34,36),(30,30),(34,32)),('C',(24,40),(38,42),(30,44)),('C',(16,44),(22,44),(20,44)),('A',(8,36),8,8,True)],True)
