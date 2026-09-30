"""Circular emblem reduced to a narrow arch with banner across its middle. Restore circular medallion above a low banner.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: award: round medallion hierarchy
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cb339990-49e6-46a8-ad97-83dd4ad21af5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__circular-emblem-with-banner/20260929T131521Z-thuan-mac/reference/intellectual property and tradmark_cb339990-49e6-46a8-ad97-83dd4ad21af5.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circular-emblem-with-banner'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('circular', 'emblem', 'with', 'banner')
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

        path('seal',(10,28),[('C',(8,20),(8,26),(8,23)),('A',(24,6),16,14,True),('A',(40,20),16,14,True),('C',(38,28),(40,23),(40,26))])
        oval('inner',24,20,7,6)
        poly('banner',(6,34),(42,34),(36,38),(42,42),(6,42),(12,38),closed=True)
