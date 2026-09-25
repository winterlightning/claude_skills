'Drawn Bow and Arrow\nPlan: Diagonal bow, drawn string and arrow share the crossing node; fletching reduced to two strokes.\nReference: Lucide bow-arrow: open arrowhead and a coherent curved bow.\nReduction: Omit small closed arrowhead and fletching pockets; retain string, bow and shaft.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a05b2dba-7a41-4b74-ae70-8d926dd6d7e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bow arrow_a05b2dba-7a41-4b74-ae70-8d926dd6d7e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'drawn-bow-and-arrow'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    keywords = ('drawn', 'bow', 'and', 'arrow')

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

        self.add_bezier('bow',(6,6),((15,15),(32,6),(34,24)),((34,34),(34,34),(42,42)))
        self.add_polyline('string',(6,6),(6,42),(42,42));self.relate('connect','bow','string')
        self.add_line('arrow',(6,42),(42,6));self.relate('connect','arrow','string');self.relate('connect','arrow','bow')
        self.add_polyline('point',(32,6),(42,6),(42,16));self.relate('connect','arrow','point')
