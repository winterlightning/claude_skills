"""A glue gun with nozzle, trigger, rear glue stick and a short curved glue trail; surface details omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8'
SOURCE_PATH = 'pictographic-primitives/tools/tools glue gun_419e370a-9fd2-4fcf-a6d2-cbe5f602e3f8.svg'
AUTHOR = 'gpt-6'

class HotGlueGun(Solo48):
    icon_id = 'hot-glue-gun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ()
    keywords = ('glue gun', 'hot glue', 'glue', 'adhesive', 'craft', 'diy', 'nozzle', 'tool')

    def build(self):
        # Plan: Broaden the nozzle and grip around a continuous outline, keeping the diagonal glue-gun profile and a smooth glue bead underneath.

        # Each path owns a coherent stroke; control points preserve smooth tangents.
        def path(n, start, commands, closed=False):
            here = start
            members = []
            for j, c in enumerate(commands):
                k, end, *args = c
                name = f'{n}-{j}'
                if k == 'L': self.add_line(name, here, end)
                elif k == 'A': self.add_arc(name, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif k == 'C': self.add_bezier(name, here, (args[0], args[1], end))
                here = end
                members.append(name)
            self.add_contour(n, *members, closed=closed)
        def circle(n, x, y, r):
            path(n, (x-r,y), [('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True)], True)
        def box(n, l, t, r, b, rad=4):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line = self.add_line
        poly = self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('body',(6,30),(10,18),(24,6),(34,10),(30,18),(42,26))
        poly('underside',(6,30),(16,30),(24,22),(30,34),(34,24));join('body','underside')
        line('glue-stick',(29,8),(34,6));join('glue-stick','body')
        path('glue',(6,40), [('A',(14,40),4,2,False),('A',(22,40),4,2,True)])
