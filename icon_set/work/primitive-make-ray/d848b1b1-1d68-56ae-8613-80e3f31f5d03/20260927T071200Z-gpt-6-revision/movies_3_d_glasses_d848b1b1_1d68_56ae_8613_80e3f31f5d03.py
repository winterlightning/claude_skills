'3D glasses: equal rounded lenses, an 8-unit bridge and matching angled arms.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd848b1b1-1d68-56ae-8613-80e3f31f5d03'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__movies-3-d-glasses/20260927T070927Z-thuan-mac-1/reference/movies 3 d glasses_d848b1b1-1d68-56ae-8613-80e3f31f5d03.svg'
AUTHOR = "gpt-6"

class Movies3DGlasses(Solo48):
    icon_id = 'movies-3-d-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    categories = ('primitives', 'movies')
    aliases = ()
    keywords = ('movies', 'd', 'glasses')

    def build(self):
        # 3D glasses: equal rounded lenses, an 8-unit bridge and matching angled arms.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('left-lens',4,22,20,40,5)
        r('right-lens',28,22,44,40,5)
        l('bridge',(20,28),(28,28))
        link('connect','bridge','left-lens')
        link('connect','bridge','right-lens')
        self.add_bezier('left-arm',(4,24),((4,18),(10,8),(16,8)))
        self.add_bezier('right-arm',(44,24),((44,18),(38,8),(32,8)))
        link('connect','left-arm','left-lens')
        link('connect','right-arm','right-lens')
