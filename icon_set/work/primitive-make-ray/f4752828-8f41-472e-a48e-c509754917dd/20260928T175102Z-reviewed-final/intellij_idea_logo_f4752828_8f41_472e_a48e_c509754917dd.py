"""A continuous thick-outline J-shaped emblem, circular counter and matched vertical capsule; retain three separate components.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f4752828-8f41-472e-a48e-c509754917dd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__intellij-idea-logo/20260928T175102Z-thuan-mac/reference/intellijidea logo_f4752828-8f41-472e-a48e-c509754917dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'intellij-idea-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('intellijidea logo',)

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

        path('hook',(8,8),[('L',(24,8)),('A',(28,12),4,4,True),('L',(28,24)),('A',(12,40),16,16,True),('L',(8,40)),('A',(8,32),4,4,True),('L',(12,32)),('A',(20,24),8,8,False),('L',(20,16)),('L',(8,16)),('A',(8,8),4,4,True)],True)
        circle('counter',11,24,3)
        rounded('bar',36,8,44,40,4)

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Retain the circular counter inside the curved emblem and the separate capsule. The small-circle counter is distinct in both themes; the compact emblem cannot keep the source proportions with a 4-unit gap around that counter.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ea94edbec186249dfdd4eb9ad731a146280fa7734dcd2f8a8a1b8c56d48136d4'}
