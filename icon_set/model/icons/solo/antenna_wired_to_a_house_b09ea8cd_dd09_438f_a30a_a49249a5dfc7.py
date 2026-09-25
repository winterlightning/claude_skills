'Antenna Wired to a House\nPlan: Antenna and house linked by an actual base cable; signal arc above tower.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: One radio arc; omit tower braces and house wall top segments to open spacing.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b09ea8cd-dd09-438f-a30a-a49249a5dfc7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antenna house connect_b09ea8cd-dd09-438f-a30a-a49249a5dfc7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'antenna-wired-to-a-house'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('antenna', 'wired', 'to', 'a', 'house')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_polyline('tower',(6,30),(14,15),(22,30),(14,30),(6,30))
        self.add_arc('signal',(6,10),(22,10),radius_x=8,radius_y=4)
        # Antenna peak moved down one grid unit for certified curved separation.
        self.add_polyline('roof',(30,24),(36,18),(42,24))
        self.add_polyline('house',(30,32),(30,34),(42,34),(42,32))
        path('wire',(14,30),[(14,38),((18,42),4,4,False),(32,42),((36,38),4,4,False),(36,34)])
        self.relate('connect','wire','tower');self.relate('connect','wire','house')
