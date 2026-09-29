"""Shortened the prongs, rebuilt a rounder cable loop and preserved an open cable end clear of the plug."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='79eae0ea-a0a3-48d0-a56a-a874914d50c3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__looped-power-cable-79eae0ea/20260928T171406Z-thuan-mac/reference/circle cable_79eae0ea-a0a3-48d0-a56a-a874914d50c3.svg'
AUTHOR='gpt-6'
PLAN='Shortened the prongs, rebuilt a rounder cable loop and preserved an open cable end clear of the plug.'
CONSTRUCTION_REFERENCE='Lucide plug: rounded plug head and equal paired prongs; original: circular looping cable.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='looped-power-cable-79eae0ea'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('looped', 'power', 'cable', '79eae0ea')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        self.path('plug',(26,4),[('L',(32,4)),('L',(32,6)),('L',(32,14)),('L',(32,16)),('L',(26,16)),('A',(20,10),6,6,True),('A',(26,4),6,6,True)],True)
        for y in (6,14):
            self.add_line(f'prong-{y}',(32,y),(38,y));self.relate('connect','plug',f'prong-{y}')
        self.path('cable',(20,10),[('C',(6,26),(12,10),(6,17)),('A',(24,44),18,18,False),('A',(42,26),18,18,False),('C',(42,24),(42,25),(42,25))])
        self.relate('connect','cable','plug')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'The rounded cable loop and compact plug require 2-unit top/bottom canvas insets beyond the square guide. The complete loop, two prongs and free cable end are distinct; all automatic spacing checks pass.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '67b99fcdda21b330a59305cf9c09de8149814ab74bf3fe7fae43ffca4f893587'}
