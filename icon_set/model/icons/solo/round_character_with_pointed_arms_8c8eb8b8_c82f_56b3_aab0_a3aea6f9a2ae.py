'Happy Round Smiling Character.\nPlan: Rounded character body with integrated triangular arms and feet. Main body uses radius15 arcs; each protrusion replaces a circle section rather than enclosing a tiny pocket. Sparse eyes and mouth; bounds6..42.\nReference: No useful Lucide character match; source circular body with triangular arms and rounded feet.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c8eb8b8-c82f-56b3-aab0-a3aea6f9a2ae'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-05/kirby_8c8eb8b8-c82f-56b3-aab0-a3aea6f9a2ae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-character-with-pointed-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('round', 'character', 'with', 'pointed', 'arms')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('outline',(15,12),[(6,6),(12,15),((12,33),15,15,False),(10,42),(15,36),((33,36),15,15,False),(38,42),(36,33),((36,15),15,15,False),(42,6),(33,12),((15,12),15,15,False)],True)
        for j,x in enumerate((20,28)):self.add_dot(f'eye-{j}',(x,21))
        self.add_line('mouth',(22,30),(26,30))
