"""The rejected slippers are uniform capsules with straight bars. Restore bulbous toes, tapered heels and curved vamp seams.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4862863c-9e5e-4805-9d30-b6bc2429589b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pair-of-rounded-house-slippers/20260929T135633Z-thuan-mac/reference/moccasins_4862863c-9e5e-4805-9d30-b6bc2429589b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pair-of-rounded-house-slippers'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('pair', 'of', 'rounded', 'house', 'slippers')
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
         n='slipper'+str(j)
         path(n,(l,18),[('A',(l+14,18),7,12,True),('C',(l+13,29),(l+14,22),(l+13,26)),('L',(l+12,36)),('C',(l+7,42),(l+11,41),(l+10,42)),('C',(l+2,36),(l+4,42),(l+3,41)),('L',(l+1,29)),('C',(l,18),(l+1,26),(l,22))],True)
         path(n+'vamp',(l+1,29),[('C',(l+13,29),(l+5,25),(l+9,25))]);join(n,n+'vamp')
