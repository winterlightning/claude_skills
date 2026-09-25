"""Four Hole Sewing Button.

Plan: Circular button and crossed thread with four open holes. Radius20; omit inner rim to give holes room.
Construction reference: No useful local Lucide match.
Final review: Omitted crossing thread to avoid undersized holes; retained four hole layout.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be4a9d67-241a-40d1-ad6f-ac28c0de01a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/button_be4a9d67-241a-40d1-ad6f-ac28c0de01a1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-hole-cross-stitched-button'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('four', 'hole', 'cross', 'stitched', 'button')

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

        circle('button',24,24,20)
        for j,(x,y) in enumerate([(17,17),(31,17),(17,31),(31,31)]):circle(f'hole-{j}',x,y,2)
