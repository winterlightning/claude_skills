"""Use a broad arched headband, paired tall padded earcups and a long looping cable terminating in an explicit plug and jack.
Construction reference: Lucide headphones original and atomic-debug: continuous arch and paired rounded pads; source adds cable and plug."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3166725a-0332-4cff-bea4-228fc51449c2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__headphones-with-long-cable/20260929T033618Z-thuan-mac/reference/headphones cable_3166725a-0332-4cff-bea4-228fc51449c2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headphones-with-long-cable'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('headphones cable',)

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

        path('headband',(8,24),[('A',(40,24),16,18,True)])
        rounded('left-pad',8,18,16,35,4);rounded('right-pad',32,18,40,35,4)
        join('headband','left-pad');join('headband','right-pad')
        path('cable',(40,31),[('C',(40,43),(47,31),(47,43)),('L',(14,43))]);join('right-pad','cable')
        rounded('plug',6,40,14,46,3);line('jack',(2,43),(6,43));join('cable','plug');join('plug','jack')
