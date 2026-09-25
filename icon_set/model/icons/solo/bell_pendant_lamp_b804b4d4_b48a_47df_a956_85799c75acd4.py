'Hanging Pendant Ceiling Lamp.\nPlan: Bell-shaped pendant shade with rounded neck, flat rim, attached bulb and hanging cord.\nConstruction reference: Lucide lamp-ceiling: connected shade/rim/bulb and central suspension.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b804b4d4-b48a-47df-a956-85799c75acd4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lamp 4_b804b4d4-b48a-47df-a956-85799c75acd4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bell-pendant-lamp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('bell', 'pendant', 'lamp')

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

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('shade',(6,34),[((16,18),20,20,True),(16,16),((24,8),8,8,True),((32,16),8,8,True),(32,18),((42,34),20,20,True),(32,34),(16,34),(6,34)],True)
        self.add_line('cord',(24,6),(24,8));self.relate('connect','cord','shade')
        path('bulb',(32,34),[((16,34),8,8,True)])
        self.relate('connect','bulb','shade')
