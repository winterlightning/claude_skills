"""check-payment-give: A check above a pointing hand, with rounded check corners and a single coherent hand outline; source hand pose retained. Shared human-reference guidance reviewed; no detached figure.
Lucide construction: hand; original and atomic-debug inspected.
Omissions: Secondary writing lines and small folded fingers simplified; index finger and check retained.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3f6c05d9-0083-4007-be5b-cfc78f47999f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__check-payment-give/20260924T172457Z-thuan-mac/reference/check payment give_3f6c05d9-0083-4007-be5b-cfc78f47999f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'check-payment-give'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('check', 'payment', 'give')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('check',(12,26),[('L',(9,26)),('A',(6,23),3,3,True),('L',(6,9)),('A',(9,6),3,3,True),('L',(39,6)),('A',(42,9),3,3,True),('L',(42,23))])
        line('writing',(15,15),(22,15));line('amount',(31,15),(33,15))
        path('hand',(24,28),[('A',(32,28),4,4,True),('L',(32,34)),('L',(36,34)),('L',(36,36)),('A',(30,42),6,6,True),('L',(22,42)),('A',(16,36),6,6,True),('L',(16,34)),('L',(24,28))],True)
        line('finger',(24,28),(24,34));join('finger','hand')
