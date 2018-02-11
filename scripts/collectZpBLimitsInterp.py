import os

dirs = next(os.walk('.'))[1]

for d in dirs:
        cmd = "combineTool.py -M CollectLimits "+d+ "/cmb/*/*.limit.* -o "+d+".json"
	#print "combineTool.py -M CollectLimits "+d+ "/cmb/*/*.limit.* -o "+d+".json"
        os.system(cmd)

