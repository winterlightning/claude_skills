"""Restored a diagonal bottle with a rounded body, two closed loop handles, broad collar and shaped nipple.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide baby informs simple rounded baby-product shapes; supplied original defines nipple, collar and handles.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Minor source contour irregularities simplified."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '46fff59c-84bf-4526-bd9b-33201133c81c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'baby-bottle-with-handles'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('baby', 'bottle', 'with', 'handles')

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

        path('bottle',(11,24),[('L',(25,10)),('L',(38,23)),('L',(24,37)),('C',(17,42),(21,40),(20,42)),('C',(13,40),(15,42),(14,41)),('L',(8,35)),('C',(8,28),(5,32),(6,30)),('L',(11,24))],True)
        path('collar',(25,10),[('C',(29,6),(23,7),(26,4)),('L',(42,19)),('C',(38,23),(45,22),(41,26)),('L',(25,10))],True)
        path('nipple',(29,6),[('C',(35,6),(31,7),(33,7)),('C',(42,13),(41,0),(48,7)),('C',(42,19),(42,15),(41,17))])
        path('left-handle',(11,24),[('C',(7,13),(5,24),(4,17)),('C',(17,13),(10,10),(14,10))])
        path('right-handle',(31,30),[('C',(35,40),(38,30),(39,36)),('C',(24,37),(31,43),(27,40))])
        self.relate('connect','bottle','collar')
        self.relate('connect','collar','nipple')
        self.relate('connect','bottle','left-handle')
        self.relate('connect','bottle','right-handle')
 