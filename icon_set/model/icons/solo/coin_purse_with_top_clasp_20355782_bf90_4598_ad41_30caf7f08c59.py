# Final repair: Replace cramped clasp loop with a single broad clasp pin.
'Coin Purse with Top Clasp\nPlan: Rounded coin purse body tapers into top frame; centered clasp.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Drop duplicate upper frame, retain clasp and broad pouch.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20355782-bf90-4598-ad41-30caf7f08c59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/purse_20355782-bf90-4598-ad41-30caf7f08c59.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coin-purse-with-top-clasp'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('coin', 'purse', 'with', 'top', 'clasp')

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

        path('bag',(14,16),[(34,16),(44,32),((36,40),8,8,True),(12,40),((4,32),8,8,True),(14,16)],True)
        self.add_line('clasp',(24,8),(24,16));self.relate('connect','clasp','bag')
