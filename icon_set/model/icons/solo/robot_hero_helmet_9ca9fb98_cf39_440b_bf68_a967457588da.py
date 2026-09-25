'Robotic Hero Head Portrait.\nPlan: Rounded helmet, centered crest and side ears with paired eye marks. Inner face opening omitted for clearance. Bounds6..42.\nReference: Lucide bot: symmetric paired eyes and rounded head; source crest and side ears preserve hero helmet.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ca9fb98-cf39-440b-bf68-a967457588da'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-07/megaman_9ca9fb98-cf39-440b-bf68-a967457588da.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'robot-hero-helmet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('robot', 'hero', 'helmet')

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

        path('helmet',(10,22),[((18,14),8,8,True),(20,14),(28,14),(30,14),((38,22),8,8,True),(38,26),(38,28),((10,28),14,14,True),(10,26),(10,22)],True)
        self.add_polyline('crest',(20,14),(20,6),(28,6),(28,14));self.relate('connect','crest','helmet')
        for a,b in (((6,26),(10,26)),((38,26),(42,26))):
         n='ear-'+str(a[0]);self.add_line(n,a,b);self.relate('connect',n,'helmet')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,28))
