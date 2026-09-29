"""Rejected little hanging zigzag and U shapes do not show pulling a towel. Restore a broad dispenser, hanging sheet with torn edge, and two gripping hands."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='8e334d1c-5734-4a71-968a-6135a8683135'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pulling-paper-towel/20260929T041010Z-thuan-mac/reference/wayfinding tissue_8e334d1c-5734-4a71-968a-6135a8683135.svg'
AUTHOR='gpt-6'
PLAN='Rejected little hanging zigzag and U shapes do not show pulling a towel. Restore a broad dispenser, hanging sheet with torn edge, and two gripping hands.'
CONSTRUCTION_REFERENCE='Lucide hand: bent fingers and round joints; dispenser and sheet from original.'
OMISSIONS='Two grips retained; tiny dispenser sensor omitted.'
class Drawing(Solo48):
    icon_id='pulling-paper-towel'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.box('dispenser',6,6,42,23,4)
        self.path('sheet',(14,21),[('L',(14,38)),('L',(17,42)),('L',(21,39)),('L',(25,42)),('L',(29,39)),('L',(34,42)),('L',(34,21))])
        self.add_line('slot',(14,21),(34,21))
        self.path('left-hand',(6,42),[('L',(6,33)),('C',(10,29),(6,31),(8,30)),('L',(14,27)),('L',(14,33)),('L',(19,30))])
        self.path('right-hand',(42,42),[('L',(42,33)),('C',(38,29),(42,31),(40,30)),('L',(34,27)),('L',(34,33)),('L',(29,30))])
        self.relate('connect','dispenser','sheet','slot'); self.relate('connect','sheet','left-hand','right-hand','slot')
