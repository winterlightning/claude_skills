exec(open('/tmp/meaning2_refine.py').read().split("xs=json.loads")[0])
specs[0]['body']=specs[0]['body'].replace("24,21,8","24,21,9").replace('(24,16)','(24,17)')
specs[4]['body']=specs[4]['body'].replace('(23,31)','(23,32)').replace('(40,31)','(40,32)').replace('(40,23)','(40,24)').replace('(23,23)','(23,24)').replace('(30,23)','(30,24)').replace("('L',(23,16))","('L',(25,16))")
specs[5]['body']=specs[5]['body'].replace('(24,17)','(24,16)').replace('(40,17)','(40,16)').replace('(40,25)','(40,24)').replace('(23,25)','(23,24)').replace('(30,25)','(30,24)').replace('(25,33)','(25,32)').replace('(20,33)','(20,32)').replace('(30,33)','(30,32)').replace('(23,33)','(25,32)')
specs[9]['body']=specs[9]['body'].replace('(24,13)','(24,15)').replace('(24,35)','(24,33)')
specs[13]['body']=specs[13]['body'].replace("self.path('helmet',(12,35),[('C',(6,23),(8,33),(6,29)),('C',(24,8),(6,13),(14,8)),('C',(42,23),(34,8),(42,13)),('C',(36,35),(42,29),(40,33))])", "self.path('shell-left',(12,35),[('C',(6,23),(8,33),(6,29)),('C',(18,9),(6,14),(12,10))])\nself.path('shell-right',(30,9),[('C',(42,23),(36,10),(42,14)),('C',(36,35),(42,29),(40,33))])").replace("self.relate('connect','helmet','face','crest','ear-left','ear-right')", "self.relate('connect','shell-left','face','crest','ear-left');self.relate('connect','shell-right','face','crest','ear-right')")
specs[15]['body']=specs[15]['body'].replace("'planet',(27,16)","'planet',(21,14)").replace("('C',(34,27),(30,42),(38,35))","('C',(33,31),(30,42),(36,36))")
specs[17]['body']='''for n,x,y in [('left',12,19),('right',36,15)]:
 self.path(n+'-body',(x-3,y),[('A',(x+3,y),3,3,True),('L',(x+3,y+9)),('C',(x,y+14),(x+3,y+12),(x+1,y+13)),('C',(x-3,y+9),(x-1,y+13),(x-3,y+12)),('L',(x-3,y))],True)
 self.path(n+'-left-fin',(x-3,y),[('L',(x-9,y-3)),('L',(x-9,y+2)),('C',(x-3,y+6),(x-9,y+5),(x-6,y+6))])
 self.path(n+'-right-fin',(x+3,y),[('L',(x+9,y-3)),('L',(x+9,y+2)),('C',(x+3,y+6),(x+9,y+5),(x+6,y+6))])
 self.relate('connect',n+'-body',n+'-left-fin',n+'-right-fin')
self.add_line('trail-left',(12,8),(12,10));self.add_line('trail-right',(36,4),(36,6))
self.add_bezier('horizon',(4,44),((17,39),(31,39),(44,44)))'''
xs=json.loads((B/'refined.json').read_text())
for i in (0,4,5,9,13,15,17):
 run,module,md=author(i,3);xs[i]=export(run,module,md)
(B/'selected.json').write_text(json.dumps(xs,indent=2))
