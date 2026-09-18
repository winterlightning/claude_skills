"""Asymmetric flame silhouette with a tall left tongue, shorter right tongue and open inner lick.
Keyshape VRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86d3e02f-ceb4-40f7-87dd-7409985eed4a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fireman_86d3e02f-ceb4-40f7-87dd-7409985eed4a.svg'
AUTHOR = 'gpt-6'
class Batch045Icon8(Solo48):
    icon_id = 'flame-with-inner-tongue-batch-045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('flame', 'fire', 'heat', 'burning', 'tongue', 'energy', 'blaze')
    # Reference: flame: asymmetric outer tongues and rounded base.
    # Reduction: Inner enclosed tongue reduced to open lick attached at base.
    # Bounds: (6, 2, 42, 46)
    def build(self):
        def path(name, start, *steps, closed=False):
            members=[]; p=start
            for i,step in enumerate(steps):
                q=step[1]
                if p == q: continue
                member=f"{name}-{i}"
                if step[0]=='L': self.add_line(member,p,q)
                else: self.add_arc(member,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                members.append(member); p=q
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

        path('flame',(20,4),('A',(28,24),20,24,True),('L',(40,14)),('L',(40,28)),('A',(8,28),16,16,True),('A',(16,14),8,14,True),('A',(20,4),10,12,False),closed=True)
        self.add_line('inner',(24,44),(24,28))
        self.relate('connect','flame','inner')
