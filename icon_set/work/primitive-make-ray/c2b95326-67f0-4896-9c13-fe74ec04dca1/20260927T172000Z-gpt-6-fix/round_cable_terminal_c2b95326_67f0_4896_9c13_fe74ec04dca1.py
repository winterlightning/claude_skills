'Round Cable Terminal\nPlan: Circular terminal with open cable sides attached on lower circle points.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Retain circle and twin cable strokes; exact attachment requires validation.\nKeyshape: VRECT_M; exact SOLO48 contract envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c2b95326-67f0-4896-9c13-fe74ec04dca1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-cable-terminal/20260927T171905Z-thuan-mac-1/reference/cable split 1_c2b95326-67f0-4896-9c13-fe74ec04dca1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-cable-terminal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('round', 'cable', 'terminal')

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

        self.add_arc('terminal-main',(20,12),(28,12),radius_x=5,large_arc=True,sweep=True)
        self.add_arc('terminal-bottom',(28,12),(20,12),radius_x=5)
        self.add_contour('terminal','terminal-main','terminal-bottom',closed=True)
        for x in (20,28):
            self.add_line(f'cable-{x}',(x,12),(x,43));self.relate('connect',f'cable-{x}','terminal')
