import ROOT
import os,sys
#from ROOT import TGraphAsymmErrors
#from ROOT import TGraphErrors
from ROOT import TColor
#from ROOT import TGraph                                                                                                                                                                          
from array import array
from ROOT import *
#from operator import truediv
import random
import math
import glob

#Lxy_list = ["2.0", "2.2", "2.4", "2.6", "2.8", "3.0", "4.0","10.0"]

c1=ROOT.TCanvas("c1","c1",700,500)
c1.cd()
#c1.SetGrid()                                 
c1.SetLogy()
c1.SetLogx()
gStyle.SetOptStat(0)


file2 = ROOT.TFile.Open("./hists2018_Lxy2.0_all.root", 'read')                              
mass2 = file2.Get('dimuonMass')
mass2.Draw()
mass2.SetLineColor(3)
mass2.SetTitle("")
mass2.GetYaxis().SetTitle("Counts")
mass2.GetYaxis().SetTitleSize(0.05)
mass2.GetXaxis().SetTitle("m\mu\mu [GeV]")
mass2.GetXaxis().SetTitleSize(0.05)
mass2.GetYaxis().SetTitleOffset(0.8)

"""
file22 = ROOT.TFile.Open("./hists2018_Lxy2.2_all.root", 'read')
mass22 = file22.Get('dimuonMass')
mass22.SetTitle("")
mass22.Draw("same")
mass22.SetLineColor(kRed)
#c1.Update()
"""
file24 = ROOT.TFile.Open("./hists2018_Lxy2.4_all.root", 'read')
mass24 = file24.Get('dimuonMass')
mass24.SetTitle("")
mass24.Draw("same")
mass24.SetLineColor(kYellow)

file26 = ROOT.TFile.Open("./hists2018_Lxy2.6_all.root", 'read')
mass26 = file26.Get('dimuonMass')
mass26.SetTitle("")
mass26.Draw("same")
mass26.SetLineColor(kBlue)

"""
file28 = ROOT.TFile.Open("./hists2018_Lxy2.8_all.root", 'read')
mass28 = file28.Get('dimuonMass')
mass28.SetTitle("")
mass28.Draw("same")
mass28.SetLineColor(kGreen)
"""
file3 = ROOT.TFile.Open("./hists2018_Lxy3.0_all.root", 'read')
mass3 = file3.Get('dimuonMass')
mass3.SetTitle("")
mass3.Draw("same")
mass3.SetLineColor(kGreen)

file4 = ROOT.TFile.Open("./hists2018_Lxy4.0_all.root", 'read')
mass4 = file4.Get('dimuonMass')
mass4.SetTitle("")
mass4.Draw("same")
mass4.SetLineColor(kOrange)
#c1.Update()

file10 = ROOT.TFile.Open("./hists2018_Lxy10.0_all.root", 'read')
mass10 = file10.Get('dimuonMass')
mass10.SetTitle("")
mass10.Draw("same")
mass10.SetLineColor(11)
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

leg.AddEntry( mass2 , "L > 2.0 cm",  "F" )
#leg.AddEntry( mass22, "L > 2.2 cm",  "F" )
leg.AddEntry( mass24, "L > 2.4 cm",  "F" )
leg.AddEntry( mass26, "L > 2.6 cm",  "F" )                                                    
#leg.AddEntry( mass28, "L > 2.8 cm",  "F" )
leg.AddEntry( mass3, "L > 3.0 cm",  "F" )                                                    
leg.AddEntry( mass4, "L > 4.0 cm",  "F" )
leg.AddEntry( mass10, "L > 10 cm",  "F" )                                                   
leg.Draw("same")

c1.SaveAs("spectrum.root")
c1.SaveAs("spectrum.pdf")
