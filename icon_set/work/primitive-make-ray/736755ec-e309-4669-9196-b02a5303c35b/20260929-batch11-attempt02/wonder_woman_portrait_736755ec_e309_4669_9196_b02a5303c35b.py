"""Rejected face and pointed tiara are undersized inside a generic hair arch. Enlarge face, restore distinct crown and long hair above shoulders. No written reviewer feedback.
Construction: Lucide sticky-note fold junction and glasses rounded lobes where relevant.
Portraits use human_ref/user.svg circular facial construction; no body for the nightcap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='736755ec-e309-4669-9196-b02a5303c35b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wonder-woman-portrait/20260929T124811Z-thuan-mac/reference/wonder woman_736755ec-e309-4669-9196-b02a5303c35b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='wonder-woman-portrait'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('wonder', 'woman')
    human_construction='bust'
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

        # Circular jaw radius10; shoulder apex36 is four centerline units below jaw32 (touching ink).
        path('crown',(14,18),[('L',(14,14)),('L',(24,6)),('L',(34,14)),('L',(34,18))])
        path('face',(14,18),[('L',(14,22)),('A',(34,22),10,10,False),('L',(34,18))]);join('crown','face')
        self.add_line('tiara',(14,18),(34,18));join('tiara','crown');join('tiara','face')
        path('hair-left',(14,18),[('A',(6,26),8,8,False),('L',(6,42))]);join('hair-left','crown');join('hair-left','face')
        path('hair-right',(34,18),[('A',(42,26),8,8,True),('L',(42,42))]);join('hair-right','crown');join('hair-right','face')
        path('shoulders',(6,42),[('A',(24,36),18,6,True),('A',(42,42),18,6,True)]);join('shoulders','hair-left');join('shoulders','hair-right');join('shoulders','face')
