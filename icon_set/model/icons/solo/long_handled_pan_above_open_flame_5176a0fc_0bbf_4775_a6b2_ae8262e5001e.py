"""Frying Pan over Fire.

Plan: Shallow pan above a physical cooking flame; one cooking scene. Bounds4,8,44,40.
Construction reference: No useful local Lucide match.
Final review: Native light/dark review: recognizable reduced silhouette, balanced spacing and coherent joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5176a0fc-0bbf-4775-a6b2-ae8262e5001e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stove pan_5176a0fc-0bbf-4775-a6b2-ae8262e5001e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-handled-pan-above-open-flame'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('long', 'handled', 'pan', 'above', 'open', 'flame')

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

        poly('pan',(18,8),(44,8),(40,20),(22,20),closed=True);line('handle',(4,8),(18,8));join('pan','handle')
        path('flame',(22,40),[('C',(24,29),(20,36),(22,32)),('L',(28,33)),('L',(34,28)),('C',(38,40),(38,32),(40,38)),('L',(22,40))],True)
