"""Unicorn head in profile with smooth muzzle, ear, mane and neck.
Plan: Unicorn head in profile with smooth muzzle, ear, mane and neck.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Eye and horn stripe omitted; horn, ear, muzzle and mane retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'cb062411-14bf-4e33-8b8d-aeec1ab4460f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-04/fantasy unicorn_cb062411-14bf-4e33-8b8d-aeec1ab4460f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='unicorn-head-in-profile'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases=()
    keywords=('unicorn', 'head', 'in', 'profile')

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
        path('unicorn',(16,18),[('L',(12,4)),('L',(28,16)),('C',(32,8),(28,12),(30,8)),('C',(36,20),(36,8),(36,16)),('C',(40,28),(38,22),(40,24)),('C',(36,33),(40,31),(36,31)),('C',(40,40),(36,36),(38,38)),('C',(32,44),(40,42),(36,44)),('L',(16,44)),('C',(20,30),(16,38),(18,34)),('C',(12,32),(18,33),(15,34)),('C',(8,26),(10,32),(8,29)),('C',(16,18),(8,22),(12,18))],True)
