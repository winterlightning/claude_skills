"""Round baby face with side ears and smooth inward curl; no invented facial features."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '00cb164f-b36d-4ff3-a847-c9dbc18a9239'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-head-curl/20260925T060602Z-thuan-mac/reference/kid period_00cb164f-b36d-4ff3-a847-c9dbc18a9239.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'baby-head-curl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('kid period',)

    def build(self):
        # Symbol plan: Round baby face with side ears and smooth inward curl; no invented facial features.
        # Construction reference: Lucide baby; human_ref/user.svg; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('face',(8,20),[('C',(24,8),(9,12),(15,8)),('C',(40,20),(33,8),(39,12)),('A',(40,28),4,4,True),('C',(24,40),(39,36),(33,40)),('C',(8,28),(15,40),(9,36)),('A',(8,20),4,4,True)],True)
        path('curl',(28,9),[('L',(28,16)),('A',(20,16),4,4,True)]);join('curl','face')
