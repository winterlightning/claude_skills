"""The rejected voicemail loops are elongated ovals; restore the two matching circular reels and shared baseline. No written reviewer feedback.
Replaced elongated oval reels with matching circular loops joined at their bottom tangents.
Construction: Lucide voicemail original and atomic-debug: two circular loops and tangent bridge.
Omissions: None.
Keyshape: CIRCLE. Radial centerline limit 20 around (24,24), preserving the natural circular or slender subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='06fe9ad6-66bf-5efc-9afe-5d64c2e9319b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__voicemail-symbol/20260929T121814Z-thuan-mac/reference/phone actions voice mail_06fe9ad6-66bf-5efc-9afe-5d64c2e9319b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='voicemail-symbol'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('voicemail', 'symbol')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.circle('left',12,24,8);self.circle('right',36,24,8)
        self.add_line('bridge',(12,32),(36,32));self.relate('connect','bridge','left');self.relate('connect','bridge','right')
