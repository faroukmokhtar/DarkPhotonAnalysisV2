import ROOT
import os,sys
from ROOT import TGraphAsymmErrors
from ROOT import TGraphErrors
from ROOT import TColor
#from ROOT import TGraph
from array import array
from ROOT import *
from operator import truediv
import random
import math
import glob



fileEff=ROOT.TFile.Open("/afs/cern.ch/user/j/jsalfeld/public/DarkPhotonInput/DPAcceptancesEfficiencies.root")


dpxsec=array('d',[484.3,292.8,193.6,98.95,57.97,43.98,37.16,31.69,25.39,18.26,13.66,10.59])
#dpxsec=array('d',[484.3,292.8,193.6,98.95,57.97,43.98,37.16,31.69,25.39,18.26,13.66,10.59])
dpm=array('d',[10,12.5,15,20,25,28,30,32,35,40,45,50])
gdpxsec=TGraph(len(dpxsec),dpm,dpxsec)

d_list   = [40, 188, 231, 301, 341, 357]
Lxy_list = ["2", "2.2", "2.4", "2.6", "2.8", "3", "10"]

limit40  = array('d')
limit188 = array('d')
limit231 = array('d')
limit301 = array('d')
limit341 = array('d')
limit357 = array('d')

limit40_Observed  = array('d')
limit188_Observed = array('d')
limit231_Observed = array('d')
limit301_Observed = array('d')
limit341_Observed = array('d')
limit357_Observed = array('d')

limit40_68up  = array('d')
limit188_68up = array('d')
limit231_68up = array('d')
limit301_68up = array('d')
limit341_68up = array('d')
limit357_68up = array('d')

limit40_68down  = array('d')
limit188_68down = array('d')
limit231_68down = array('d')
limit301_68down = array('d')
limit341_68down = array('d')
limit357_68down = array('d')

limit40_95up  = array('d')
limit188_95up = array('d')
limit231_95up = array('d')
limit301_95up = array('d')
limit341_95up = array('d')
limit357_95up = array('d')

limit40_95down  = array('d')
limit188_95down = array('d')
limit231_95down = array('d')
limit301_95down = array('d')
limit341_95down = array('d')
limit357_95down = array('d')

Lxy  = array('d', [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 10.0])
Lerr = array('d', [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
mass = array('d', [0.3, 1.3, 2., 4., 6., 7.])

xsec=1.#pb

#some counters
m=0.2
t=0
#make the loop
a=1.

# d = 40
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_40.AsymptoticLimits.mH*.root")
        print file[0]	
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit40.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit40_95up.append(abs(tree.limit*a-limit40[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit40_95down.append(abs(tree.limit*a-limit40[-1]))
        tree.GetEntry(1)
        limit40_68up.append(abs(tree.limit*a-limit40[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit40_68down.append(abs(tree.limit*a-limit40[-1]))
        tree.GetEntry(5)
        limit40_Observed.append(tree.limit*a)
		
# d = 188
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_188.AsymptoticLimits.mH*.root")
        print file[0]
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit188.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit188_95up.append(abs(tree.limit*a-limit188[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit188_95down.append(abs(tree.limit*a-limit188[-1]))
        tree.GetEntry(1)
        limit188_68up.append(abs(tree.limit*a-limit188[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit188_68down.append(abs(tree.limit*a-limit188[-1]))
        tree.GetEntry(5)
        limit188_Observed.append(tree.limit*a)

# d = 231
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_231.AsymptoticLimits.mH*.root")
        print file[0]
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit231.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit231_95up.append(abs(tree.limit*a-limit231[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit231_95down.append(abs(tree.limit*a-limit231[-1]))
        tree.GetEntry(1)
        limit231_68up.append(abs(tree.limit*a-limit231[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit231_68down.append(abs(tree.limit*a-limit231[-1]))
        tree.GetEntry(5)
        limit231_Observed.append(tree.limit*a)

# d = 301
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_301.AsymptoticLimits.mH*.root")
        print file[0]
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit301.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit301_95up.append(abs(tree.limit*a-limit301[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit301_95down.append(abs(tree.limit*a-limit301[-1]))
        tree.GetEntry(1)
        limit301_68up.append(abs(tree.limit*a-limit301[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit301_68down.append(abs(tree.limit*a-limit301[-1]))
        tree.GetEntry(5)
        limit301_Observed.append(tree.limit*a)

# d = 341
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_341.AsymptoticLimits.mH*.root")
        print file[0]
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit341.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit341_95up.append(abs(tree.limit*a-limit341[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit341_95down.append(abs(tree.limit*a-limit341[-1]))
        tree.GetEntry(1)
        limit341_68up.append(abs(tree.limit*a-limit341[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit341_68down.append(abs(tree.limit*a-limit341[-1]))
        tree.GetEntry(5)
        limit341_Observed.append(tree.limit*a)

# d = 357
for L in Lxy_list:
        file=glob.glob("output/Lxy"+L+"_ALL/higgsCombineasympMassIndex_357.AsymptoticLimits.mH*.root")
        print file[0]
        f=ROOT.TFile.Open(file[0])
        tree=f.Get("limit")
        tree.GetEntry(2)
        limit357.append(tree.limit*a)
        tree=f.Get("limit")
        tree.GetEntry(0)
        limit357_95up.append(abs(tree.limit*a-limit357[-1]))
        tree=f.Get("limit")
        tree.GetEntry(4)
        limit357_95down.append(abs(tree.limit*a-limit357[-1]))
        tree.GetEntry(1)
        limit357_68up.append(abs(tree.limit*a-limit357[-1]))
        tree=f.Get("limit")
        tree.GetEntry(3)
        limit357_68down.append(abs(tree.limit*a-limit357[-1]))
        tree.GetEntry(5)
        limit357_Observed.append(tree.limit*a)



#####
c1=ROOT.TCanvas("c1","c1",700,500)
#c1.SetGrid()
c1.SetLogy()
#c1.SetLogx()

mg=ROOT.TMultiGraph()
mgeps=ROOT.TMultiGraph()

graph_limit40=ROOT.TGraph(len(Lxy),Lxy,limit40)
graph_limit40.SetTitle("graph_limit40")
graph_limit40.SetMarkerSize(0.8)
graph_limit40.SetMarkerStyle(20)
graph_limit40.SetMarkerColor(kBlack)
graph_limit40.SetLineWidth(1)
graph_limit40.SetLineStyle(7)
graph_limit40.GetYaxis().SetRangeUser(0.0001,1)
graph_limit40.GetXaxis().SetRangeUser(0,10)
graph_limit40.GetYaxis().SetTitle("#sigma(pp#rightarrow A)#times BR(A#rightarrow #mu#mu)[pb]")
graph_limit40.GetYaxis().SetTitleSize(2)
graph_limit40.GetXaxis().SetTitle("#mu#mu Mass [GeV]")

graph_limit188=ROOT.TGraph(len(Lxy),Lxy,limit188)
graph_limit188.SetTitle("graph_limit188")
graph_limit188.SetMarkerSize(0.8)
graph_limit188.SetMarkerStyle(20)
graph_limit188.SetMarkerColor(kBlack)
graph_limit188.SetLineWidth(1)
graph_limit188.SetLineStyle(7)

graph_limit231=ROOT.TGraph(len(Lxy),Lxy,limit231)
graph_limit231.SetTitle("graph_limit231")
graph_limit231.SetMarkerSize(0.8)
graph_limit231.SetMarkerStyle(20)
graph_limit231.SetMarkerColor(kBlack)
graph_limit231.SetLineWidth(1)
graph_limit231.SetLineStyle(7)

graph_limit301=ROOT.TGraph(len(Lxy),Lxy,limit301)
graph_limit301.SetTitle("graph_limit301")
graph_limit301.SetMarkerSize(0.8)
graph_limit301.SetMarkerStyle(20)
graph_limit301.SetMarkerColor(kBlack)
graph_limit301.SetLineWidth(1)
graph_limit301.SetLineStyle(7)

graph_limit341=ROOT.TGraph(len(Lxy),Lxy,limit341)
graph_limit341.SetTitle("graph_limit341")
graph_limit341.SetMarkerSize(0.8)
graph_limit341.SetMarkerStyle(20)
graph_limit341.SetMarkerColor(kBlack)
graph_limit341.SetLineWidth(1)
graph_limit341.SetLineStyle(7)

graph_limit357=ROOT.TGraph(len(Lxy),Lxy,limit357)
graph_limit357.SetTitle("graph_limit357")
graph_limit357.SetMarkerSize(0.8)
graph_limit357.SetMarkerStyle(20)
graph_limit357.SetMarkerColor(kBlack)
graph_limit357.SetLineWidth(1)
graph_limit357.SetLineStyle(7)

graph_limit40_obs =ROOT.TGraph(len(Lxy),Lxy,limit40_Observed)
graph_limit188_obs=ROOT.TGraph(len(Lxy),Lxy,limit188_Observed)
graph_limit231_obs=ROOT.TGraph(len(Lxy),Lxy,limit231_Observed)
graph_limit301_obs=ROOT.TGraph(len(Lxy),Lxy,limit301_Observed)
graph_limit341_obs=ROOT.TGraph(len(Lxy),Lxy,limit341_Observed)
graph_limit357_obs=ROOT.TGraph(len(Lxy),Lxy,limit357_Observed)


"""
graph_limit40_95up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit40, Lerr,Lerr,limit40_95up,limit40_95down)
graph_limit40_95up.SetTitle("graph_limit40_95up")
graph_limit40_95up.SetFillColor(ROOT.TColor.GetColor(252,241,15))

graph_limit40_95down=ROOT.TGraph(len(Lxy),Lxy,limit40_95down)
graph_limit40_95down.SetTitle("graph_limit40_95down")
graph_limit40_95down.SetMarkerSize(1)
graph_limit40_95down.SetMarkerStyle(23)
graph_limit40_95down.SetMarkerColor(kYellow)
"""
graph_limit40_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit40,Lerr,Lerr,limit40_68up,limit40_68down)
graph_limit40_68up.SetTitle("graph_limit40_68up")
graph_limit40_68up.SetFillColor(41);
graph_limit40_68up.SetMarkerColor(41)

graph_limit188_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit188,Lerr,Lerr,limit188_68up,limit188_68down)
graph_limit188_68up.SetTitle("graph_limit188_68up")
graph_limit188_68up.SetFillColor(42);
graph_limit188_68up.SetMarkerColor(42)

graph_limit231_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit231,Lerr,Lerr,limit231_68up,limit231_68down)
graph_limit231_68up.SetTitle("graph_limit231_68up")
graph_limit231_68up.SetFillColor(43);
graph_limit231_68up.SetMarkerColor(43)

graph_limit301_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit301,Lerr,Lerr,limit301_68up,limit301_68down)
graph_limit301_68up.SetTitle("graph_limit301_68up")
graph_limit301_68up.SetFillColor(44);
graph_limit301_68up.SetMarkerColor(44)

graph_limit341_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit341,Lerr,Lerr,limit341_68up,limit341_68down)
graph_limit341_68up.SetTitle("graph_limit341_68up")
graph_limit341_68up.SetFillColor(45);
graph_limit341_68up.SetMarkerColor(45)

graph_limit357_68up=ROOT.TGraphAsymmErrors(len(Lxy),Lxy,limit357,Lerr,Lerr,limit357_68up,limit357_68down)
graph_limit357_68up.SetTitle("graph_limit357_68up")
graph_limit357_68up.SetFillColor(46);
graph_limit357_68up.SetMarkerColor(46)
"""
graph_limit40_68down=ROOT.TGraph(len(Lxy),Lxy,limit40_68down)
graph_limit40_68down.SetTitle("graph_limit68down")
graph_limit40_68down.SetMarkerSize(1)
graph_limit40_68down.SetMarkerStyle(22)
graph_limit40_68down.SetMarkerColor(kGreen)
"""

#mg.Add(graph_limit40_95up,"3")
mg.Add(graph_limit40_68up,"3")
mg.Add(graph_limit188_68up,"3")
mg.Add(graph_limit231_68up,"3")
mg.Add(graph_limit301_68up,"3")
mg.Add(graph_limit341_68up,"3")
mg.Add(graph_limit357_68up,"3")

mg.Add(graph_limit40,"pl")
mg.Add(graph_limit188,"pl")
mg.Add(graph_limit231,"pl")
mg.Add(graph_limit301,"pl")
mg.Add(graph_limit341,"pl")
mg.Add(graph_limit357,"pl")

mg.Draw("APC")

mg.GetXaxis().SetRangeUser(0., 11.)
mg.GetYaxis().SetRangeUser(0.001,0.1)

mg.GetYaxis().SetTitle("#sigma(pp#rightarrow A)#times BR(A#rightarrow #mu#mu)#times Acc. [pb]")
mg.GetYaxis().SetTitleSize(0.05)
mg.GetXaxis().SetTitle("Lxy [cm]")
mg.GetXaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleOffset(0.8)

c1.Update()
legend=ROOT.TLegend(0.5,0.6,0.8,0.9)
cmsTag=ROOT.TLatex(0.13,0.917,"#scale[1.1]{CMS}")
cmsTag.SetNDC()
cmsTag.SetTextAlign(11)
cmsTag.Draw()
cmsTag2=ROOT.TLatex(0.215,0.917,"#scale[0.825]{#bf{#it{Preliminary}}}")
cmsTag2.SetNDC()
cmsTag2.SetTextAlign(11)
#cmsTag.SetTextFont(61)
cmsTag2.Draw()
cmsTag3=ROOT.TLatex(0.90,0.917,"#scale[0.9]{#bf{61.3 fb^{-1} (13 TeV, 2018)}}")
cmsTag3.SetNDC()
cmsTag3.SetTextAlign(31)
#cmsTag.SetTextFont(61)
cmsTag3.Draw()
leg=ROOT.TLegend(0.65, 0.65,0.88, 0.85)  
leg.SetBorderSize( 0 )
leg.SetFillStyle( 1001 )
leg.SetFillColor(kWhite) 

leg.AddEntry( graph_limit40 , "Expected",  "LP" )
leg.AddEntry( graph_limit40_68up, "m = 0.3 GeV",  "F" ) 
leg.AddEntry( graph_limit188_68up, "m = 1.3 GeV",  "F" )
leg.AddEntry( graph_limit231_68up, "m = 2 GeV",  "F" )
leg.AddEntry( graph_limit301_68up, "m = 4 GeV",  "F" )
leg.AddEntry( graph_limit341_68up, "m = 6 GeV",  "F" )
leg.AddEntry( graph_limit357_68up, "m = 7 GeV",  "F" )
#leg.AddEntry( graph_limit40_95up, "#pm 2#sigma",  "F" ) 

leg.Draw("same")
c1.SaveAs("limit2018C_cmsdas_v2_v2.root")
c1.SaveAs("limit2018C_cmsdas_v2_v2.pdf")





