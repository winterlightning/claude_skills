"""A right-facing human head wearing a rounded VR visor and horizontal strap. Bounds (8,4)-(40,44). Continuous neck, circular crown and separately rounded visor.
Construction reference: Lucide headset: rounded equipment housing; human user reference for rounded head silhouette.
Omissions: Small nose step simplified."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='333b76cc-b37e-568d-8fc3-aa0f76f2f559'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vr-headset/20260924T101756Z-thuan-mac/reference/vr headset_333b76cc-b37e-568d-8fc3-aa0f76f2f559.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='vr-headset'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('vr', 'headset')
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
        path('profile',(16,44),[('L',(16,37)),('C',(8,22),(10,30),(8,26)),('L',(8,19)),('A',(23,4),15,15,True),('C',(34,12),(29,4),(32,8))])
        path('visor',(30,12),[('L',(34,12)),('L',(37,12)),('A',(40,15),3,3,True),('L',(40,23)),('A',(37,26),3,3,True),('L',(30,26)),('A',(23,19),7,7,True),('A',(30,12),7,7,True)],True)
        join('profile','visor')
        line('strap',(8,19),(23,19));join('strap','profile');join('strap','visor')
        path('face',(36,26),[('L',(38,34)),('L',(32,34)),('L',(32,36)),('A',(28,40),4,4,True),('L',(25,40)),('L',(25,44))]);join('face','visor')
