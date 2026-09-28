"""A diagonal dental explorer with an arcing hook and short angled branch. Bounds (6,6)-(42,42); smooth tangent curve continues the diagonal shaft.
Construction reference: Lucide wrench: coherent diagonal tool silhouette; source hook curvature retained.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='34b397e2-5944-4499-8303-bd0af66a4a03'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__angled-dental-explorer-curved-tip/20260924T101756Z-thuan-mac/reference/tooth_34b397e2-5944-4499-8303-bd0af66a4a03.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='angled-dental-explorer-curved-tip'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('tooth',)
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
        path('tool',(6,42),[('L',(22,26)),('L',(36,12)),('C',(42,10),(39,9),(42,8)),('C',(32,6),(38,6),(35,6)),('C',(25,9),(29,6),(27,7))])
        line('branch',(22,26),(30,34));join('tool','branch')
