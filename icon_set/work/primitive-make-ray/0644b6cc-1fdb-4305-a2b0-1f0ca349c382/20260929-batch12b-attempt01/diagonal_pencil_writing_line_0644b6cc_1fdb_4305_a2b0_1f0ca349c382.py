"""Rejected pencil loses the eraser separator and graphite nib boundary and is too horizontal. Restore a steeper diagonal barrel with distinct rounded cap and nib.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0644b6cc-1fdb-4305-a2b0-1f0ca349c382'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-pencil-writing-line/20260929T132613Z-thuan-mac/reference/stylus_0644b6cc-1fdb-4305-a2b0-1f0ca349c382.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='diagonal-pencil-writing-line'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('stylus',)
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

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('pencil',(6,34),[('L',(10,22)),('L',(26,6)),('A',(38,18),9,9,True),('L',(18,34)),('L',(6,38)),('L',(6,34))],True)
        self.add_line('eraser-seam',(26,6),(38,18));join('eraser-seam','pencil')
        self.add_line('nib-base',(10,22),(18,34));join('nib-base','pencil')
        self.add_line('baseline',(20,42),(42,42))
