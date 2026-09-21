"""Radio Antenna with Signal Waves.

Plan: Antenna with two pairs of side waves; bounds6,6,42,42. Head circle radius2 at24,20, shaft ends42. Upper/lower wave ends preserve opening.
Construction reference: Lucide radio: mirrored signal arcs around circular emitter
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd52ef05a-9efa-4acd-b331-27a67a8c21f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antennae_d52ef05a-9efa-4acd-b331-27a67a8c21f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slender-antenna-with-paired-signal-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('slender', 'antenna', 'with', 'paired', 'signal', 'arcs')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        circle('head',24,20,2);line('shaft',(24,22),(24,40));join('head','shaft')
        path('inner-left',(15,12),[('A',(15,28),2,8,False)])
        path('inner-right',(33,12),[('A',(33,28),2,8,True)])
        path('outer-left',(6,8),[('A',(6,32),2,12,False)])
        path('outer-right',(42,8),[('A',(42,32),2,12,True)])
