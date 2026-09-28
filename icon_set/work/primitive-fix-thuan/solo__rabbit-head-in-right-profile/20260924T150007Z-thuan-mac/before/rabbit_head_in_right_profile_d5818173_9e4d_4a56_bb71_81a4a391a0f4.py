"""Rabbit Head Profile.

Plan: Rabbit profile bounds8,4,40,44. Two upright ears, rounded muzzle and open shoulder line. Remove tiny mouth detail.
Construction reference: Lucide rabbit: long ears, projecting muzzle, coherent animal silhouette
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5818173-9e4d-4a56-bb71-81a4a391a0f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/angora_d5818173-9e4d-4a56-bb71-81a4a391a0f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rabbit-head-in-right-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rabbit', 'head', 'in', 'right', 'profile')

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

        path('rabbit',(8,44),[('C',(14,28),(8,37),(14,36)),('L',(14,22)),('C',(10,4),(8,15),(10,7)),('C',(22,20),(19,4),(21,13)),('L',(22,4)),('C',(30,20),(30,4),(30,12)),('C',(36,28),(33,21),(34,24)),('C',(40,32),(37,29),(40,29)),('C',(30,36),(40,36),(35,38)),('C',(36,44),(30,40),(36,40))])
