'Three Rising Rounded Bars\nPlan: Three increasing outlined bars with shared baseline; repeated width eight and step sixteen.\nReference: Lucide chart-no-axes-column-increasing: regular ascending series.\nReduction: Omit baseline overhang; three outlined bars retained.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fc8cd79-b7c3-4758-ab65-6c1f725a806d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/analytics graph bars stacked_9fc8cd79-b7c3-4758-ab65-6c1f725a806d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-rising-rounded-bars'
    keyshape = Keyshape.HRECT_L
    category = "primitives-generate"
    keywords = ('three', 'rising', 'rounded', 'bars')

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

        for k,(x,t) in enumerate([(4,24),(20,16),(36,8)]):
            path(f'bar-{k}',(x,40),[(x,t+4),((x+4,t),4,4,True),((x+8,t+4),4,4,True),(x+8,40),(x,40)],True)
