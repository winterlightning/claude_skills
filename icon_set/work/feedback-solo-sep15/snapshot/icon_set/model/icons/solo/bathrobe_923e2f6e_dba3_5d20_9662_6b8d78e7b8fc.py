"""Front-facing belted wrap robe. Square extremes 6,6–42,42. Mirrored sleeves; directional lapel. Lucide shirt informs garment outline; omit duplicate belt tails and front hem seam."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '923e2f6e-dba3-5d20-9662-6b8d78e7b8fc'
SOURCE_PATH = 'pictographic-primitives/spas/bathroom robe_923e2f6e-dba3-5d20-9662-6b8d78e7b8fc.svg'
AUTHOR = 'gpt-6'

class Bathrobe(Solo48):
    icon_id = 'bathrobe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wellness"
    aliases = ()
    keywords = ('spa', 'wellness', 'bathrobe')

    def build(self):
        # Plan: Lucide shirt principles: open sleeve ends, a broad V collar and clean waist; curved flared hem preserves the robe silhouette without pinched folds.

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
        path('robe',(16,6), [('L',(6,8)),('L',(6,26)),('L',(14,26)),('L',(14,28)),('C',(10,38),(14,33),(10,35)),('A',(14,42),4,4,False),('L',(34,42)),('A',(38,38),4,4,False),('C',(34,28),(38,35),(34,33)),('L',(34,26)),('L',(42,26)),('L',(42,8)),('L',(32,6)),('L',(16,6))],True)
        poly('lapel',(32,6),(24,20),(24,28));line('collar',(16,6),(24,20));join('lapel','robe');join('collar','robe');join('collar','lapel')
        poly('belt',(14,28),(24,28),(34,28));join('belt','robe');join('belt','lapel')
        line('tie',(24,28),(24,33));join('tie','belt');join('tie','lapel')
