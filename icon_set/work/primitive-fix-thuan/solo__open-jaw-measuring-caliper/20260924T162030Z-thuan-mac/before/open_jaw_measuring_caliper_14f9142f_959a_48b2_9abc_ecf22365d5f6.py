"""Precision Vernier Caliper.

Plan: Caliper upright beam and two left-facing jaws. Bounds8,4,40,44. Remove fine sliding rule detail; shared upper and lower jaw attachments.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14f9142f-959a-48b2-9abc-ecf22365d5f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/caliper_14f9142f-959a-48b2-9abc-ecf22365d5f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-jaw-measuring-caliper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'jaw', 'measuring', 'caliper')

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

        poly('beam',(28,4),(28,12),(40,12),(40,20),(28,20),(28,44))
        poly('upper-jaw',(28,4),(8,4),(8,16),(16,16),(16,12),(28,12));join('upper-jaw','beam')
        path('lower-jaw',(28,28),[('L',(16,28)),('L',(16,24)),('L',(8,24)),('L',(8,32)),('C',(28,38),(8,38),(22,38))]);join('lower-jaw','beam')
