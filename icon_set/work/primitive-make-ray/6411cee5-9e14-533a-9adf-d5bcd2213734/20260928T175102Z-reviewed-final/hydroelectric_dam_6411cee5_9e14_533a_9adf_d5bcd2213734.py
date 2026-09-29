"""Paired sloping dam towers, horizontal upper spillway, two falling water strokes and separated coherent waves.
Construction: No useful subject match; geometric construction from the supplied original."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hydroelectric-dam/20260928T175102Z-thuan-mac/reference/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hydroelectric-dam'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('water dam',)

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

        # Mirrored towers expose exact bridge attachment nodes.
        for name,sign in [('left',1),('right',-1)]:
            x=lambda v: v if sign==1 else 48-v
            poly(name,(x(6),33),(x(8),6),(x(14),6),(x(14),10),(x(14),18),(x(11),33))
        line('bridge-top',(14,10),(34,10));line('bridge-bottom',(14,18),(34,18))
        for j,x in enumerate((21,28)):line(f'water-{j}',(x,24),(x,27))
        path('waterline',(6,33),[('C',(15,34),(9,31),(12,34)),('C',(24,32),(18,34),(21,32)),('C',(33,34),(27,32),(30,34)),('C',(42,33),(36,34),(39,31))])
        path('river',(6,41),[('C',(15,42),(9,39),(12,42)),('C',(24,40),(18,42),(21,40)),('C',(33,42),(27,40),(30,42)),('C',(42,41),(36,42),(39,39))])
        for t in ['left','right']:
            for b in ['bridge-top','bridge-bottom','waterline']:join(t,b)

# User authorized quality-preserving exceptions; approval binds this exact drawing.
Drawing.exception = {'reason': 'Retain two outlined sloping towers, two falling-water marks and two separated waves. Compact tower and water spacing remains readable at 48 px in both themes; forcing 4-unit gaps removes identifying dam detail.', 'approved_by': 'user-delegated-discretion-reviewed-by-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '92107b030e6846fd439a46588150b69a4c3c4b9754830cbed14dbe2b5563712a'}
