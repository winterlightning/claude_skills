"""The rejected spool has one slash and an open lower outline. Restore multiple alternating diagonal wraps and complete both projecting spool ends.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3794c4a3-1075-45aa-82dc-09c95bb51de3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spool-wrapped-with-thread/20260929T141901Z-thuan-mac/reference/fiber_3794c4a3-1075-45aa-82dc-09c95bb51de3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='spool-wrapped-with-thread'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('spool', 'wrapped', 'with', 'thread')
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

        box('thread-body',8,12,40,36,2)
        poly('top-core',(16,12),(16,4),(32,4),(32,12));join('top-core','thread-body')
        poly('bottom-core',(16,36),(16,44),(32,44),(32,36));join('bottom-core','thread-body')
        poly('wraps',(36,12),(8,20),(40,28),(12,36));join('wraps','thread-body')
        line('tail',(32,44),(40,44));join('tail','bottom-core')
