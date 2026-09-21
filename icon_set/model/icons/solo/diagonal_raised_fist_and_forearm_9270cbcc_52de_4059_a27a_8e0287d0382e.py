"""Raised Clenched Fist.

Plan: Diagonal forearm and clenched hand within6,6,42,42; three knuckle divisions replace four crowded fingers.
Construction reference: Lucide hand rounded fingers and shared palm; source diagonal pose
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9270cbcc-52de-4059-a27a-8e0287d0382e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/artificial arm_9270cbcc-52de-4059-a27a-8e0287d0382e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-raised-fist-and-forearm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'raised', 'fist', 'and', 'forearm')

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

        path('fist',(6,34),[('L',(18,22)),('C',(18,14),(14,18),(15,17)),('L',(24,8)),('C',(28,6),(25,6),(26,6)),('C',(32,8),(30,6),(31,7)),('L',(40,16)),('C',(42,20),(42,17),(42,18)),('C',(40,24),(42,22),(41,23)),('L',(30,34)),('C',(24,34),(28,36),(26,36)),('L',(16,42))])
        poly('fold',(32,8),(28,18),(36,26));join('fold','fist')
