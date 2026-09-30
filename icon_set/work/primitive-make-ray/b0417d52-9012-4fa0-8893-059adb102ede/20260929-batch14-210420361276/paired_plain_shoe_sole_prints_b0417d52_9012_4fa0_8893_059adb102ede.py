"""The rejected soles are uniform pill shapes. Restore broad rounded toes, inward-curved waists and separated heels.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b0417d52-9012-4fa0-8893-059adb102ede'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__paired-plain-shoe-sole-prints/20260929T135704Z-thuan-mac/reference/shoe prints_b0417d52-9012-4fa0-8893-059adb102ede.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='paired-plain-shoe-sole-prints'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('paired', 'plain', 'shoe', 'sole', 'prints')
    def build(self):

        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for j,l in enumerate((6,28)):
         n='sole'+str(j)
         path(n,(l,18),[('A',(l+14,18),7,12,True),('C',(l+12,30),(l+14,23),(l+12,26)),('L',(l+12,33)),('L',(l+12,36)),('C',(l+7,42),(l+12,40),(l+10,42)),('C',(l+2,36),(l+4,42),(l+2,40)),('L',(l+2,33)),('L',(l+2,30)),('C',(l,18),(l+2,26),(l,23))],True)
         line(n+'heel',(l+2,33),(l+12,33));join(n,n+'heel')
