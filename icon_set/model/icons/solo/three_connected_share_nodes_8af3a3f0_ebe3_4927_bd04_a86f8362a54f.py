"""Three Connected Share Nodes.

Plan: Three matching round nodes with diagonal connecting branches; bounds8,4,40,44. Node radii6, true cardinal joins.
Construction reference: share-2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8af3a3f0-ebe3-4927-bd04-a86f8362a54f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/share node_8af3a3f0-ebe3-4927-bd04-a86f8362a54f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-connected-share-nodes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'connected', 'share', 'nodes')

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

        for n,x,y in [('left',14,24),('upper',34,10),('lower',34,38)]:
         path(n,(x-6,y),[('A',(x,y-6),6,6,True),('A',(x+6,y),6,6,True),('A',(x,y+6),6,6,True),('A',(x-6,y),6,6,True)],True)
        line('upper-link',(20,24),(28,10));line('lower-link',(20,24),(28,38))
        join('upper-link','left');join('upper-link','upper');join('lower-link','left');join('lower-link','lower');join('upper-link','lower-link')
