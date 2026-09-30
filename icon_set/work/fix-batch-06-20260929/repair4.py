from author import author,ROOT
import json
H='Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap'
s=json.loads((ROOT/'specs3.json').read_text())
code=s['15'].replace("('C',(22,22),(34,21),(27,22)),('C',(16,32),(18,22),(16,26)),('L',(16,40))","('C',(24,22),(34,21),(29,22)),('A',(20,26),4,4,False),('L',(20,28))")
exec(code)
s['15']=code
t=json.loads((ROOT/'specs2.json').read_text())
code=t['16'].replace('18,20,2','18,22,2').replace('30,20,2','30,22,2').replace('(21,31),(27,31)','(22,33),(26,33)')
exec(code)
s['16']=code
(ROOT/'specs4.json').write_text(json.dumps(s,indent=2))
