'Paw Print with Four Oval Toes\nPlan: Four small circular toes and broad organic pad. Toe pair spacing and pad shape share a vertical axis.\nReference: Lucide paw-print: four round toes above one organic pad.\nReduction: Toes become small circles; retain count and paw-pad silhouette.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e35f2af-227b-4dcc-9883-97fc7e054d59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baidu logo_0e35f2af-227b-4dcc-9883-97fc7e054d59.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paw-print-with-four-oval-toes'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('paw', 'print', 'with', 'four', 'oval', 'toes')

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

        for k,(x,y) in enumerate([(8,22),(17,8),(31,8),(40,22)]):circle(f'toe-{k}',x,y,2)
        self.add_bezier('pad',(24,22),((20,22),(20,28),(17,30)),((14,33),(10,34),(10,38)),((10,42),(14,42),(18,42)),((20,42),(22,40),(24,40)),((26,40),(28,42),(30,42)),((34,42),(38,42),(38,38)),((38,34),(34,33),(31,30)),((28,28),(28,22),(24,22)))
        self.add_contour('paw','pad',closed=True)
