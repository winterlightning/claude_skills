"""Restored two circular cuff bodies with separate wrist openings, flat lock housings and a narrow high arched connector.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide link: separate connected loops; original owns the two cuff housings and tall connector.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Lock rivets omitted; circular openings and rectangular housings retained."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '404190ff-389e-4a15-a7fe-4b448b432ffd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'handcuffs-with-arched-connector'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('handcuffs', 'with', 'arched', 'connector')

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

        for name,x in [('left',13),('right',35)]:
            path(name,(x-4,23),[('L',(x-4,20)),('L',(x+4,20)),('L',(x+4,23)),('C',(x+8,32),(x+7,25),(x+8,28)),('C',(x,42),(x+8,38),(x+5,42)),('C',(x-8,32),(x-5,42),(x-8,38)),('C',(x-4,23),(x-8,28),(x-7,25))],True)
            circle(name+'-opening',x,32,4)
        path('connector',(13,20),[('L',(13,16)),('C',(24,6),(13,10),(17,6)),('C',(35,16),(31,6),(35,10)),('L',(35,20))])
        self.relate('connect','connector','left');self.relate('connect','connector','right')
 