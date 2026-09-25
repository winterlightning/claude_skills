"""Simple Bicycle.

Plan: Two equal wheels, open angular frame, saddle and flat handlebar retained. Removed the close inner frame triangle and wheel-hub spokes. Keyshape HRECT_M uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide bike wheels; source angular frame retained, all parts built fresh for SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75853355-5676-4fd9-b3b1-39a87e786c78'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bike fiets velo_75853355-5676-4fd9-b3b1-39a87e786c78.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flat-handlebar-bicycle'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('flat', 'handlebar', 'bicycle')

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

        for x in [12,36]:circle(f'wheel{x}',x,30,8)
        poly('frame',(12,22),(20,10),(28,18),(36,22));join('frame','wheel12');join('frame','wheel36')
        line('saddle',(12,10),(20,10));join('saddle','frame')
        poly('handlebar',(36,22),(36,10),(42,10));join('handlebar','frame');join('handlebar','wheel36')
