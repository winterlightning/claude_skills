"""Inverted skier with bent raised legs, two skis, extended arm and upright pole stroke. SQUARE balances the action. Shared full_body_ref.png informed head and round-ended limbs. Head center (28,38), radius4, upper torso junction (28,26): 38-4-26=8 centerline /4 ink gap. Omit pole basket and clothing detail. Asymmetry preserves the upside-down pose.

Symbol plan: SQUARE; visible bounds (4, 4, 44, 44). SOLO48, stroke4.
Source reference inspected from exported batch SVG. Author: gpt-6.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95760764-05e8-4308-8e26-5b559bc41d45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/free skiiing 1_95760764-05e8-4308-8e26-5b559bc41d45.svg'
AUTHOR = 'gpt-6'

def _circle(icon, name, x, y, r):
    icon.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
    icon.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def _path(icon, name, start, commands, closed=False):
    members=[]; p=start
    for i,c in enumerate(commands):
        n=f'{name}-{i}'; q=c[1]
        if c[0]=='L': icon.add_line(n,p,q)
        else: icon.add_arc(n,p,q,radius_x=c[2],radius_y=c[3] if len(c)>3 else c[2],sweep=c[4] if len(c)>4 else True)
        p=q; members.append(n)
    icon.add_contour(name,*members,closed=closed)

class Batch051Icon(Solo48):
    icon_id = 'inverted-freestyle-skier-batch-051'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('skier', 'skiing', 'inverted', 'freestyle', 'skis', 'pole', 'sport')

    def build(self):
        _circle(self,'head',28,38,4)
        self.add_line('torso',(28,26),(28,22))
        self.add_polyline('leg-one',(28,22),(18,10),(6,10))
        self.add_polyline('leg-two',(28,22),(16,22),(6,22))
        for n,y in enumerate((10,22)):
            self.add_line('ski-'+str(n),(6,y-4),(6,y+4))
            self.relate('connect','ski-'+str(n),'leg-'+('one' if n==0 else 'two'))
        self.add_polyline('arm',(28,26),(42,22),(42,6))
        for n in ('leg-one','leg-two','arm'): self.relate('connect','torso',n)
        self.relate('connect','leg-one','leg-two')
        self.mark_human_figure('skier',head='head',torso='torso',torso_junction='start')
