"""Head is bulky and jets shrink unevenly. Use a clean diagonal dome and equal parallel jets.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: shower-head: diagonal face and separate jets
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a384c77d-8674-4738-9d1b-23923510b862'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__curved-showerhead-water-jets/20260929T131521Z-thuan-mac/reference/light rain sensor_a384c77d-8674-4738-9d1b-23923510b862.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='curved-showerhead-water-jets'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('curved', 'showerhead', 'water', 'jets')
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

        path('pipe',(42,42),[('L',(42,16)),('A',(32,6),10,10,False),('L',(30,6)),('L',(22,14))])
        path('head',(10,18),[('C',(22,14),(14,14),(18,14)),('C',(26,34),(33,14),(34,26)),('L',(10,18))],True);join('head','pipe')
        for j,(x,y) in enumerate([(12,30),(20,38)]):line(f'jet-{j}',(x,y),(x-6,y+4))
