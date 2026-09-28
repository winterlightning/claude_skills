'Robotic Hero Head Portrait.\nPlan: Rounded helmet, centered crest and side ears with paired eye marks. Inner face opening omitted for clearance. Bounds6..42.\nReference: Lucide bot: symmetric paired eyes and rounded head; source crest and side ears preserve hero helmet.\nKeyshape: SQUARE, exact SOLO48 envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9ca9fb98-cf39-440b-bf68-a967457588da'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robot-hero-helmet/20260927T171905Z-thuan-mac-1/reference/megaman_9ca9fb98-cf39-440b-bf68-a967457588da.svg'
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

        self.add_arc('helmet-upper-left',(10,22),(18,14),radius_x=8,sweep=True)
        self.add_line('helmet-crown-1',(18,14),(20,14))
        self.add_line('helmet-crown-2',(20,14),(28,14))
        self.add_line('helmet-crown-3',(28,14),(30,14))
        self.add_arc('helmet-upper-right',(30,14),(38,22),radius_x=8,sweep=True)
        self.add_line('helmet-right',(38,22),(38,28))
        self.add_bezier('helmet-jaw-right',(38,28),((38,32),(36,37),(32,38)))
        self.add_bezier('helmet-chin-right',(32,38),((29,41),(27,42),(24,42)))
        self.add_bezier('helmet-chin-left',(24,42),((21,42),(19,41),(16,38)))
        self.add_bezier('helmet-jaw-left',(16,38),((12,37),(10,32),(10,28)))
        self.add_line('helmet-left',(10,28),(10,22))
        self.add_contour('helmet','helmet-upper-left','helmet-crown-1','helmet-crown-2',
                         'helmet-crown-3','helmet-upper-right','helmet-right',
                         'helmet-jaw-right','helmet-chin-right','helmet-chin-left',
                         'helmet-jaw-left','helmet-left',closed=True)
        self.add_polyline('crest',(20,14),(20,6),(28,6),(28,14));self.relate('connect','crest','helmet')
        for a,b in (((6,26),(10,26)),((38,26),(42,26))):
         n='ear-'+str(a[0]);self.add_line(n,a,b);self.relate('connect',n,'helmet')
        self.add_bezier('face-left',(16,38),((18,32),(18,23),(20,24)))
        self.add_bezier('face-left-brow',(20,24),((22,25),(23,27),(24,28)))
        self.add_bezier('face-right-brow',(24,28),((25,27),(26,25),(28,24)))
        self.add_bezier('face-right',(28,24),((30,23),(30,32),(32,38)))
        self.add_contour('face','face-left','face-left-brow','face-right-brow','face-right')
        self.relate('connect','face','helmet')
