"""Restore the outer protective frame, curved glass chimney, top cap, broad base and asymmetric flame.
Construction reference: Lucide flame: asymmetric flowing flame; supplied original determines glass and protective frame."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e26b4fae-5159-5626-a3fd-b6d33103328d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hurricane-oil-lantern/20260929T033618Z-thuan-mac/reference/outdoors flame lantern_e26b4fae-5159-5626-a3fd-b6d33103328d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hurricane-oil-lantern'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives'
    aliases = ()
    keywords = ('outdoors flame lantern',)

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

        poly('cap',(16,4),(32,4),(32,10),(16,10),closed=True)
        path('glass',(18,10),[('C',(16,32),(15,20),(13,26)),('C',(24,38),(18,36),(20,38)),('C',(32,32),(28,38),(30,36)),('C',(30,10),(35,26),(33,20))])
        path('left-rail',(16,10),[('L',(13,10)),('C',(10,15),(11,10),(10,12)),('L',(8,34)),('A',(12,38),4,4,False),('L',(16,38))])
        path('right-rail',(32,10),[('L',(35,10)),('C',(38,15),(37,10),(38,12)),('L',(40,34)),('A',(36,38),4,4,True),('L',(32,38))])
        poly('base',(14,38),(34,38),(36,44),(12,44),closed=True)
        path('flame',(24,19),[('C',(20,28),(25,24),(20,24)),('A',(28,28),4,4,False),('C',(24,19),(28,24),(26,22))],True)
        for n in ['glass','left-rail','right-rail']:join('cap',n);join('base',n)
