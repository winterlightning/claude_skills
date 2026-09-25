"""Railway Station Bell.

Plan: Station bell on post, bounds8,4,40,44. Round finial and dome, horizontal arm and lower clapper retained.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0acbda39-4f44-4699-bc9d-a0a3e95630be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bell train station_0acbda39-4f44-4699-bc9d-a0a3e95630be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'post-mounted-railway-bell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('post', 'mounted', 'railway', 'bell')

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

        circle('finial',12,8,4);poly('post',(12,12),(12,21),(12,44));join('post','finial')
        poly('arm',(8,21),(12,21),(32,21),(40,21));join('arm','post')
        path('bell',(24,42),[('L',(24,38)),('A',(40,38),8,8,True),('L',(40,42)),('L',(24,42))],True)
        line('hanger',(32,21),(32,30));join('hanger','arm');join('hanger','bell')
        line('clapper',(32,42),(32,44));join('clapper','bell')
