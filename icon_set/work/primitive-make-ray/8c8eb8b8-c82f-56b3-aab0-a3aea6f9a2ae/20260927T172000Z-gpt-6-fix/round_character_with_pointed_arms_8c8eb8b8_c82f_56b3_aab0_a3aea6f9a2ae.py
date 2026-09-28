'Happy Round Smiling Character.\nPlan: Rounded character body with integrated triangular arms and feet. Main body uses radius15 arcs; each protrusion replaces a circle section rather than enclosing a tiny pocket. Sparse eyes and mouth; bounds6..42.\nReference: No useful Lucide character match; source circular body with triangular arms and rounded feet.\nKeyshape fitted to exact SOLO48 envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c8eb8b8-c82f-56b3-aab0-a3aea6f9a2ae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-character-with-pointed-arms/20260927T171905Z-thuan-mac-1/reference/kirby_8c8eb8b8-c82f-56b3-aab0-a3aea6f9a2ae.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'round-character-with-pointed-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('round', 'character', 'with', 'pointed', 'arms')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 4 and step[0] == 'C':
                    _, end, c1, c2 = step
                    self.add_bezier(member, point, (c1,c2,end))
                    point = end
                elif len(step) == 2:
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

        path('outline',(15,12),[(6,6),(12,15),((12,33),15,15,False),
             ('C',(10,42),(6,37),(6,42)),
             ('C',(19,38),(13,42),(16,40)),
             ((29,38),15,15,False),
             ('C',(38,42),(32,40),(35,42)),
             ('C',(36,33),(42,42),(42,37)),
             ((36,15),15,15,False),(42,6),(33,12),
             ((15,12),15,15,False)],True)
        for j,x in enumerate((20,28)):
            self.add_line(f'eye-{j}',(x,19),(x,21))
        self.add_arc('mouth',(21,29),(27,29),radius_x=3,radius_y=1,sweep=False)
