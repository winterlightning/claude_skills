"""Pond with Cattail Plant.

Plan: Cattail above oval pond, bounds8,4,40,44. One water ripple replaces two; two leaves share the stalk junction.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28cbf705-e201-4181-b017-6c0198a22483'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pond_28cbf705-e201-4181-b017-6c0198a22483.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pond-with-cattail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pond', 'with', 'cattail')

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

        path('pond',(8,35),[('A',(40,35),16,9,True),('A',(8,35),16,9,True)],True)
        path('seed',(20,8),[('A',(28,8),4,4,True),('L',(28,12)),('A',(20,12),4,4,True),('L',(20,8))],True)
        line('stem',(24,16),(24,26));join('seed','stem');join('stem','pond')
        poly('leaves',(14,20),(24,26),(34,20));join('leaves','stem');join('leaves','pond')
        line('water',(20,35),(28,35))
