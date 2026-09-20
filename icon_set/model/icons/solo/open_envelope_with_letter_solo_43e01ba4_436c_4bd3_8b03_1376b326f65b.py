'Open Envelope with Letter.\nPlan: Letter above open envelope, with hidden envelope top removed behind the paper. Bounds6..42.\nConstruction reference: Lucide mail-open original/atomic-debug: visible folds and coherent open envelope.\nReduction: Remove hidden back-flap edges behind the letter.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43e01ba4-436c-4bd3-8b03-1376b326f65b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mail card_43e01ba4-436c-4bd3-8b03-1376b326f65b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-envelope-with-letter-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('open', 'envelope', 'with', 'letter', 'solo')

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

        path('envelope',(6,22),[(6,38),((10,42),4,4,False),(38,42),((42,38),4,4,False),(42,22)])
        self.add_polyline('letter',(14,28),(14,6),(34,6),(34,28))
        self.add_polyline('fold',(6,22),(18,32),(30,32),(42,22));self.relate('connect','fold','envelope');self.relate('connect','fold','letter')
