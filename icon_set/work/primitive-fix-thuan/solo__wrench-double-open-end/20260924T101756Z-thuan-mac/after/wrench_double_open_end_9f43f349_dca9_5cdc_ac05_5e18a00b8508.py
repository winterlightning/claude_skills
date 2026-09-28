"""A diagonal double-ended open wrench with rounded jaw shoulders and two angled jaw mouths. Bounds (6,6)-(42,42); halves mirror around (24,24).
Construction reference: Lucide wrench: curved open jaw and diagonal shaft; source duplicated open jaw retained.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9f43f349-dca9-5cdc-ac05-5e18a00b8508'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wrench-double-open-end/20260924T101756Z-thuan-mac/reference/wrench right_9f43f349-dca9-5cdc-ac05-5e18a00b8508.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='wrench-double-open-end'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('wrench', 'right')
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
        path('wrench',(29,6),[('C',(39,7),(32,6),(36,6)),('L',(30,14)),('L',(34,18)),('L',(42,13)),('C',(42,17),(42,11),(42,14)),('C',(31,24),(42,24),(35,26)),('L',(24,31)),('C',(17,42),(26,35),(24,42)),('C',(7,41),(13,42),(10,42)),('L',(18,34)),('L',(14,30)),('L',(6,35)),('C',(6,31),(6,36),(6,33)),('C',(17,24),(6,24),(13,22)),('L',(24,17)),('C',(29,6),(22,13),(23,6))],True)
