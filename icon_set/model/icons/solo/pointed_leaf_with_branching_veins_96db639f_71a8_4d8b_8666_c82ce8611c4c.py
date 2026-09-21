"""Simple Botanical Tree Leaf.

Plan: Pointed leaf, central stem and one mirrored pair of branching veins retained. Reduced the repeated vein count. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: Lucide leaf: coherent pointed silhouette and open midrib; fine side veins omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96db639f-71a8-4d8b-8666-c82ce8611c4c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/beech_96db639f-71a8-4d8b-8666-c82ce8611c4c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-leaf-with-branching-veins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pointed', 'leaf', 'with', 'branching', 'veins')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('leaf',(24,4),[('C',(40,27),(34,14),(40,20)),('C',(24,40),(40,35),(32,40)),('C',(8,27),(16,40),(8,35)),('C',(24,4),(8,20),(14,14))],True)
        line('vein',(24,17),(24,44));join('vein','leaf')
        line('right-vein',(24,30),(31,23));join('right-vein','vein')
        line('left-vein',(24,30),(17,23));join('left-vein','vein');join('left-vein','right-vein')
