"""Robotic Arm Assembly Line.

Plan: Robot elbow, gripper and three conveyor rollers; bounds6,6,42,42. Rollers become three dots; narrow arm becomes one stroke.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7b08f5f-04fe-479e-bafa-80221fd891d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/assembly factory belt_b7b08f5f-04fe-479e-bafa-80221fd891d2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'robot-gripper-above-a-conveyor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('robot', 'gripper', 'above', 'a', 'conveyor')

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

        circle('joint',14,10,4);line('arm',(18,10),(32,10));join('arm','joint')
        poly('grip',(42,6),(36,6),(32,10),(36,14),(42,14));join('grip','arm')
        line('support',(14,14),(10,24));join('support','joint')
        rect('belt',6,24,36,18,4);join('support','belt')
        for x in (15,24,33):self.add_dot('roller-'+str(x),(x,33))
