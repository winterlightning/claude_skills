"""Rounded Video Camera.

Plan: Rounded body with flared hood; shared junctions at body right. Bounds4,10,44,38.
Construction reference: video.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41f90a9c-b243-4a88-8a3f-f48976903507'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/video_41f90a9c-b243-4a88-8a3f-f48976903507.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'video-camera-solo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('video', 'camera', 'solo')

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

        path('body',(8,10),[('L',(26,10)),('A',(30,14),4,4,True),('L',(30,18)),('L',(30,30)),('L',(30,34)),('A',(26,38),4,4,True),('L',(8,38)),('A',(4,34),4,4,True),('L',(4,14)),('A',(8,10),4,4,True)],True)
        poly('hood',(30,18),(44,10),(44,38),(30,30));join('body','hood')
