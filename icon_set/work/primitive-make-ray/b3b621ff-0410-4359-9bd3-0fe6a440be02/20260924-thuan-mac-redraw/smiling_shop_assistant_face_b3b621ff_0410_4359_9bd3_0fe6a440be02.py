"""A friendly circular face with a smooth side-parted hairline. Radius20 centered24. Eyes and smile centered below the swept fringe; no detached body.
Construction reference: icon_set/references/human_ref/user.svg: circular head; source side-parted fringe retained.
Omissions: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b3b621ff-0410-4359-9bd3-0fe6a440be02'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__smiling-shop-assistant-face/20260924T100518Z-thuan-mac/reference/shop assistant_b3b621ff-0410-4359-9bd3-0fe6a440be02.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='smiling-shop-assistant-face'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('shop', 'assistant')
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
        path('face',(4,24),[('A',(8,12),20,20,True),('A',(24,4),20,20,True),('A',(40,12),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)],True)
        path('hair',(8,12),[('C',(28,10),(14,18),(22,17)),('C',(40,12),(31,16),(37,15))]);join('hair','face')
        for x in (18,30):self.add_dot('eye-'+str(x),(x,25))
        path('smile',(21,34),[('C',(27,34),(23,35),(25,35))])
