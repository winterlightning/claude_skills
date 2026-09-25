"""Faceted Emerald Cut Gemstone.

Plan: Nested centered octagons with corresponding corner seams. Bounds6,6,42,42. Ring width9+.
Construction reference: gem.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1199c32a-830d-499e-b014-4e43c35e6e0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emerald_1199c32a-830d-499e-b014-4e43c35e6e0c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'octagonal-gem-with-inset-facet-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('octagonal', 'gem', 'with', 'inset', 'facet', 'ring')

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

        outer=[(16,6),(32,6),(42,16),(42,32),(32,42),(16,42),(6,32),(6,16)]
        inner=[(20,16),(28,16),(32,20),(32,28),(28,32),(20,32),(16,28),(16,20)]
        poly('outer',*outer,closed=True);poly('inner',*inner,closed=True)
        for j,(a,b) in enumerate(zip(outer,inner)):line(f'facet-{j}',a,b);join(f'facet-{j}','outer');join(f'facet-{j}','inner')
