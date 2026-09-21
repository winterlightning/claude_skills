"""Flowering Pansy Plant.

Plan: Rounded flower lobes above stem and pointed leaves, bounds8,4,40,44. Omit tiny disk to preserve open blossom.
Construction reference: flower-2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '099a11a2-aae6-4663-9d14-d5bf3690eb1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pansy_099a11a2-aae6-4663-9d14-d5bf3690eb1e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pansy-paired-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('pansy', 'paired', 'leaves')

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

        path('bloom',(24,8),[('C',(32,4),(26,4),(28,4)),('C',(36,12),(36,4),(38,8)),('C',(40,20),(40,12),(40,16)),('C',(30,24),(40,25),(34,26)),('C',(24,28),(29,28),(26,28)),('C',(18,24),(22,28),(19,28)),('C',(8,20),(14,26),(8,25)),('C',(12,12),(8,16),(8,12)),('C',(16,4),(10,8),(12,4)),('C',(24,8),(20,4),(22,4))],True)
        line('stem',(24,28),(24,44));join('stem','bloom')
        path('leaf-left',(24,44),[('C',(8,35),(12,44),(8,40)),('C',(24,44),(16,35),(22,38))],True);join('leaf-left','stem')
        path('leaf-right',(24,44),[('C',(40,35),(26,38),(32,35)),('C',(24,44),(40,40),(36,44))],True);join('leaf-right','stem');join('leaf-right','leaf-left')
