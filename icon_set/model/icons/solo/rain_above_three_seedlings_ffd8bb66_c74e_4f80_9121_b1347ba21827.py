"""Rain Cloud Over Growing Sprouts.

Plan: Rain above three sprouts, bounds6,6,42,42. Five rain marks reduced to three; three paired leaves and ground preserved. Repeated seedlings share common parameters.
Construction reference: Lucide cloud-rain: rounded cloud and detached rain strokes; source seedling scene
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffd8bb66-c74e-4f80-9121-b1347ba21827'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/organic rain growth_ffd8bb66-c74e-4f80-9121-b1347ba21827.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rain-above-three-seedlings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rain', 'above', 'three', 'seedlings')

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

        path('cloud',(14,18),[('A',(14,10),4,4,True),('L',(16,10)),('A',(32,10),8,4,True),('L',(34,10)),('A',(34,18),4,4,True),('L',(14,18))],True)
        for x in (14,24,34):line('rain-'+str(x),(x+1,26),(x-1,27))
        poly('ground',(6,42),(10,42),(24,42),(38,42),(42,42))
        for x in (10,24,38):
         poly('sprout-'+str(x),(x-4,36),(x,42),(x+4,36));join('sprout-'+str(x),'ground')
