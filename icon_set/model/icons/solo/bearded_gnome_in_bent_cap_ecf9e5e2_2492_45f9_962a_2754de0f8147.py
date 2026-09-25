'Bearded Garden Gnome Face.\nSymbol plan: Bent cap above a pointed beard with two round eye marks. Ear bulges, nose and mouth omitted. Shared brim connects hat and beard; extrema(8,4)-(40,44).\nConstruction reference: human_ref/user.svg: circular jaw; source pointed hat and beard preserve gnome identity.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ecf9e5e2-2492-45f9-962a-2754de0f8147'
SOURCE_PATH = 'pictographic-primitives/video-games/batch-04/gnome_ecf9e5e2-2492-45f9-962a-2754de0f8147.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'bearded-gnome-in-bent-cap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('bearded', 'gnome', 'in', 'bent', 'cap')

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

        self.add_polyline('hat',(8,20),(18,4),(32,10),(28,20),closed=True)
        path('beard',(8,20),[(8,30),(24,44),(40,30),(40,20),(28,20)])
        self.add_line('brim',(28,20),(40,20));self.relate('connect','brim','hat');self.relate('connect','brim','beard');self.relate('connect','hat','beard')
        for j,x in enumerate((18,30)):self.add_dot(f'eye-{j}',(x,28))
