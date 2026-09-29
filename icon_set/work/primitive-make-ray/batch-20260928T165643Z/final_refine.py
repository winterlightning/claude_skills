from author_batch import *
records=json.loads((Path(__file__).parent/'refined-runs.json').read_text())
for n in [4,6,7,15]:
    module=ROOT/records[n-1]['module']
    code=module.read_text().split('    def build(self):\n',1)[1]
    SPECS[n]['code']=textwrap.dedent(code)
    SPECS[n].update({k:v for k,v in records[n-1]['spec'].items() if k in SPECS[n] and k!='code'})
SPECS[4]['code']=SPECS[4]['code'].replace("'spoon-bowl',(30,19)","'spoon-bowl',(32,18)").replace("(26,15),(31,6)","(28,14),(32,6)").replace("('C',(30,19),(42,17),(34,23))","('C',(32,18),(42,17),(36,22))").replace('(25,25),(30,19)','(25,25),(32,18)')
SPECS[6]['code']=SPECS[6]['code'].replace("'halo',(26,4)","'halo',(26,6)").replace("('A',(42,4),8,2,True)","('A',(42,6),8,2,True)").replace("'wing',(22,15)","'wing',(20,14)")
SPECS[7]['code']=SPECS[7]['code'].replace("'head',24,20,3","'head',24,20,4").replace("# user.svg: head bottom23, shoulders top31 = exact 4 ink gap.","# user.svg: head bottom24, shoulders top32 = exact 4 ink gap.").replace("'shoulders',(20,33),[('A',(24,31),4,2,True),('A',(28,33),4,2,True)]","'shoulders',(18,35),[('A',(24,32),6,3,True),('A',(30,35),6,3,True)]")
SPECS[15]['code']=SPECS[15]['code'].replace('(18,22)','(19,22)')
for n in [4,6,7,15]:records[n-1]=author(n,'r2' if n==4 else 'r3')
(Path(__file__).parent/'final-runs.json').write_text(json.dumps(records,indent=2))
