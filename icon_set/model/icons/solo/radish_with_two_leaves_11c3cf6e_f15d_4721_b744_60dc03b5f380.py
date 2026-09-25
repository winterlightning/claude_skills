"""Radish Vegetable with Leaves.

Plan: Radish bounds8,4,40,44 with two symmetric leaves and pointed root. Shared leaf/stem junction at24,18.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11c3cf6e-f15d-4721-b744-60dc03b5f380'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/radish_11c3cf6e-f15d-4721-b744-60dc03b5f380.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radish-with-two-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('radish', 'with', 'two', 'leaves')

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

        path('root',(24,27),[('C',(38,30),(34,27),(38,27)),('C',(24,44),(38,38),(28,36)),('C',(10,30),(20,36),(10,38)),('C',(24,27),(10,27),(14,27))],True)
        for side in (-1,1):
         path('leaf-'+str(side),(24,18),[('C',(24+side*16,4),(24,8),(24+side*10,4)),('C',(24,18),(24+side*16,14),(24+side*8,18))],True)
        line('stem',(24,18),(24,27));join('stem','root')
        for side in (-1,1):join('stem','leaf-'+str(side))
        join('leaf--1','leaf-1')
