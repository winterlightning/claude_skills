'Bathrobe with tied belt.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/bathrobe_with_tied_belt.py'
AUTHOR = 'gpt-6'

class BathrobeWithTiedBelt(Solo48):
    icon_id = 'bathrobe-with-tied-belt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ('bathrobe', 'robe', 'dressing-gown')
    keywords = ('bathrobe', 'robe', 'spa', 'bath', 'hotel', 'garment', 'clothing', 'belt')

    def build(self):
        # Plan: Lucide shirt: balanced shoulders and sleeves, broad wrap panels and tangent rounded hem; belt and tie share one waist node.

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
        path('robe',(13,40), [('L',(13,30)),('L',(13,22)),('L',(12,19)),('L',(8,10)),('L',(18,4)),('L',(30,4)),('L',(40,10)),('L',(36,19)),('L',(35,22)),('L',(35,30)),('L',(35,40)),('A',(31,44),4,4,True),('L',(17,44)),('A',(13,40),4,4,True)],True)
        poly('wrap',(18,4),(24,30),(30,4));join('wrap','robe')
        poly('belt',(13,30),(24,30),(35,30));join('belt','robe');join('belt','wrap')
        line('tie',(24,30),(24,36));join('tie','belt');join('tie','wrap')
