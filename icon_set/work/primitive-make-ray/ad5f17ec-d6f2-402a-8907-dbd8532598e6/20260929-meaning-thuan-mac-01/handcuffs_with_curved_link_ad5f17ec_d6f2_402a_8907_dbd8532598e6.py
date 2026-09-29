"""Restored two double-ring cuffs at staggered heights, rectangular locking collars, and a long curved connecting link.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide link: curved connection between loop structures; source defines staggered cuff placement and broad loop connector.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Tiny locking rivets omitted; both inner cuff holes and lock collars retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ad5f17ec-d6f2-402a-8907-dbd8532598e6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handcuffs-with-curved-link'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('handcuffs', 'with', 'curved', 'link')

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

        circle('left-outer',13,34,9);circle('left-inner',13,34,4)
        circle('right-outer',35,22,9);circle('right-inner',35,22,4)
        path('left-lock',(9,26),[('L',(9,22)),('A',(11,20),2,True),('L',(17,20)),('A',(19,22),2,True),('L',(19,27))])
        path('right-lock',(28,16),[('L',(25,13)),('L',(31,8)),('L',(35,13))])
        path('link',(13,20),[('C',(5,9),(10,16),(3,15)),('C',(17,6),(7,4),(11,3)),('C',(27,11),(21,6),(24,8))])
 