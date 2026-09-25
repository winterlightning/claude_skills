"""Pointed Quartz Crystal.

Plan: Crystal at10,4,38,44 with shared facet vertices. Simplify small facet divisions to one central ridge and shoulder seam.
Construction reference: Lucide gem: coherent outer polygon with shared facet endpoints
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6972ce76-101b-4356-b4eb-ea83870f496a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mineral_6972ce76-101b-4356-b4eb-ea83870f496a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-pointed-quartz-crystal'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tall', 'pointed', 'quartz', 'crystal')

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

        poly('outline',(24,4),(38,16),(38,34),(24,44),(10,34),(10,16),closed=True)
        poly('facets',(10,16),(24,22),(38,16));line('ridge-top',(24,4),(24,22));line('ridge-bottom',(24,22),(24,44))
        for a,b in [('outline','facets'),('outline','ridge-top'),('outline','ridge-bottom'),('facets','ridge-top'),('facets','ridge-bottom'),('ridge-top','ridge-bottom')]: join(a,b)
