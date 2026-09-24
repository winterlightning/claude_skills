"""An upright hand with a curled thumb.
Plan: VRECT_L leaves room for the long index finger and widened thumb curl.
Reduction: No defining component removed; thumb tip and inner palm rebalanced.
Construction: Human reference guidance inspected; Lucide hand reviewed for round finger caps and continuous palm contour.
Layout: Anatomical asymmetry preserved; no head or torso gap applies."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76411d38-aca5-4268-9511-bc3205689722'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bhudda hand finger citron 1_76411d38-aca5-4268-9511-bc3205689722.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'upright-hand-with-curled-fingers'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('upright', 'hand', 'with', 'curled', 'fingers')

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

        self.add_bezier('thumb-outer',(8,44),((8,33),(8,22),(10,18)))
        self.add_arc('thumb-tip',(10,18),(18,24),radius_x=5)
        self.add_bezier('thumb-inner',(18,24),((17,26),(17,27),(17,29)),((17,34),(28,34),(28,25)),((28,20),(28,14),(28,10)))
        self.add_arc('index-0',(28,10),(40,10),radius_x=6,sweep=True)
        self.add_bezier('palm',(40,10),((40,28),(40,32),(30,39)),((27,41),(25,43),(24,44)))
        self.add_contour('hand','thumb-outer','thumb-tip','thumb-inner','index-0','palm')
