"""The rejected tailor square is just an L stroke and the skirt loses the tool proportions. Restore an outlined L ruler with marked divisions beside a flared skirt and broad waistband.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cb351c07-8fc6-42c1-8471-f516ff46710f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__skirt-beside-tailor-square/20260929T141901Z-thuan-mac/reference/fashion design measuring_cb351c07-8fc6-42c1-8471-f516ff46710f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='skirt-beside-tailor-square'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('skirt', 'beside', 'tailor', 'square')
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

        poly('ruler',(4,40),(4,8),(44,8),(44,16),(12,16),(12,40),(4,40))
        for x in (24,36):line('top-mark'+str(x),(x,8),(x,16));join('top-mark'+str(x),'ruler')
        line('side-mark',(4,28),(12,28));join('side-mark','ruler')
        poly('skirt',(24,24),(36,24),(40,32),(44,40),(20,40),(22,32),(24,24))
        line('waistband',(22,32),(40,32));join('waistband','skirt')
