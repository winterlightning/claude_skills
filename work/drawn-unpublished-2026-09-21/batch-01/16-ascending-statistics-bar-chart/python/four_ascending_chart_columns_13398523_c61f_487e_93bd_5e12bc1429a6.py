'Four Ascending Chart Columns\nPlan: Four ascending outlined columns with equal widths and gaps; no filled-bar substitution.\nReference: Lucide chart-no-axes-column-increasing: regular ascending series.\nReduction: Retain the defining silhouette and visible parts.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13398523-c61f-487e-93bd-5e12bc1429a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/daytum logo_13398523-c61f-487e-93bd-5e12bc1429a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-ascending-chart-columns'
    keyshape = Keyshape.HRECT_L
    category = "objects"
    keywords = ('four', 'ascending', 'chart', 'columns')

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

        for k in range(4):
            x=4+11*k;t=29-7*k
            self.add_polyline(f'column-{k}',(x,40),(x,t),(x+7,t),(x+7,40),(x,40))
