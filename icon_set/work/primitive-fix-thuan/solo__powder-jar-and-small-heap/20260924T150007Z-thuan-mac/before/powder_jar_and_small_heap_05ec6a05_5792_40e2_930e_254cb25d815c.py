"""Powder Container and Pile.

Plan: Powder jar behind separate heap, bounds8,4,40,44. Keep intentional occlusion gap and remove only lid overhang detail.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05ec6a05-5792-40e2-930e-254cb25d815c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/powder_05ec6a05-5792-40e2-930e-254cb25d815c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'powder-jar-and-small-heap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('powder', 'jar', 'and', 'small', 'heap')

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

        rect('lid',8,4,24,8,4)
        path('jar',(8,12),[('L',(8,40)),('A',(12,44),4,4,False),('L',(14,44))]);join('jar','lid')
        line('right-wall',(32,12),(32,18));join('right-wall','lid')
        path('heap',(28,44),[('C',(24,40),(24,44),(24,42)),('C',(32,28),(24,36),(29,28)),('C',(40,40),(35,28),(40,36)),('C',(36,44),(40,42),(40,44)),('L',(28,44))],True)
