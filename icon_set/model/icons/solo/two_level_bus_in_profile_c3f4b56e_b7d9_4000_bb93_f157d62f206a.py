'A double-decker bus in profile has two window tiers and two wheels. HRECT_L provides the wide vehicle envelope. Body owns tier lines and shared window divider; wheels share radius and y37 axis. Source supplies two storeys; Lucide bus supplies integrated wheel contacts and sparse glazing. Reduce repeated window mullions to one per tier.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3f4b56e-b7d9-4000-bb93-f157d62f206a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/bus double 1_c3f4b56e-b7d9-4000-bb93-f157d62f206a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'two-level-bus-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Double Decker Bus',)
    keywords = ('double', 'decker', 'bus')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('body',(13,37),[(4,37),(4,26),(4,18),(4,12),((8,8),4,4,True),(24,8),(40,8),((44,12),4,4,True),(44,18),(44,26),(44,37),(35,37)])
        self.add_line('underbody',(19,37),(29,37))
        for x in (16,32):
            circle(f'wheel-{x}',x,37,3)
            self.relate('connect',f'wheel-{x}','body');self.relate('connect',f'wheel-{x}','underbody')
        for y in (18,26):
            self.add_polyline(f'tier-{y}',(4,y),(24,y),(44,y));self.relate('connect',f'tier-{y}','body')
        self.add_line('upper-divider',(24,8),(24,18));self.relate('connect','upper-divider','body');self.relate('connect','upper-divider','tier-18')
        self.add_line('lower-divider',(24,18),(24,26));self.relate('connect','lower-divider','tier-18');self.relate('connect','lower-divider','tier-26');self.relate('connect','lower-divider','upper-divider')
