"""Segmented Crawling Caterpillar.

Plan: Retained the raised caterpillar head, segmented body and two antennae. Merged overlapping circles into a coherent outline with two internal divisions.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aef18a77-2470-45cf-abf5-2253679f1d58'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/silkworm_aef18a77-2470-45cf-abf5-2253679f1d58.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'segmented-caterpillar-with-raised-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('segmented', 'caterpillar', 'with', 'raised', 'head')

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

        path('caterpillar',(4,32),[('A',(12,24),8,8,True),('L',(20,24)),('C',(28,20),(24,24),(28,24)),('A',(36,12),8,8,True),('A',(44,20),8,8,True),('C',(32,40),(44,32),(40,40)),('L',(12,40)),('A',(4,32),8,8,True)],True)
        line('a',(16,24),(16,40));line('b',(28,20),(28,40));join('a','caterpillar');join('b','caterpillar')
        line('ant-left',(36,12),(28,8));line('ant-right',(36,12),(44,8));join('ant-left','caterpillar');join('ant-right','caterpillar');join('ant-left','ant-right')
