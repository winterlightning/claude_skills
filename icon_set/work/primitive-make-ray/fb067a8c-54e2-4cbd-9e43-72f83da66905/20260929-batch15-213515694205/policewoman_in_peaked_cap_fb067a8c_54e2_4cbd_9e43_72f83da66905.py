"""The rejected peaked cap is triangular and the chest pocket becomes a stray bottom stroke. Restore a broad shallow crown and curved visor over the circular jaw, with clean uniform shoulders.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and shoulder arch with touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fb067a8c-54e2-4cbd-9e43-72f83da66905'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__policewoman-in-peaked-cap/20260929T141901Z-thuan-mac/reference/police woman_fb067a8c-54e2-4cbd-9e43-72f83da66905.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='policewoman-in-peaked-cap'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('policewoman', 'in', 'peaked', 'cap')
    human_construction = "bust"
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

        poly('crown',(14,18),(8,6),(24,4),(40,6),(34,18))
        path('brim',(14,18),[('A',(34,18),10,2,False)]);join('brim','crown')
        path('jaw',(34,18),[('A',(14,18),10,10,True)]);join('jaw','brim');join('jaw','crown')
        for side,s in [('l',-1),('r',1)]:
         path('hair'+side,(24+s*10,18),[('C',(24+s*16,28),(24+s*10,23),(24+s*12,26))]);join('hair'+side,'jaw');join('hair'+side,'brim');join('hair'+side,'crown')
        path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('jaw','shoulders')
        line('seam',(24,32),(24,44));join('seam','shoulders')
