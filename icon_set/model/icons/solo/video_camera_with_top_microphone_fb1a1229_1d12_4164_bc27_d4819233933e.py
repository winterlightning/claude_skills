"""Professional Video Camera.

Plan: Professional camera bounds4,8,44,40. Body, flared lens and top microphone remain. Side circles reduced to two dots; handle reduced to a support.
Construction reference: Lucide video: rectangular body and flared lens attachment
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb1a1229-1d12-4164-bc27-d4819233933e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camera professional_fb1a1229-1d12-4164-bc27-d4819233933e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'video-camera-with-top-microphone'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('video', 'camera', 'with', 'top', 'microphone')

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

        path('body',(8,20),[('L',(16,20)),('L',(26,20)),('A',(30,24),4,4,True),('L',(30,28)),('L',(30,36)),('A',(26,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,24)),('A',(8,20),4,4,True)],True)
        poly('lens',(30,28),(44,20),(44,40),(30,36));join('lens','body')
        line('support',(16,20),(16,12));poly('microphone',(8,12),(8,8),(32,8));join('support','body');join('support','microphone')
        for x in (13,21):self.add_dot('control-'+str(x),(x,30))
