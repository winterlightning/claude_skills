"""Bent pick with an oblong grip entering an open padlock.
SQUARE (6,6)..(42,42) balances the lower-left tool against the upper-right lock.
The diagonal capsule has radius 5, integer tangent endpoints, and a split arc
at its genuine pick attachment. Omit the crowded left/bottom lock edges as
in the reference; reduce the keyhole to a short slot. Lucide lock-open informs
the rounded housing and detached shackle end; all geometry is reauthored.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f4d0d07-e981-4efd-ae8c-b673077a9b75'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crime tools loackpick unlock_7f4d0d07-e981-4efd-ae8c-b673077a9b75.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'pick-entering-open-padlock'
    keyshape = Keyshape.SQUARE
    category = 'Uncategorized'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ['Lockpicking a Padlock']
    keywords = ['padlock','pick','lockpicking','keyhole','shackle','tool','security']
    def build(self):


        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        path('lock',(24,24),[(38,24),((42,28),4,4,True),(42,38),((38,42),4,4,True),(32,42)])
        path('shackle',(24,24),[(24,15),((42,15),9,9,True)]);join('lock','shackle')
        path('handle',(8,33),[(12,30),((19,31),5,5,True),((18,38),5,5,True),(14,41),((8,33),5,5,True)],True)
        poly('pick',(19,31),(25,34),(30,34))
        line('keyhole',(30,33),(30,34))
        join('pick','handle');join('pick','keyhole')
