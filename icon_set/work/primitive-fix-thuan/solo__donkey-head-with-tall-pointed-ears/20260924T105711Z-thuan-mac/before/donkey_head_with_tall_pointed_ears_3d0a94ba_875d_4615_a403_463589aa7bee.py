"""Simple donkey head profile.

Plan: Left-facing long muzzle, two tall ears and angled neck retained. Omitted the tight nose seam. Keyshape VRECT_L uses its exact SOLO48 bounds; mirrored geometry only where the source supports it.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d0a94ba-875d-4615-a403-463589aa7bee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/donkey_3d0a94ba-875d-4615-a403-463589aa7bee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'donkey-head-with-tall-pointed-ears'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('donkey', 'head', 'with', 'tall', 'pointed', 'ears')

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

        path('head',(16,20),[('C',(10,30),(14,25),(10,26)),('C',(8,35),(8,32),(8,33)),('C',(15,40),(8,39),(11,40)),('L',(25,36)),('L',(31,44))])
        path('back',(25,36),[('C',(30,26),(29,35),(30,30)),('L',(40,35))]);join('head','back')
        path('ear-right',(16,20),[('C',(28,4),(17,12),(24,6)),('C',(28,20),(31,11),(30,16)),('L',(40,35))]);join('ear-right','head');join('ear-right','back')
        path('ear-left',(16,20),[('C',(10,4),(10,16),(10,10)),('C',(21,11),(16,5),(19,8))]);join('ear-left','head');join('ear-left','ear-right')
