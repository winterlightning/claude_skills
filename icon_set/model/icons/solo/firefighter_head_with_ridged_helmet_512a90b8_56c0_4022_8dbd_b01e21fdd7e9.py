"""Firefighter Avatar with Safety Helmet.

Plan: Circular head with central helmet ridge and wide brim, bounds6,6,42,42. Isolated head uses solo, not bust.
Construction reference: hard-hat.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '512a90b8-56c0-4022-8dbd-b01e21fdd7e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar fire fighter man_512a90b8-56c0-4022-8dbd-b01e21fdd7e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'firefighter-head-with-ridged-helmet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('firefighter', 'head', 'with', 'ridged', 'helmet')

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

        path('head',(8,24),[('L',(8,26)),('A',(24,42),16,16,False),('A',(40,26),16,16,False),('L',(40,24))])
        poly('brim',(6,24),(8,24),(20,24),(28,24),(40,24),(42,24));join('head','brim')
        path('helmet',(8,24),[('A',(20,8),16,16,True),('L',(20,6)),('L',(28,6)),('L',(28,8)),('A',(40,24),16,16,True)]);join('helmet','brim');join('helmet','head')
        line('ridge-left',(20,8),(20,24));line('ridge-right',(28,8),(28,24))
        for n in ('ridge-left','ridge-right'):join(n,'helmet');join(n,'brim')
