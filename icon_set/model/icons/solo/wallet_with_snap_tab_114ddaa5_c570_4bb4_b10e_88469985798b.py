"""Wallet with a projecting card and smoothly rounded snap tab.
Plan: Wallet with a projecting card and smoothly rounded snap tab.
Construction: Lucide wallet: clean tab and shell; source provides tilted projecting card.
Omissions: Tiny snap dot omitted; tab retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '114ddaa5-c570-4bb4-b10e-88469985798b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/wallet_114ddaa5-c570-4bb4-b10e-88469985798b.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='wallet-with-snap-tab'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('wallet', 'with', 'snap', 'tab')

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
        path('wallet-right',(40,24),[('L',(40,20)),('A',(36,16),4,4,False)])
        path('wallet',(12,16),[('L',(8,16)),('A',(4,20),4,4,False),('L',(4,36)),('A',(8,40),4,4,False),('L',(36,40)),('A',(40,36),4,4,False),('L',(40,32))])
        path('card',(12,16),[('L',(28,9)),('C',(32,8),(30,8),(31,8)),('A',(36,12),4,4,True),('L',(36,16))]);join('card','wallet');join('card','wallet-right')
        path('tab',(40,24),[('L',(34,24)),('A',(30,28),4,4,False),('A',(34,32),4,4,False),('L',(42,32)),('A',(44,30),2,2,False),('L',(44,26)),('A',(42,24),2,2,False),('L',(40,24))],True);join('tab','wallet');join('tab','wallet-right')
