"""Repair first-pass spacing and exact attachment nodes in fresh runs only."""
from pathlib import Path
import json
HERE=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=str(HERE/'batch.json')
rows=json.loads((HERE/'batch.json').read_text())
def patch(i,replacements):
    p=Path(rows[i]['module']);s=p.read_text()
    for a,b in replacements:
        assert a in s,(i,a);s=s.replace(a,b)
    p.write_text(s)
patch(0,[("(38,13),(35,4),(38,8)","(40,13),(35,4),(40,8)"),("(31,26),(38,17),(34,22)","(31,26),(40,17),(34,22)"),("(17,1),(8,6)","(17,4),(8,6)"),("(30,43),(24,45)","(30,44),(24,44)")])
patch(1,[("circle('fan',16,21,5)","circle('fan',17,21,4)"),("(29,25),(36,25)","(29,25),(35,25)")])
patch(8,[("(16,14),(19,14)","(18,14),(21,14)"),("(16,34),(19,34)","(18,34),(21,34)"),("(19,14),(19,34)","(21,14),(21,34)")])
patch(10,[("(18,9),(24,6),(30,9)","(19,8),(24,6),(29,8)"),("p(12,20)","p(14,18)"),("p(12,40)","p(13,39)"),("(17,20),(24,24),(31,20)","(18,20),(24,24),(30,20)"),("(24,24),(24,30)","(24,24),(24,29)"),("(18,39),(24,42),(30,39)","(19,39),(24,42),(29,39)"),("(24,36),(24,42)","(24,37),(24,42)")])
patch(14,[("('L',(22,22))", "('L',(24,22))"),("join('beam','share')","join('beam','share');join('handle','beam')")])
patch(16,[("path('hilum',(18,26),[('C',(25,19),(18,23),(22,19)),('C',(28,25),(28,19),(30,22)),('C',(19,29),(26,29),(21,32)),('C',(18,26),(18,28),(18,27))]", "path('hilum',(20,28),[('C',(27,21),(20,25),(24,21)),('C',(30,27),(30,21),(32,24)),('C',(21,31),(28,31),(23,34)),('C',(20,28),(20,30),(20,29))]")])

# Split true T-junctions in straight receiving runs while retaining names and contours.
TOPOLOGY='''
        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacements,rebuilt={},[]
        for primitive in self.primitives:
            if isinstance(primitive,Line) and primitive.start!=primitive.end:
                a,b=primitive.start,primitive.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b];names=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{primitive.element_id}-node-{j}';rebuilt.append(Line(name,u,v));names.append(name)
                    replacements[primitive.element_id]=names
                    if not any(primitive.element_id in c.members for c in self.contours):self.add_contour(primitive.element_id,*names)
                    continue
            rebuilt.append(primitive)
        if replacements:
            self.primitives[:]=rebuilt
            self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
'''
for row in rows:
    p=Path(row['module']);p.write_text(p.read_text()+TOPOLOGY)
