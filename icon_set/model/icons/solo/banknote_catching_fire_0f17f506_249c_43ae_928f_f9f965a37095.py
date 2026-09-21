'Banknote Catching Fire\nPlan: Diagonal banknote with center ring above overlapping flame at lower left.\nReference: Lucide flame: asymmetric coherent outline.\nReduction: Omit inner flame and note corners; retain burning note and circular seal.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f17f506-249c-43ae-928f-f9f965a37095'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/business burn money_0f17f506-249c-43ae-928f-f9f965a37095.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banknote-catching-fire'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('banknote', 'catching', 'fire')

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

        self.add_polyline('note',(16,17),(29,6),(42,18),(30,30))
        self.add_dot('seal',(29,18))
        self.add_bezier('flame',(17,42),((7,42),(6,35),(6,30)),((6,25),(11,19),(16,17)),((12,26),(15,31),(20,27)),((24,32),(26,42),(17,42)))
        self.add_contour('flame-outline','flame',closed=True)
        self.relate('connect','note','flame-outline')
