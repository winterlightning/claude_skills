'Battlement Wall Behind Water Moat\nPlan: Three broad crenellations over a moat basin; one wave carries water identity.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Remove a second wave and extra enclosure; preserve battlements and water.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '733ca1ef-c038-4751-abd2-87ebc697810d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/moat_733ca1ef-c038-4751-abd2-87ebc697810d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'battlement-wall-behind-water-moat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('battlement', 'wall', 'behind', 'water', 'moat')

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

        path('wall',(6,22),[(6,6),(14,6),(14,14),(34,14),(34,6),(42,6),(42,22)])
        path('water',(6,22),[(42,22),(42,38),((38,42),4,4,True),(10,42),((6,38),4,4,True),(6,22)],True)
        self.relate('connect','wall','water')
        path('wave',(15,32),[((24,32),5,1,False),((33,32),5,1,True)])
