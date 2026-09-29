"""Restored a full-width browser toolbar with two control dots and a separate centered person symbol below it.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide panels-top-left: continuous toolbar divider. human_ref/user.svg: circular head and broad open shoulder arch; head (24,25), radius3, shoulders begin y36, exact detached 4px ink gap.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Browser controls reduced to two dots; profile remains detached from the outer frame."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3a3e4d85-115c-4ccb-82d1-46fd45222b3a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'browser-user-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('browser', 'user', 'profile')

    def build(self):

        def curve(name,start,c1,c2,end): self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start;ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L':self.add_line(part,point,end)
                elif kind=='C':curve(part,point,args[0],args[1],end)
                elif kind=='A':self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                ids.append(part);point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,True)],True)

        box('browser',6,6,42,42,4)
        self.add_line('toolbar',(6,16),(42,16))
        self.relate('connect','browser','toolbar')
        self.add_dot('control-a',(14,11));self.add_dot('control-b',(22,11))
        circle('head',24,25,3)
        path('shoulders',(15,40),[('C',(24,36),(16,37),(19,36)),('C',(33,40),(29,36),(32,37))])
 