"""Rebuild two equally sized, low rounded links with inward openings and a centered horizontal connector. Keep the broad natural chain proportions.
Construction reference: Lucide link-2 original and atomic-debug: two opposed rounded ends and a separate central connector."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b4c96571-b91a-5c18-ae5c-9991078d4792'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-chain-link/20260929T033618Z-thuan-mac/reference/hyperlink_b4c96571-b91a-5c18-ae5c-9991078d4792.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-chain-link'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('hyperlink',)

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

        path('left-link',(21,19),[('A',(17,14),5,5,False),('L',(10,14)),('A',(4,20),6,6,False),('L',(4,28)),('A',(10,34),6,6,False),('L',(17,34)),('A',(21,29),5,5,False)])
        path('right-link',(27,19),[('A',(31,14),5,5,True),('L',(38,14)),('A',(44,20),6,6,True),('L',(44,28)),('A',(38,34),6,6,True),('L',(31,34)),('A',(27,29),5,5,True)])
        line('connector',(16,24),(32,24))

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep the two broad low chain links and centered connecting bar. The shorter envelope and compact local link/bar openings preserve natural chain proportions; both openings remain visible at 48 px.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b97fb1e971e0894de1ae6283615d859697948e448699f79990f90f180d67d197'}
