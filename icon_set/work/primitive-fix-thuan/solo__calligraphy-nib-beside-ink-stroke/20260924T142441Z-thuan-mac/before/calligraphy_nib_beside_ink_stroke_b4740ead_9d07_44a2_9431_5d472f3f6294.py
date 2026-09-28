'Calligraphy Nib Beside Ink Stroke\nPlan: Diagonal nib with slit and separate curled ink stroke.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Preserve diagonal nib and lower curl; omit tiny nib hole.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4740ead-9d07-44a2-9431-5d472f3f6294'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crafts calligraphy_b4740ead-9d07-44a2-9431-5d472f3f6294.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'calligraphy-nib-beside-ink-stroke'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('calligraphy', 'nib', 'beside', 'ink', 'stroke')

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

        self.add_polyline('nib',(24,24),(29,6),(36,6),(42,12),(42,19),(24,24))
        self.add_line('slit',(24,24),(33,15));self.relate('connect','slit','nib')
        path('ink',(15,20),[((6,29),9,9,False),(6,34),((22,34),8,8,False)])
