"""Roman Centurion Helmet.

Plan: Crested helmet profile with cheek guard and face; bounds6,6,42,42. No tiny eye or neck ticks.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a7f7bab-3ca7-449f-9116-208c7295f691'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/centurion_0a7f7bab-3ca7-449f-9116-208c7295f691.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crested-centurion-helmet-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crested', 'centurion', 'helmet', 'profile')

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

        path('crest',(6,28),[('C',(30,6),(6,14),(14,6)),('C',(42,10),(35,6),(38,8)),('L',(36,18)),('C',(16,30),(22,10),(12,21)),('L',(6,28))],True)
        path('helmet',(16,30),[('C',(10,40),(15,35),(13,38)),('C',(24,32),(18,42),(22,36)),('C',(34,42),(26,38),(29,42)),('L',(34,30)),('L',(40,30)),('L',(36,18))]);join('helmet','crest')
