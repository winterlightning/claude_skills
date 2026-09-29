"""Rejected horns hand merges middle fingers into bumps and draws the thumb as a horizontal bar. Restore long index and little fingers, two folded knuckles, and a diagonally crossing thumb."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='288502c6-5133-5149-95a3-52e3acc6c690'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rock-horns-hand-with-crossing-thumb/20260929T044747Z-thuan-mac/reference/concert rock_288502c6-5133-5149-95a3-52e3acc6c690.svg'
AUTHOR='gpt-6'
PLAN='Rejected horns hand merges middle fingers into bumps and draws the thumb as a horizontal bar. Restore long index and little fingers, two folded knuckles, and a diagonally crossing thumb.'
CONSTRUCTION_REFERENCE='Previously inspected Lucide hand original and atoms: circular finger ends, continuous palm and articulated thumb.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rock-horns-hand-with-crossing-thumb'
    keyshape=Keyshape.VRECT_L
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
        self.path('hand',(10,27),[('L',(10,8)),('A',(18,8),4,4,True),('L',(18,22)),('C',(25,20),(18,17),(25,17)),('C',(32,22),(25,17),(32,17)),('L',(32,12)),('A',(40,12),4,4,True),('L',(40,30)),('C',(25,44),(40,39),(33,44)),('C',(10,33),(16,44),(10,39)),('L',(10,27))],True)
        self.path('thumb',(10,29),[('C',(17,24),(10,26),(13,24)),('L',(24,24)),('C',(24,31),(28,24),(28,31)),('L',(20,31)),('C',(23,36),(23,32),(23,34))])
        self.add_line('fold',(25,20),(25,24));self.relate('connect','hand','thumb','fold');self.relate('connect','thumb','fold')

Drawing.exception = {'reason': 'The two long raised fingers, folded middle knuckles and crossing thumb must remain. Compact inner finger gaps preserve the rock-horns hand pose.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '9a23d7f42abd0f926c24b7a1c2df0ec7902370b88d7ead01e591c748aa2c8d12'}
