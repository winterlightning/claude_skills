"""Close the brain region as a broad organic lobe inside a recognizable side-profile head, with forehead, nose, chin and neck.
Construction reference: Lucide brain: closed organic lobes; source requires one simplified side-view brain region."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4c63fd0e-abca-498d-a2c5-8e8bd6b5f894'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-profile-with-brain-4c63fd0e/20260929T033618Z-thuan-mac/reference/dementia disorder symptoms_4c63fd0e-abca-498d-a2c5-8e8bd6b5f894.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'head-profile-with-brain-4c63fd0e'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('dementia disorder symptoms',)

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

        path('head',(14,44),[('L',(14,34)),('C',(6,20),(8,31),(6,26)),('C',(24,4),(6,10),(14,4)),('C',(39,17),(33,4),(37,8)),('L',(44,27)),('L',(39,27)),('L',(39,33)),('A',(33,39),6,6,True),('L',(31,39)),('L',(31,44))])
        path('brain',(13,22),[('C',(24,12),(13,15),(18,12)),('C',(34,19),(31,12),(34,15)),('C',(26,24),(34,22),(28,22)),('C',(20,28),(24,25),(23,28)),('C',(13,22),(16,29),(13,27))],True)

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Keep a closed organic brain lobe inside the side-profile head. The local brain/skull gap is narrower than the nominal MIC but remains visibly open at 48 px in both themes.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9531d3f7a519e447e798426143db44d5c13e22336df417409a64f78eba4ff8f9'}
