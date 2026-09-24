"""A diagonal grain head with two broad overlapping curved bracts and a short stem. Square extremes (6,6)-(42,42). Natural diagonal asymmetry retained.
Construction reference: Lucide wheat: curved grain lobes; supplied reference owns the single-ear silhouette.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8c67d503-423f-4f89-820c-06ea16117fe2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__single-wheat-ear/20260924T100518Z-thuan-mac/reference/protein gluten wheat_8c67d503-423f-4f89-820c-06ea16117fe2.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='single-wheat-ear'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('protein', 'gluten', 'wheat')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('grain',(12,36),[('C',(10,21),(5,30),(6,26)),('L',(16,14)),('L',(24,6)),('L',(28,15)),('C',(42,6),(32,7),(35,6)),('C',(32,23),(42,14),(38,20)),('L',(42,26)),('L',(29,39)),('C',(12,36),(22,44),(15,39))],True)
        path('bract',(16,14),[('C',(32,32),(14,28),(22,34)),('L',(36,32))]);join('grain','bract')
        line('stem',(6,42),(12,36));join('stem','grain')
