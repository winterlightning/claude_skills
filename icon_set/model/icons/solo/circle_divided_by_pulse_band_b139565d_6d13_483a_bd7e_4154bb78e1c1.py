"""Signal Pulse in Circle.

Plan: Reduced the very narrow double pulse band to one continuous pulse crossing a circular outline; preserved the central peak and dip. Keyshape CIRCLE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b139565d-6d13-483a-bd7e-4154bb78e1c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/broadcom logo_b139565d-6d13-483a-bd7e-4154bb78e1c1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circle-divided-by-pulse-band'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('circle', 'divided', 'by', 'pulse', 'band')

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

        path('ring',(4,24),[('A',(24,4),20,20,True),('A',(44,24),20,20,True)])
        path('lower',(44,24),[('A',(24,44),20,20,True),('A',(4,24),20,20,True)])
        poly('pulse',(4,24),(15,24),(20,31),(25,15),(31,24),(44,24));join('pulse','ring');join('pulse','lower');join('ring','lower')
