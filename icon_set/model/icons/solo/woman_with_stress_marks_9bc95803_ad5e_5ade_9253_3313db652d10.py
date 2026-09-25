"""Woman Experiencing Stress and Headache.

Plan: centered circular face with bob hair, broad curved shoulders and two stress marks.
Human user.svg informs circular face and shoulders. Circular face bottom33/body top37: zero ink gap.
VRECT_L extremes8,4,40,44. Center stress mark and neckline omitted to retain clear hair and shoulders.
Reference: pictographic-primitives/work/user woman stress_9bc95803-ad5e-5ade-9253-3313db652d10.svg
Authored directly on SOLO48; no source geometry was scaled or traced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bc95803-ad5e-5ade-9253-3313db652d10'
SOURCE_PATH = 'pictographic-primitives/work/user woman stress_9bc95803-ad5e-5ade-9253-3313db652d10.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'woman-with-stress-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('woman', 'with', 'stress', 'marks')

    def build(self):

        def path(name, start, commands, closed=False):
            point, members = start, []
            for index, command in enumerate(commands):
                kind, end, *args = command
                member = f'{name}-{index}'
                if kind == 'L':
                    self.add_line(member, point, end)
                elif kind == 'A':
                    self.add_arc(member, point, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                else:
                    self.add_bezier(member, point, (args[0], args[1], end))
                point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, radius):
            path(name, (x-radius,y), [('A',(x+radius,y),radius,radius,True),
                 ('A',(x-radius,y),radius,radius,True)], True)
        def box(name, l, t, r, b, radius=4):
            path(name,(l+radius,t),[('L',(r-radius,t)),('A',(r,t+radius),radius,radius,True),
                ('L',(r,b-radius)),('A',(r-radius,b),radius,radius,True),('L',(l+radius,b)),
                ('A',(l,b-radius),radius,radius,True),('L',(l,t+radius)),
                ('A',(l+radius,t),radius,radius,True)],True)

        # Centered circular face inside a separate, symmetrical bob outline.
        self.add_arc('head-top',(19,28),(29,28),radius_x=5,sweep=True)
        self.add_arc('head-bottom',(29,28),(19,28),radius_x=5,sweep=True)
        self.add_contour('head','head-top','head-bottom',closed=True)
        path('hair',(10,31),[('L',(10,28)),('A',(38,28),14,14,True),('L',(38,31))])
        self.add_arc('body-top',(8,44),(40,44),radius_x=16,radius_y=7,sweep=True)
        self.add_contour('body','body-top')
        self.relate('connect','head','body')
        self.add_polyline('stress-left',(8,4),(12,7),(8,10))
        self.add_polyline('stress-right',(40,4),(36,7),(40,10))
