'Parent and Child.\nPlan: Adult at left and smaller child at right. Circular heads; detached shoulder extrema exactly8 below head outlines. Partial adult shoulder avoids overlap. Bounds6..42.\nReference: human_ref/user.svg: circular heads, broad curved shoulders; group arrangement follows source. Head/body ink gap4 for both people.\nKeyshape: SQUARE; constructed to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab07d9fa-5a90-40d1-929f-c687e4e325fb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_21/godmother_ab07d9fa-5a90-40d1-929f-c687e4e325fb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'adult-beside-child-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('adult', 'beside', 'child', 'bust')

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

        circle('adult-head',15,12,6)
        path('adult-shoulder',(6,42),[(6,35),((15,26),9,9,True),(18,26)])
        circle('child-head',34,25,4)
        path('child-shoulder',(26,42),[((34,37),8,5,True),((42,42),8,5,True)])
