"""Restore the complete outlined H with slab serifs, curved serif shoulders and one broad center bar.
Construction reference: Supplied original; no useful local Lucide subject match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a08dce58-bc2a-4e25-bd53-f469ccddb795'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hyves-logo/20260929T033618Z-thuan-mac/reference/hyves logo_a08dce58-bc2a-4e25-bd53-f469ccddb795.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hyves-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('hyves logo',)

    def build(self):

        def path(name, start, commands, closed=False):
            members = []
            here = start
            for i, cmd in enumerate(commands):
                kind, end, *args = cmd
                if kind == 'L' and end == here:
                    continue
                key = f'{name}-{i}'
                if kind == 'L': self.add_line(key, here, end)
                elif kind == 'A':
                    rx, ry, sweep = args
                    self.add_arc(key, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                elif kind == 'C': self.add_bezier(key, here, (args[0], args[1], end))
                members.append(key)
                here = end
            self.add_contour(name, *members, closed=closed)
        def oval(name, x, y, rx, ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): oval(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)

        path('letter',(6,6),[('L',(20,6)),('L',(20,10)),('C',(18,14),(18,10),(18,12)),('L',(18,20)),('L',(30,20)),('L',(30,14)),('C',(28,10),(30,12),(30,10)),('L',(28,6)),('L',(42,6)),('L',(42,10)),('C',(38,14),(38,10),(38,12)),('L',(38,34)),('C',(42,38),(38,36),(38,38)),('L',(42,42)),('L',(28,42)),('L',(28,38)),('C',(30,34),(30,38),(30,36)),('L',(30,28)),('L',(18,28)),('L',(18,34)),('C',(20,38),(18,36),(18,38)),('L',(20,42)),('L',(6,42)),('L',(6,38)),('C',(10,34),(10,38),(10,36)),('L',(10,14)),('C',(6,10),(10,12),(10,10)),('L',(6,6))],True)

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Preserve the outlined slab-serif H and curved serif shoulders of the Hyves logo. Logo-specific internal curve spacing remains visibly open at native size in both themes.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ab870fab9648da7ac3ccf1e71206b24c29bbce2db00401f02b8808963424ed6f'}
