"""Simple Mosquito Insect Icon.

Plan: Mosquito wings, tapered abdomen, proboscis and upper angular leg pair retained. Merged the small head/thorax and omitted crowded lower legs. Keyshape SQUARE uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3605667b-c5bf-410b-bf1d-b0ebd95706b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mosquito_3605667b-c5bf-410b-bf1d-b0ebd95706b4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'long-legged-mosquito'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('long', 'legged', 'mosquito')

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

        path('body',(24,18),[('C',(29,29),(28,20),(29,25)),('C',(24,42),(29,34),(26,39)),('C',(19,29),(22,39),(19,34)),('C',(24,18),(19,25),(20,20))],True)
        line('proboscis',(24,6),(24,18));join('body','proboscis')
        for s in [-1,1]:
         path(f'wing{s}',(24,18),[('C',(24+s*18,26),(24+s*12,17),(24+s*18,18)),('C',(24+s*12,32),(24+s*18,30),(24+s*16,32)),('C',(24,18),(24+s*8,32),(24+s*4,22))],True);join(f'wing{s}','body');join(f'wing{s}','proboscis')
         poly(f'leg{s}',(24,18),(24+s*12,14),(24+s*14,6));join(f'leg{s}','proboscis');join(f'leg{s}','body');join(f'leg{s}',f'wing{s}')
        join('wing-1','wing1');join('leg-1','leg1')
