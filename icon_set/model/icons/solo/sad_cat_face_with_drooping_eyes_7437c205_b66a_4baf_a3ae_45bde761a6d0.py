"""Sad Frowning Cat Face.

Plan: Sad cat face with two pointed ears, drooping eyelids and frown; bounds6,6,42,42.
Construction reference: Lucide cat: joined ear/head silhouette; source sad expression
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7437c205-b66a-4baf-a3ae-45bde761a6d0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sad cat_7437c205-b66a-4baf-a3ae-45bde761a6d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sad-cat-face-with-drooping-eyes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sad', 'cat', 'face', 'with', 'drooping', 'eyes')

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

        path('face',(8,6),[('L',(17,12)),('C',(31,12),(21,10),(27,10)),('L',(40,6)),('L',(40,18)),('C',(42,26),(42,21),(42,23)),('C',(24,42),(42,36),(34,42)),('C',(6,26),(14,42),(6,36)),('C',(8,18),(6,23),(6,21)),('L',(8,6))],True)
        line('eye-left',(15,23),(18,21));line('eye-right',(30,21),(33,23))
        path('mouth',(19,32),[('C',(29,32),(22,28),(26,28))])
