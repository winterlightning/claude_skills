"""paintbrush: standalone SOLO48 repair.
Plan: Diagonal pointed brush with rounded handle and ferrule.
Keyshape: SQUARE; shared dimensions and nodes own repeated elements.
Reduction: Broadened handle and ferrule openings. A radius-5 cap and 3-4-5 tangent construction make the handle joins smooth.
Lucide originals and atomic-debug construction reference: paintbrush.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6746ee9-8a45-44c8-81ef-7d3da12c0bca'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_29/paintbrush_f6746ee9-8a45-44c8-81ef-7d3da12c0bca.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-artist-paintbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('pointed', 'artist', 'paintbrush')

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

        # Capsule cap: center (37,11), radius 5; side tangents use the 3-4-5 triangle.
        # The 8x6 base vector and 6x-8 ferrule vector both have length 10.
        self.add_line('handle-side-a',(21,24),(33,8))
        self.add_arc('handle-cap',(33,8),(41,14),radius_x=5)
        self.add_line('handle-side-b',(41,14),(29,30))
        self.add_line('handle-base',(29,30),(21,24))
        self.add_contour('handle-outline','handle-side-a','handle-cap','handle-side-b','handle-base',closed=True)
        self.add_polyline('ferrule',(21,24),(15,32),(23,38),(29,30))
        self.relate('connect','ferrule','handle-outline')
        self.add_bezier('bristles',(15,32),((6,30),(12,38),(6,42)),((15,42),(23,42),(23,38)))
        self.relate('connect','bristles','ferrule')
