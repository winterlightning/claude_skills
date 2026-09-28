"""Gas Station Pump.

Plan: Upright pump, wide display and curved side hose. Bounds6,6,42,42. Omit miniature nozzle trigger.
Construction reference: fuel.
Final review: Widened hose; simplified body and display.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f1e37b5-f219-4e5b-8497-623ac443e33e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/pump_1f1e37b5-f219-4e5b-8497-623ac443e33e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fuel-pump-hanging-hose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('fuel', 'pump', 'hanging', 'hose')

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

        poly('pump',(6,6),(26,6),(26,24),(26,42),(6,42),closed=True)
        line('display-base',(6,20),(26,20));join('display-base','pump')
        path('hose',(26,24),[('L',(30,24)),('A',(34,28),4,4,True),('L',(34,34)),('A',(42,34),4,4,False),('L',(42,16)),('L',(34,8))]);join('hose','pump')
