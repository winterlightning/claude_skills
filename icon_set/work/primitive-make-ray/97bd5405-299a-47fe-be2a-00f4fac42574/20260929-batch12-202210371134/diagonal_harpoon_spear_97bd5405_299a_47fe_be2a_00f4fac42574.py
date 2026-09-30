"""Hook is too short and closes against shaft; restore long downward hook and more distinct barb.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful exact local Lucide match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='97bd5405-299a-47fe-be2a-00f4fac42574'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-harpoon-spear/20260929T131521Z-thuan-mac/reference/harpooner_97bd5405-299a-47fe-be2a-00f4fac42574.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='diagonal-harpoon-spear'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('diagonal', 'harpoon', 'spear')
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

        poly('shaft',(6,42),(26,22),(34,14))
        poly('tip',(34,14),(29,10),(42,6),(38,19),(34,14),closed=True);join('shaft','tip')
        path('hook',(26,22),[('L',(26,36)),('A',(14,36),6,6,True)]);join('hook','shaft')
