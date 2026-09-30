from revise4 import *
D['spool-wrapped-with-thread']['code']="""
path('thread-body',(12,8),[('L',(24,8)),('L',(36,8)),('A',(40,12),4,4,True),('L',(40,24)),('L',(40,36)),('A',(36,40),4,4,True),('L',(24,40)),('L',(12,40)),('A',(8,36),4,4,True),('L',(8,32)),('L',(8,16)),('L',(8,12)),('A',(12,8),4,4,True)],True)
line('top-core',(24,4),(24,8));join('top-core','thread-body')
line('bottom-core',(24,40),(24,44));join('bottom-core','thread-body')
poly('wraps',(8,16),(40,24),(8,32));join('wraps','thread-body')
"""
D['spool-wrapped-with-thread']['issue']='The rejected spool has one diagonal slash and an open lower outline. Restore two alternating diagonal thread runs on a complete rounded barrel with projecting axle ends.'
D['spool-wrapped-with-thread']['omissions']='Reduce the projecting core outlines to short axle strokes and omit the loose tail, making room for two clearly separated wraps.'
if __name__=='__main__':generate(sys.argv[1:])
