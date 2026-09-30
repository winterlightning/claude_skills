"""Rejected cap has an angular projecting hook and omits both hair wings. Restore recognizable draping fabric, pompom and hair silhouette. No written reviewer feedback.
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='573cd435-465f-4569-b444-d50f28ac43d3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__woman-wearing-drooping-nightcap/20260929T124811Z-thuan-mac/reference/pajamas woman_573cd435-465f-4569-b444-d50f28ac43d3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='woman-wearing-drooping-nightcap'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pajamas', 'woman')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        # Circular face below the cap, asymmetric trailing point, paired open hair wings.
        path('hat',(6,26),[('L',(6,18)),('A',(18,6),12,12,True),('L',(28,6)),('A',(40,18),12,12,True),('L',(40,24)),('L',(30,16)),('L',(30,26)),('L',(6,26))],True)
        path('jaw',(30,26),[('A',(10,26),10,10,True)]);join('jaw','hat')
        circle('pompom',40,27,2);join('pompom','hat')
        path('hair-left',(6,26),[('L',(6,42)),('L',(18,42))]);join('hair-left','hat')
        path('hair-right',(30,26),[('L',(34,42)),('L',(26,42))]);join('hair-right','hat');join('hair-right','jaw')
