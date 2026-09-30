"""The rejected helmet has a bowl-like visor and a plain central uniform stripe. Restore a straight helmet band and an open V collar under the round face.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: human_ref/user.svg: circular jaw and rounded shoulders with touching bust ink.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1c9b753f-2008-485b-b32d-95627b609d40'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__policewoman-with-rounded-helmet/20260929T141901Z-thuan-mac/reference/police woman_1c9b753f-2008-485b-b32d-95627b609d40.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='policewoman-with-rounded-helmet'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('policewoman', 'with', 'rounded', 'helmet')
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

        path('helmet',(12,16),[('A',(36,16),12,12,True)])
        line('brim',(12,16),(36,16));join('brim','helmet')
        path('jaw',(36,16),[('A',(12,16),12,12,True)]);join('jaw','helmet');join('jaw','brim')
        for side,s in [('l',-1),('r',1)]:
         path('hair'+side,(24+s*12,16),[('C',(24+s*16,26),(24+s*12,21),(24+s*14,25))]);join('hair'+side,'jaw');join('hair'+side,'brim');join('hair'+side,'helmet')
        path('shoulders',(8,44),[('L',(8,40)),('C',(16,34),(8,36),(12,34)),('C',(24,32),(18,32),(21,32)),('C',(32,34),(27,32),(30,32)),('C',(40,40),(36,34),(40,36)),('L',(40,44))]);join('jaw','shoulders')
        poly('collar',(16,34),(24,42),(32,34));join('collar','shoulders')
