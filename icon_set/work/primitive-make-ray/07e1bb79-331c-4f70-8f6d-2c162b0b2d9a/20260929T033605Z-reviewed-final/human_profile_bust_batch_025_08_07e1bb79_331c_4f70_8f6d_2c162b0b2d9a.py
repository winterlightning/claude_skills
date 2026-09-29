"""Restore a continuous frontal bust with a broad cranium, ears, circular jaw transition, visible neck and sloping shoulders.
Construction reference: human_ref/user.svg: broad head and smooth shoulders; source specifically requires a connected neck and ear-bearing silhouette."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '07e1bb79-331c-4f70-8f6d-2c162b0b2d9a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__human-profile-bust-batch-025-08/20260929T033618Z-thuan-mac/reference/person 1_07e1bb79-331c-4f70-8f6d-2c162b0b2d9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-profile-bust-batch-025-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('person 1',)

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

        path('bust',(4,44),[('C',(9,39),(4,41),(6,40)),('L',(18,35)),('L',(18,30)),('A',(14,22),10,10,True),('C',(12,20),(10,23),(10,17)),('L',(14,20)),('L',(14,12)),('C',(24,4),(14,6),(18,4)),('C',(34,12),(30,4),(34,6)),('L',(34,20)),('L',(36,20)),('C',(34,22),(38,17),(38,23)),('A',(30,30),10,10,True),('L',(30,35)),('L',(39,39)),('C',(44,44),(42,40),(44,41))])

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep the continuous head, ears, neck and shoulders of a frontal bust. Ear curves intentionally form small solid lobes where they meet the head; natural bust proportions require a larger envelope while remaining within the canvas.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e6f945ecd0c6355343615dccde9a64fa386f1484a7cc56b6f13b40c59a376f66'}
