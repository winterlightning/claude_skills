"""An oval durian with many evenly distributed broad spikes and a short stem. Bounds (8,4)-(40,44). Mirrored thorn series follows the reference silhouette.
Construction reference: No useful exact Lucide match; source thorn rhythm retained.
Omissions: Fine extra thorns reduced to twelve broad points."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6aba0722-424b-4f5e-95ea-9f8fc1a40e2c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spiky-durian-fruit/20260924T100518Z-thuan-mac/reference/durian_6aba0722-424b-4f5e-95ea-9f8fc1a40e2c.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spiky-durian-fruit'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('durian',)
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
        poly('fruit',(24,10),(29,7),(30,14),(37,12),(35,20),(40,22),(36,28),(40,32),(34,34),(35,41),(28,39),(24,44),(20,39),(13,41),(14,34),(8,32),(12,28),(8,22),(13,20),(11,12),(18,14),(19,7),(24,10),closed=True)
        line('stem',(24,4),(24,10));join('stem','fruit')
