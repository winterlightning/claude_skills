"""Walking turtle with a rounded shell, long neck and smoothly rounded muzzle.
Plan: Walking turtle with a rounded shell, long neck and smoothly rounded muzzle.
Construction: Lucide turtle: broad shell arc and rounded limb construction; original retains upright long neck.
Omissions: Eye and shell pattern omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '9c7c74da-c103-4fea-9bf5-13a249aa772b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/48-9c7c74da-c103-4fea-9bf5-13a249aa772b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='walking-turtle'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'video-games'
    aliases=()
    keywords=('walking', 'turtle')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('body',(4,32),[('A',(18,18),14,14,True),('A',(32,32),14,14,True),('L',(32,14)),('A',(38,8),6,6,True),('A',(44,14),6,6,True),('L',(44,18)),('A',(40,22),4,4,True),('L',(40,32)),('A',(32,40),8,8,True)])
        poly('belly',(4,32),(12,32),(32,32));join('body','belly')
        path('back-leg',(12,32),[('L',(8,36)),('C',(4,40),(6,38),(6,40))]);join('back-leg','belly')
