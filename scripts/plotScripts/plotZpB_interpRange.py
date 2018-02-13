import os
import math
import ROOT
from array import array
import re
import json
import types

#model = "2HDM"
model = "ZpB"

doScaleXS = 1

doFillAvgHigh = 1
doFillAvgLow = 1
doFillAvgRest = 1
doFillAvgAll = 1

doFillFit = 0
doFillFitAll = 0


from CMS_lumi import CMS_lumi
import plotting_interp as plot
ROOT.gROOT.SetBatch(ROOT.kTRUE)
plot.ModTDRStyle()

canv = ROOT.TCanvas('test', 'test')
canv.SetLogz()

def SetMyPalette():
    alpha = 1
    nRGBs = 9
    stops = array(
        'd', [0.0000, 0.1250, 0.2500, 0.3750, 0.5000, 0.6250, 0.7500, 0.8750, 1.0000])
    red = array(
        'd', ([0./255.,  50./255.,  130./255.,  180./255., 200./255.,  215./255., 230./255., 240./255., 255./255.]))
    green = array(
        'd', ([0./255.,  50./255.,  130./255.,  180./255., 200./255.,  215./255., 230./255., 240./255., 255./255.]))
    blue = array(
        'd', ([255./255., 255./255., 255./255., 255./255., 255./255., 255./255., 255./255., 255./255., 255./255.]))
    ROOT.TColor.CreateGradientColorTable(nRGBs, stops, red, green, blue, 255, alpha)

SetMyPalette()
ROOT.gStyle.SetNumberContours(255)
ROOT.gStyle.SetOptStat(0)

A=[]
Z=[]

if model == "2HDM":
    A=[300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675]
    Z=[600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950]
    #A=[300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800,825,850,875,900,925,950,975]

elif model == "ZpB":
    A=[1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
    #A=[1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 125, 150, 175, 200]
    Z=[10, 20, 30, 40, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800,1900, 2000]
    #Z=[10, 20, 30, 40, 50, 75, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]

BinningA = [0.0]
BinningZ = [0.0]

for i in range(0, len(A)-1):
    BinningA.append( (A[i] + A[i+1])/2.0)
BinningA.append((A[-1] + A[-1] - ((A[-1] + A[-2])/2.0)))
for i in range(0, len(Z)-1):
    BinningZ.append( (Z[i] + Z[i+1])/2.0)
BinningZ.append((Z[-1] + Z[-1] - ((Z[-1] + Z[-2])/2.0)))

#print BinningA
#print BinningZ


limitPlot = ROOT.TH2F("lplot","lplot",len(Z),array('d',BinningZ),len(A),array('d',BinningA))
limitPlotObs = ROOT.TH2F("lplotObs","lplotObs",len(Z),array('d',BinningZ),len(A),array('d',BinningA))
limitPlotUp = ROOT.TH2F("lplotU","lplotU",len(Z),array('d',BinningZ),len(A),array('d',BinningA))
limitPlotDown = ROOT.TH2F("lplotDown","lplotDown",len(Z),array('d',BinningZ),len(A),array('d',BinningA))
limitPlotUp2 = ROOT.TH2F("lplotU2","lplotU2",len(Z),array('d',BinningZ),len(A),array('d',BinningA))
limitPlotDown2 = ROOT.TH2F("lplotDown2","lplotDown2",len(Z),array('d',BinningZ),len(A),array('d',BinningA))

limDir = ""
limitPlotObs.GetXaxis().SetTitle("M_{Z'} [GeV]")
if model =="2HDM":
    limitPlotObs.GetYaxis().SetTitle("M_{A} [GeV]")
    limDir = "Zprime"
if model =="ZpB":
    limitPlotObs.GetYaxis().SetTitle("M_{#chi} [GeV]")
    limDir = "Baryonic"

def scaleXS(Z,A):
    xsFile = ""
    if model == "2HDM":
        xsFile = "xtt_monoH.txt" 
    if model =="ZpB":
        xsFile = "xtt_monoH_ZpB.txt"
    xsRef = open(xsFile)
    returnString = "99999"
    for line in xsRef:
        if (str(line.split(' ')[0]) == str(Z) and str(line.split(' ')[1]) == str(A)):
            returnString = str(1./float(line.split(' ')[2]))
            ##print returnString
    return returnString


for a in A:
    for z in Z:
        data = {}
        filename= limDir+str(z)+'A'+str(a)+'.json'
        ##print 'Using filename ' 
        ##print filename
        scale = 1.
        if doScaleXS:
            scale = scaleXS(z,a)
        if os.path.isfile(filename) and scale != "99999":
           ##print scale
           with open(filename) as jsonfile:
              data = json.load(jsonfile)
              for key in data:
                  limitPlot.SetBinContent(limitPlot.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'exp0'])
                  limitPlotUp.SetBinContent(limitPlotUp.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'exp+1'])
                  limitPlotDown.SetBinContent(limitPlotDown.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'exp-1'])
                  limitPlotUp2.SetBinContent(limitPlotUp2.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'exp+2'])
                  limitPlotDown2.SetBinContent(limitPlotDown2.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'exp-2'])
                  limitPlotObs.SetBinContent(limitPlotObs.GetXaxis().FindBin(float(z)),limitPlot.GetYaxis().FindBin(float(a)),float(scale)*data[key][u'obs'])
        #if "00" in str(Z[d]):
        #    limitPlotObs.GetXaxis().SetBinLabel(j,str(Z[d]))
        #if "00" in str(A[c]) or "50" in str(A[c]):
        #    limitPlotObs.GetYaxis().SetBinLabel(i,str(A[c]))


# do averaging for below line
if doFillAvgLow:
    for j in range(1,limitPlotObs.GetNbinsX()+1):
        for i in range (1,limitPlotObs.GetNbinsY()+1):
            aVal = A[i-1]
            zVal = Z[j-1]
            binVal = str(limitPlotObs.GetBinContent(j,i))
            #print "i: {0}   A: {1}   j: {2}   Z: {3}  Limit: {4}   ".format(i,aVal,j,zVal,str(limitPlotObs.GetBinContent(j,i)))
            if binVal == "0.0" and 2*float(aVal) < float(zVal):
            #if binVal == "0.0":
                #print " OBSERVED back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotObs.GetBinContent(j-1,i)),str(limitPlotObs.GetBinContent(j+1,i)),str(limitPlotObs.GetBinContent(j,i-1)),str(limitPlotObs.GetBinContent(j,i+1)))
                avg = 0.0
                div = 0.0
                back = limitPlotObs.GetBinContent(j-1,i)
                if back != 0.0 and back < 50.:
                    avg += back
                    div += 1
                forward = limitPlotObs.GetBinContent(j+1,i)
                if forward != 0.0 and forward < 50.:
                    avg += forward
                    div += 1
                down = limitPlotObs.GetBinContent(j,i-1)
                if down != 0.0 and down < 50.:
                    avg += down
                    div += 1
                up = limitPlotObs.GetBinContent(j,i+1)
                if up != 0.0 and up < 50.:
                    avg += up
                    div += 1
                if div !=0:
                    avg = avg/div
                    #print "avg: " + str(avg)
                    limitPlotObs.SetBinContent(j,i,avg)
                    
                
                if doFillAvgAll:
                    #print " EXP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlot.GetBinContent(j-1,i)),str(limitPlot.GetBinContent(j+1,i)),str(limitPlot.GetBinContent(j,i-1)),str(limitPlot.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlot.GetBinContent(j-1,i)
                    if back != 0.0 and back < 50.:
                        avg += back
                        div += 1
                    forward = limitPlot.GetBinContent(j+1,i)
                    if forward != 0.0 and forward < 50.:
                        avg += forward
                        div += 1
                    down = limitPlot.GetBinContent(j,i-1)
                    if down != 0.0 and down < 50.:
                        avg += down
                        div += 1
                    up = limitPlot.GetBinContent(j,i+1)
                    if up != 0.0 and up < 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlot.SetBinContent(j,i,avg)
                    
                    #print " EXP UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp.GetBinContent(j-1,i)),str(limitPlotUp.GetBinContent(j+1,i)),str(limitPlotUp.GetBinContent(j,i-1)),str(limitPlotUp.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp.GetBinContent(j-1,i)
                    if back != 0.0 and back < 50.:
                        avg += back
                        div += 1
                    forward = limitPlotUp.GetBinContent(j+1,i)
                    if forward != 0.0 and forward < 50.:
                        avg += forward
                        div += 1
                    down = limitPlotUp.GetBinContent(j,i-1)
                    if down != 0.0 and down < 50.:
                        avg += down
                        div += 1
                    up = limitPlotUp.GetBinContent(j,i+1)
                    if up != 0.0 and up < 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotUp.SetBinContent(j,i,avg)
                    
                    #print " EXP DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown.GetBinContent(j-1,i)),str(limitPlotDown.GetBinContent(j+1,i)),str(limitPlotDown.GetBinContent(j,i-1)),str(limitPlotDown.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown.GetBinContent(j-1,i)
                    if back != 0.0 and back < 50.:
                        avg += back
                        div += 1
                    forward = limitPlotDown.GetBinContent(j+1,i)
                    if forward != 0.0 and forward < 50.:
                        avg += forward
                        div += 1
                    down = limitPlotDown.GetBinContent(j,i-1)
                    if down != 0.0 and down < 50.:
                        avg += down
                        div += 1
                    up = limitPlotDown.GetBinContent(j,i+1)
                    if up != 0.0 and up < 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotDown.SetBinContent(j,i,avg)
                    
                    #print " EXP 2 UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp2.GetBinContent(j-1,i)),str(limitPlotUp2.GetBinContent(j+1,i)),str(limitPlotUp2.GetBinContent(j,i-1)),str(limitPlotUp2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp2.GetBinContent(j-1,i)
                    if back != 0.0 and back < 50.:
                        avg += back
                        div += 1
                    forward = limitPlotUp2.GetBinContent(j+1,i)
                    if forward != 0.0 and forward < 50.:
                        avg += forward
                        div += 1
                    down = limitPlotUp2.GetBinContent(j,i-1)
                    if down != 0.0 and down < 50.:
                        avg += down
                        div += 1
                    up = limitPlotUp2.GetBinContent(j,i+1)
                    if up != 0.0 and up < 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotUp2.SetBinContent(j,i,avg)
                    
                    #print " EXP 2 DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown2.GetBinContent(j-1,i)),str(limitPlotDown2.GetBinContent(j+1,i)),str(limitPlotDown2.GetBinContent(j,i-1)),str(limitPlotDown2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown2.GetBinContent(j-1,i)
                    if back != 0.0 and back < 50.:
                        avg += back
                        div += 1
                    forward = limitPlotDown2.GetBinContent(j+1,i)
                    if forward != 0.0 and forward < 50.:
                        avg += forward
                        div += 1
                    down = limitPlotDown2.GetBinContent(j,i-1)
                    if down != 0.0 and down < 50.:
                        avg += down
                        div += 1
                    up = limitPlotDown2.GetBinContent(j,i+1)
                    if up != 0.0 and up < 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotDown2.SetBinContent(j,i,avg)


# above line
if doFillAvgHigh:
    for j in range (1,limitPlotObs.GetNbinsX()+1):
        for i in  reversed(range(1,limitPlotObs.GetNbinsY()+1)):
            aVal = A[i-1]
            zVal = Z[j-1]
            binVal = str(limitPlotObs.GetBinContent(j,i))
            #print "i: {0}   A: {1}   j: {2}   Z: {3}  Limit: {4}   ".format(i,aVal,j,zVal,str(limitPlotObs.GetBinContent(j,i)))
            if binVal == "0.0" and 2*float(aVal) > float(zVal):
                #print " OBSERVED back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotObs.GetBinContent(j-1,i)),str(limitPlotObs.GetBinContent(j+1,i)),str(limitPlotObs.GetBinContent(j,i-1)),str(limitPlotObs.GetBinContent(j,i+1)))
                avg = 0.0
                div = 0.0
                back = limitPlotObs.GetBinContent(j-1,i)
                if  back != 0.0 and  back > 50.:
                    avg += back
                    div += 1
                forward = limitPlotObs.GetBinContent(j+1,i)
                if forward != 0.0 and forward > 50.:
                    avg += forward
                    div += 1
                down = limitPlotObs.GetBinContent(j,i-1)
                if down != 0.0 and down > 50.:
                    avg += down
                    div += 1
                up = limitPlotObs.GetBinContent(j,i+1)
                if up != 0.0 and up > 50.:
                    avg += up
                    div += 1
                if div !=0:
                    avg = avg/div
                    #print "avg: " + str(avg)
                    limitPlotObs.SetBinContent(j,i,avg)
                    
                
                if doFillAvgAll:
                    #print " EXP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlot.GetBinContent(j-1,i)),str(limitPlot.GetBinContent(j+1,i)),str(limitPlot.GetBinContent(j,i-1)),str(limitPlot.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlot.GetBinContent(j-1,i)
                    if back != 0.0 and back > 50.:
                        avg += back
                        div += 1
                    forward = limitPlot.GetBinContent(j+1,i)
                    if forward != 0.0 and forward > 50.:
                        avg += forward
                        div += 1
                    down = limitPlot.GetBinContent(j,i-1)
                    if down != 0.0 and down > 50.:
                        avg += down
                        div += 1
                    up = limitPlot.GetBinContent(j,i+1)
                    if up != 0.0 and up > 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlot.SetBinContent(j,i,avg)
                    
                    #print " EXP UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp.GetBinContent(j-1,i)),str(limitPlotUp.GetBinContent(j+1,i)),str(limitPlotUp.GetBinContent(j,i-1)),str(limitPlotUp.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp.GetBinContent(j-1,i)
                    if back != 0.0 and back > 50.:
                        avg += back
                        div += 1
                    forward = limitPlotUp.GetBinContent(j+1,i)
                    if forward != 0.0 and forward > 50.:
                        avg += forward
                        div += 1
                    down = limitPlotUp.GetBinContent(j,i-1)
                    if down != 0.0 and down > 50.:
                        avg += down
                        div += 1
                    up = limitPlotUp.GetBinContent(j,i+1)
                    if up != 0.0 and up > 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotUp.SetBinContent(j,i,avg)
                    
                    #print " EXP DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown.GetBinContent(j-1,i)),str(limitPlotDown.GetBinContent(j+1,i)),str(limitPlotDown.GetBinContent(j,i-1)),str(limitPlotDown.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown.GetBinContent(j-1,i)
                    if back != 0.0 and back > 50.:
                        avg += back
                        div += 1
                    forward = limitPlotDown.GetBinContent(j+1,i)
                    if forward != 0.0 and forward > 50.:
                        avg += forward
                        div += 1
                    down = limitPlotDown.GetBinContent(j,i-1)
                    if down != 0.0 and down > 50.:
                        avg += down
                        div += 1
                    up = limitPlotDown.GetBinContent(j,i+1)
                    if up != 0.0 and up > 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotDown.SetBinContent(j,i,avg)
                    
                    #print " EXP 2 UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp2.GetBinContent(j-1,i)),str(limitPlotUp2.GetBinContent(j+1,i)),str(limitPlotUp2.GetBinContent(j,i-1)),str(limitPlotUp2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp2.GetBinContent(j-1,i)
                    if back != 0.0 and back > 50.:
                        avg += back
                        div += 1
                    forward = limitPlotUp2.GetBinContent(j+1,i)
                    if forward != 0.0 and forward > 50.:
                        avg += forward
                        div += 1
                    down = limitPlotUp2.GetBinContent(j,i-1)
                    if down != 0.0 and down > 50.:
                        avg += down
                        div += 1
                    up = limitPlotUp2.GetBinContent(j,i+1)
                    if up != 0.0 and up > 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotUp2.SetBinContent(j,i,avg)
                    
                    #print " EXP 2 DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown2.GetBinContent(j-1,i)),str(limitPlotDown2.GetBinContent(j+1,i)),str(limitPlotDown2.GetBinContent(j,i-1)),str(limitPlotDown2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown2.GetBinContent(j-1,i)
                    if back != 0.0 and back > 50.:
                        avg += back
                        div += 1
                    forward = limitPlotDown2.GetBinContent(j+1,i)
                    if forward != 0.0 and forward > 50.:
                        avg += forward
                        div += 1
                    down = limitPlotDown2.GetBinContent(j,i-1)
                    if down != 0.0 and down > 50.:
                        avg += down
                        div += 1
                    up = limitPlotDown2.GetBinContent(j,i+1)
                    if up != 0.0 and up > 50.:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        #print "avg: " + str(avg)
                        limitPlotDown2.SetBinContent(j,i,avg)

# at line
if doFillAvgRest:
    for i in range (1,limitPlotObs.GetNbinsY()+1):
        for j in range (1,limitPlotObs.GetNbinsX()+1):
            aVal = A[i-1]
            zVal = Z[j-1]
            binVal = str(limitPlotObs.GetBinContent(j,i))
            print "i: {0}   A: {1}   j: {2}   Z: {3}  Limit: {4}   ".format(i,aVal,j,zVal,str(limitPlotObs.GetBinContent(j,i)))
            if binVal == "0.0":
                print " OBSERVED back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotObs.GetBinContent(j-1,i)),str(limitPlotObs.GetBinContent(j+1,i)),str(limitPlotObs.GetBinContent(j,i-1)),str(limitPlotObs.GetBinContent(j,i+1)))
                avg = 0.0
                div = 0.0
                back = limitPlotObs.GetBinContent(j-1,i)
                if back != 0.0:
                    avg += back
                    div += 1
                forward = limitPlotObs.GetBinContent(j+1,i)
                if forward != 0.0:
                    avg += forward
                    div += 1
                down = limitPlotObs.GetBinContent(j,i-1)
                if down != 0.0:
                    avg += down
                    div += 1
                up = limitPlotObs.GetBinContent(j,i+1)
                if up != 0.0:
                    avg += up
                    div += 1
                if div !=0:
                    avg = avg/div
                    print "avg: " + str(avg)
                    limitPlotObs.SetBinContent(j,i,avg)
                    
                
                if doFillAvgAll:
                    print " EXP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlot.GetBinContent(j-1,i)),str(limitPlot.GetBinContent(j+1,i)),str(limitPlot.GetBinContent(j,i-1)),str(limitPlot.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlot.GetBinContent(j-1,i)
                    if back != 0.0:
                        avg += back
                        div += 1
                    forward = limitPlot.GetBinContent(j+1,i)
                    if forward != 0.0:
                        avg += forward
                        div += 1
                    down = limitPlot.GetBinContent(j,i-1)
                    if down != 0.0:
                        avg += down
                        div += 1
                    up = limitPlot.GetBinContent(j,i+1)
                    if up != 0.0:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        print "avg: " + str(avg)
                        limitPlot.SetBinContent(j,i,avg)
                    
                    print " EXP UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp.GetBinContent(j-1,i)),str(limitPlotUp.GetBinContent(j+1,i)),str(limitPlotUp.GetBinContent(j,i-1)),str(limitPlotUp.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp.GetBinContent(j-1,i)
                    if back != 0.0:
                        avg += back
                        div += 1
                    forward = limitPlotUp.GetBinContent(j+1,i)
                    if forward != 0.0:
                        avg += forward
                        div += 1
                    down = limitPlotUp.GetBinContent(j,i-1)
                    if down != 0.0:
                        avg += down
                        div += 1
                    up = limitPlotUp.GetBinContent(j,i+1)
                    if up != 0.0:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        print "avg: " + str(avg)
                        limitPlotUp.SetBinContent(j,i,avg)
                    
                    print " EXP DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown.GetBinContent(j-1,i)),str(limitPlotDown.GetBinContent(j+1,i)),str(limitPlotDown.GetBinContent(j,i-1)),str(limitPlotDown.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown.GetBinContent(j-1,i)
                    if back != 0.0:
                        avg += back
                        div += 1
                    forward = limitPlotDown.GetBinContent(j+1,i)
                    if forward != 0.0:
                        avg += forward
                        div += 1
                    down = limitPlotDown.GetBinContent(j,i-1)
                    if down != 0.0:
                        avg += down
                        div += 1
                    up = limitPlotDown.GetBinContent(j,i+1)
                    if up != 0.0:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        print "avg: " + str(avg)
                        limitPlotDown.SetBinContent(j,i,avg)
                    
                    print " EXP 2 UP back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotUp2.GetBinContent(j-1,i)),str(limitPlotUp2.GetBinContent(j+1,i)),str(limitPlotUp2.GetBinContent(j,i-1)),str(limitPlotUp2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotUp2.GetBinContent(j-1,i)
                    if back != 0.0:
                        avg += back
                        div += 1
                    forward = limitPlotUp2.GetBinContent(j+1,i)
                    if forward != 0.0:
                        avg += forward
                        div += 1
                    down = limitPlotUp2.GetBinContent(j,i-1)
                    if down != 0.0:
                        avg += down
                        div += 1
                    up = limitPlotUp2.GetBinContent(j,i+1)
                    if up != 0.0:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        print "avg: " + str(avg)
                        limitPlotUp2.SetBinContent(j,i,avg)
                    
                    print " EXP 2 DOWN back: {0}   forward: {1}   down: {2}   up: {3}   ".format(str(limitPlotDown2.GetBinContent(j-1,i)),str(limitPlotDown2.GetBinContent(j+1,i)),str(limitPlotDown2.GetBinContent(j,i-1)),str(limitPlotDown2.GetBinContent(j,i+1)))
                    avg = 0.0
                    div = 0.0
                    back = limitPlotDown2.GetBinContent(j-1,i)
                    if back != 0.0:
                        avg += back
                        div += 1
                    forward = limitPlotDown2.GetBinContent(j+1,i)
                    if forward != 0.0:
                        avg += forward
                        div += 1
                    down = limitPlotDown2.GetBinContent(j,i-1)
                    if down != 0.0:
                        avg += down
                        div += 1
                    up = limitPlotDown2.GetBinContent(j,i+1)
                    if up != 0.0:
                        avg += up
                        div += 1
                    if div !=0:
                        avg = avg/div
                        print "avg: " + str(avg)
                        limitPlotDown2.SetBinContent(j,i,avg)



limitPlotObs.GetZaxis().SetRangeUser(.3,70000000)
limitPlotObs.SetBarOffset(0.10)
limitPlotObs.Draw("COLZ")

limitPlotUp2.SetMinimum(1);
limitPlotUp2.SetContour(1);
limitPlotUp2.SetLineWidth(2);
limitPlotUp2.SetLineColor(5);
#limitPlotUp2.Draw("CONT3 SAME")

limitPlotDown2.SetMinimum(1);
limitPlotDown2.SetContour(1);
limitPlotDown2.SetLineWidth(2);
limitPlotDown2.SetLineColor(5);
#limitPlotDown2.Draw("CONT3 SAME")

limitPlotUp.SetMinimum(1);
limitPlotUp.SetContour(1);
limitPlotUp.SetLineWidth(2);
limitPlotUp.SetLineColor(8);
limitPlotUp.Draw("CONT3 SAME")

limitPlotDown.SetMinimum(1);
limitPlotDown.SetContour(1);
limitPlotDown.SetLineWidth(2);
limitPlotDown.SetLineColor(8);
limitPlotDown.Draw("CONT3 SAME")

limitPlotObsCopy = limitPlotObs.Clone()
limitPlotObsCopy.SetMinimum(1);
limitPlotObsCopy.SetContour(1);
limitPlotObsCopy.SetLineWidth(2);
limitPlotObsCopy.Draw("CONT3 SAME")

limitPlot.SetMinimum(1);
limitPlot.SetContour(1);
limitPlot.SetLineStyle(2);
limitPlot.SetLineWidth(3);
limitPlot.Draw("CONT3 SAME")

leg = ROOT.TLegend(.35,.65,.90,.90)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.030)
leg.AddEntry(limitPlotObsCopy,"Observed Limit (95% CL)","L")
leg.AddEntry(limitPlot,"Expected Limit (95% CL)","L")
leg.AddEntry(limitPlotUp,"Expected Limit #pm1 #sigma","L")
#leg.AddEntry(limitPlotUp,"Expected Limit +/- 1 \sigma","L")
leg.Draw()

#leg.AddEntry(limitPlotUp2,"Expected Limit +/- 2\sigma r = 1 (95% CL)","L")
#leg.Draw()

CMS_lumi(canv,4,0)
canv.Draw()
canv.Print("test.pdf")
limitPlot.SaveAs("test.root")

