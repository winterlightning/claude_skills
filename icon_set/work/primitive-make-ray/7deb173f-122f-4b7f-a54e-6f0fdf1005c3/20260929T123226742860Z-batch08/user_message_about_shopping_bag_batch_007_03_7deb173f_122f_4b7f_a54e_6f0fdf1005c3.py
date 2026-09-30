"""The rejected speech outline has lost its tail, and the shopping bag reads as a padlock; restore the speech cue and bag shape. No written reviewer feedback.
Restored a speech tail, rounded the enclosure, and rebuilt the bag handle and side profile.
Construction: Lucide message-square original and atomic-debug; supplied bag and left-facing profile.
Omissions: Tiny facial details and the far speech wall omitted to retain a clear profile and bag.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7deb173f-122f-4b7f-a54e-6f0fdf1005c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__user-message-about-shopping-bag-batch-007-03/20260929T121814Z-thuan-mac/reference/shopping bag user message_7deb173f-122f-4b7f-a54e-6f0fdf1005c3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='user-message-about-shopping-bag-batch-007-03'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('user', 'message', 'about', 'shopping', 'bag', 'batch', '007', '03')

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

        self.path('bubble',(32,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,34)),('A',(10,38),4,4,False),('L',(16,39)),('L',(24,42)),('L',(24,39))])
        self.add_polyline('bag',(15,21),(25,21),(25,29),(15,29),closed=True)
        self.path('handle',(15,21),[('A',(25,21),5,6,True)]);self.relate('connect','handle','bag')
        self.path('profile',(42,16),[('C',(38,26),(38,16),(38,22)),('L',(34,31)),('L',(38,31)),('L',(38,38)),('A',(42,42),4,4,False)])
