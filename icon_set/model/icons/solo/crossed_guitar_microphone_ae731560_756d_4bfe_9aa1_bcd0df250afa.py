"""Crossed guitar and microphone with rounded lobes and a smooth microphone capsule.
Plan: Crossed guitar and microphone with rounded lobes and a smooth microphone capsule.
Construction: No useful exact compound match; source controls diagonal crossing; circular lobes and coherent cubic transitions.
Omissions: Sound hole, strings and microphone seam omitted for spacing."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'ae731560-756d-4bfe-9aa1-bcd0df250afa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/party music_ae731560-756d-4bfe-9aa1-bcd0df250afa.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='crossed-guitar-microphone'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('crossed', 'guitar', 'microphone')

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
        path('guitar',(6,34),[('C',(13,26),(6,28),(8,26)),('C',(18,22),(17,26),(16,24)),('L',(32,8)),('L',(40,16)),('L',(26,30)),('C',(24,36),(24,32),(28,33)),('C',(14,42),(21,40),(18,42)),('A',(6,34),8,8,True)],True)
        path('mic',(18,22),[('L',(8,12)),('C',(12,6),(4,8),(8,6)),('C',(16,8),(14,6),(15,7)),('L',(24,16))])
        line('mic-handle',(28,28),(42,42));join('mic-handle','guitar');join('mic','guitar')
