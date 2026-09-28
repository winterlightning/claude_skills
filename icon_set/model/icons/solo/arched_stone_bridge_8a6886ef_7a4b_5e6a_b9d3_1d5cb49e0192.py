"""Replace the flattened arc wave with two identical smooth waves, each made from tangent-matched curves. Keep the approved single stone arch.
Reference: Local Lucide waves-horizontal and supplied stone bridge; repeated smooth wave construction
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/bridge_8a6886ef-7a4b-5e6a-b9d3-1d5cb49e0192.svg'
AUTHOR = 'gpt-6'

class ArchedStoneBridge(Solo48):
    icon_id = 'arched-stone-bridge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('arched', 'stone', 'bridge')

    def build(self):
        # Symbol plan: Replace the flattened arc wave with two identical smooth waves, each made from tangent-matched curves. Keep the approved single stone arch.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        line('deck',(4,8),(44,8))
        path('bridge',(4,8),[('L',(4,27)),('L',(14,27)),('L',(14,26)),('A',(34,26),10,10,True),('L',(34,27)),('L',(44,27)),('L',(44,8))]);join('deck','bridge')
        path('water',(4,40),[('C',(14,36),(8,40),(10,36)),('C',(24,40),(18,36),(20,40)),('C',(34,36),(28,40),(30,36)),('C',(44,40),(38,36),(40,40))])
