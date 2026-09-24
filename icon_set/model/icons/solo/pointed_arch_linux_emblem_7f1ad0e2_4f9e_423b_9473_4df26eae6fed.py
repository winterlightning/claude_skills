'The pointed Arch Linux emblem with a rounded lower notch and interrupted right slope.\nPlan: VRECT_L matches the tall pointed emblem.\nReduction: Made the lower notch shallower and slightly narrower to clear the left slope; retained its opening and the right-side break.\nConstruction: No useful direct Lucide match; supplied Arch emblem governs the silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f1ad0e2-4f9e-423b-9473-4df26eae6fed'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arch linux logo_7f1ad0e2-4f9e-423b-9473-4df26eae6fed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-arch-linux-emblem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('pointed', 'arch', 'linux', 'emblem')

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

        self.add_polyline('left',(8,44),(24,4),(35,31))
        path('base',(8,44),[(20,39),((28,39),4,4,True),(40,44),(38,39)])
        self.relate('connect','left','base')
