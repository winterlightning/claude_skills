'Plumed battle helmet.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8214f96f-5065-5adb-8225-f44c3d1738eb'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/spartan mask_8214f96f-5065-5adb-8225-f44c3d1738eb.svg'
AUTHOR = 'gpt-6'

class PlumedBattleHelmet(Solo48):
    icon_id = 'plumed-battle-helmet'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('helmet', 'plume', 'spartan', 'greek', 'warrior', 'armour', 'battle', 'crest')

    def build(self):
        # Plan: A smooth dome and broad cheek guard define the empty helmet. Widen the crest gap and remove the cramped neck fragments beneath the helmet.

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
        path('helmet',(16,24), [('A',(28,12),12,12,True),('A',(40,24),12,12,True),('L',(40,28)),('L',(36,28)),('L',(40,44)),('L',(30,38)),('L',(26,28)),('L',(24,36)),('L',(16,36)),('L',(16,24))],True)
        path('crest',(28,12), [('L',(34,4)),('L',(24,4)),('A',(8,20),16,16,False),('L',(8,30)),('L',(8,40))]);join('crest','helmet')
