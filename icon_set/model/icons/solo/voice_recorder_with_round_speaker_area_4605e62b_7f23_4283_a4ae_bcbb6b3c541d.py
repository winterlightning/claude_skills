"""Portable Voice Recorder.

Plan: Upright recorder bounds10,4,38,44, circle speaker with two control bars. Shared x24 axis.
Construction reference: Lucide briefcase: continuous quarter-circle corner construction
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4605e62b-7f23-4283-a4ae-bcbb6b3c541d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dictaphone_4605e62b-7f23-4283-a4ae-bcbb6b3c541d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'voice-recorder-with-round-speaker-area'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('voice', 'recorder', 'with', 'round', 'speaker', 'area')

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

        rect('body',10,4,28,40,4)
        circle('speaker',24,16,3)
        line('control',(20,32),(28,32))
