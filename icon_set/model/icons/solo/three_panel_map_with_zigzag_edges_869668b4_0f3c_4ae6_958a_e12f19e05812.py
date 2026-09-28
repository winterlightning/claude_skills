"""Folded Paper Map.

Plan: Three repeated upright panels joined at crease endpoints. Bounds6,6,42,42. Shared12u panel width; no map markings.
Construction reference: map.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '869668b4-0f3c-4ae6-958a-e12f19e05812'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/map_869668b4-0f3c-4ae6-958a-e12f19e05812.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-panel-map-with-zigzag-edges'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('three', 'panel', 'map', 'with', 'zigzag', 'edges')

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

        poly('map',(6,12),(18,6),(30,12),(42,6),(42,36),(30,42),(18,36),(6,42),closed=True)
        line('left-fold',(18,6),(18,36));line('right-fold',(30,12),(30,42));join('map','left-fold');join('map','right-fold')
