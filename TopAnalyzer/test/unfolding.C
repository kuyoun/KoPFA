#include "TStyle.h"
#include "TCanvas.h"
#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TVectorD.h"
#include "TLegend.h"
#include "TProfile.h"
#include "TTree.h"
#include "TCut.h"
#include "TGraphAsymmErrors.h"
#include "style.h"
#include "TGraph.h"

#include <iostream>
#include "TUnfold.h"
#include "unfold/RooUnfold-1.0.3/src/TSVDUnfold.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfold.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfoldResponse.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfoldBayes.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfoldSvd.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfoldBinByBin.h"
#include "unfold/RooUnfold-1.0.3/src/RooUnfoldInvert.h"
#include "HHStyle.h"
#include "unfolding.h"
vector<double> chi2;

void unfolding(int k=4){

  gSystem->Load("libFWCoreFWLite.so");
  gROOT->LoadMacro("tdrstyle.C");
  setTDRStyle();

  //gStyle->SetOptStat(0000);
  gStyle->SetOptFit(0011);

  TFile * file = new TFile("/afs/cern.ch/work/t/tjkim/public/store/top/TOP11013/unfold/preUnfolding.root");
  TFile * file_acceptance = new TFile("/afs/cern.ch/work/t/tjkim/public/store/top/TOP11013/unfold/acceptance.root");
  TFile * file_truthFinal = new TFile("/afs/cern.ch/work/t/tjkim/public/store/top/TOP11013/unfold/truthFinal.root");
  //response matrix
  TH2F * h2ResponseM = (TH2F*) file->Get("h2_response_m");
  //measured distribution
  //TH1F * hDataDist = (TH1F*) file->Get("hData_vsum");
  TH1F * hDataDist = (TH1F*) file->Get("hData_kin");
  //TH1F * hPseudoDataMADGRAPH = (TH1F*) file->Get("hPseudoData_vsum_MadGraph");
  //TH1F * hPseudoDataPOWHEG = (TH1F*) file->Get("hPseudoData_vsum_Powheg");
  //TH1F * hDataDistUp = (TH1F*) file->Get("hData_vsum_up");
  //TH1F * hDataDistDw = (TH1F*) file->Get("hData_vsum_dw");
  //truth level after reconstruction level selection
  TH1F * hGenDistMADGRAPH = (TH1F*) file->Get("hTruth_MadGraph");
  //TH1F * hGenDistPOWHEG = (TH1F*) file->Get("hTruth_Powheg");
  //acceptance 
  TH1F * hAcceptDistPton = (TH1F*) file_acceptance->Get("hAccept_kin_Pton");
  TH1F * hAcceptDistPtcl = (TH1F*) file_acceptance->Get("hAccept_kin_Ptcl");
  TH1F * hAcceptDistFull = (TH1F*) file_acceptance->Get("hAccept_kin_Full");
  //truth level for final
  TH1 * hGenMADGRAPH_Full = (TH1*) file_truthFinal->Get("MadGraph_Full");
  TH1 * hGenMADGRAPH_Ptcl = (TH1*) file_truthFinal->Get("MadGraph_Ptcl");
  TH1 * hGenMADGRAPH_Pton = (TH1*) file_truthFinal->Get("MadGraph_Pton");
  TH1 * hGenPOWHEG_Full = (TH1*) file_truthFinal->Get("POWHEG_Full");
  TH1 * hGenPOWHEG_Ptcl = (TH1*) file_truthFinal->Get("POWHEG_Ptcl");
  TH1 * hGenPOWHEG_Pton = (TH1*) file_truthFinal->Get("POWHEG_Pton");
  TH1 * hGenMCNLO_Full = (TH1*) file_truthFinal->Get("MCNLO_Full");
  TH1 * hGenMCNLO_Ptcl = (TH1*) file_truthFinal->Get("MCNLO_Ptcl");
  TH1 * hGenMCNLO_Pton = (TH1*) file_truthFinal->Get("MCNLO_Pton");

  TH1 * hGenMCNLO = (TH1*) file_truthFinal->Get("hTTbarM");
  TH1 * hGenMCNLO_Up = (TH1*) file_truthFinal->Get("hTTbarM_Up");
  TH1 * hGenMCNLO_Down = (TH1*) file_truthFinal->Get("hTTbarM_Down");

  TH1 * hNLOMtt = (TH1*) file_truthFinal->Get("nnll");

  double lumi = 4982;
  bool print = true; //save plots
  bool printX = true; //print cross section
  bool pseudo = false;
  bool toytest = false;

  //RooUnfold::ErrorTreatment err = RooUnfold::kNoError;  //0
  //RooUnfold::ErrorTreatment err = RooUnfold::kErrors;  //1
  RooUnfold::ErrorTreatment err = RooUnfold::kCovariance; //2
  //RooUnfold::ErrorTreatment err = RooUnfold::kCovToy; //3

  int method = 2; // BinByBin:0 Invert:1 SVD:2 Bayes:3 
  TH1F* h_unfold = unfoldingPlot(method, h2ResponseM,  hDataDist, hGenDistMADGRAPH, "kin", lumi, k, err, print, pseudo, toytest);
  //TH1F* h_unfoldup = unfoldingPlot(method, h2ResponseM,  hDataDistUp, hGenDist, "vusm_up", lumi, k, err, print, pseudo, toytest);
  //TH1F* h_unfolddw = unfoldingPlot(method, h2ResponseM,  hDataDistDw, hGenDist, "vusm_dw", lumi, k, err, print, pseudo, toytest);

  //for final plots
  bool norm =  true;
  bool log = true;
  bool bincorr = false;
  bool HBBstyle = false;

  //Full correction: set norm = false for absolute X
  FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDistFull, hGenMADGRAPH_Full, lumi, "unfold_simple_full", "dSigmadM",  0.0001, 200, false, log, bincorr, print); 
  //Full correction normalized
  //FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDistFull, hGenMADGRAPH_Full, hGenMCNLO_Full, hGenPOWHEG_Full, lumi, "unfold_Normalized_full", "dSigmadM",  0.000001, 0.06, norm, log, bincorr, print, printX, HBBstyle);

  //visible correction: set norm = false for absolute X
  //FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDistPtcl, hGenMADGRAPH_Ptcl, hGenMCNLO, hGenPOWHEG_Ptcl, lumi, "unfold", "dSigmadM",  0.00001, 0.06, false, log, bincorr, print, printX, HBBstyle); 
  //FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDistPtcl, hGenMADGRAPH_Ptcl, lumi, "unfold_simple", "dSigmadM",  0.000001, 1, false, log, bincorr, print);
  //visible correction normalized
  //FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDistPtcl, hGenMADGRAPH_Ptcl, hGenMCNLO, hGenPOWHEG_Ptcl, lumi, "unfold_Normalized", "dSigmadM",  0.000001, 0.06, norm, log, bincorr, print, printX, HBBstyle); 

  //TGraphAsymmErrors* de = FinalPlot(h_unfold, hGenDistMADGRAPH, hAcceptDist, lumi, "unfold_Normalized_simple", "dSigmadM",  0.00001, 0.06, norm, log, bincorr, print);
  //TGraphAsymmErrors* up = FinalPlot(h_unfoldup, hGenDistMADGRAPH, hAcceptDist, lumi, "unfold_Normalized_simple_up", "dSigmadM",  0.00001, 0.06, norm, log, bincorr, print);
  //TGraphAsymmErrors* dw = FinalPlot(h_unfolddw, hGenDistMADGRAPH, hAcceptDist, lumi, "unfold_Normalized_simple_dw", "dSigmadM",  0.00001, 0.06, norm, log, bincorr, print); 
  //getUncertainty(de,up,dw); 
  //For PAS TOP-11-013
  bincorr = true;
  HBBstyle = true;
  if(HBBstyle){
    gROOT->SetStyle("Plain");
    setHHStyle(*gStyle);
  }
  
   //visible phase space
  //TOP11013Plot(h_unfold, hGenDistMADGRAPH, hAcceptDistPtcl, hGenMADGRAPH_Ptcl, hGenMCNLO, hGenPOWHEG_Ptcl, lumi, "unfold_Normalized_pas013", "dSigmadM",  0.00001, 0.06, norm, log, bincorr, print, false, HBBstyle, true, hGenMCNLO_Up, hGenMCNLO_Down);
  //full phase space
  //TOP11013Plot(h_unfold, hGenDistMADGRAPH, hAcceptDistFull, hGenMADGRAPH_Full, hGenMCNLO_Full, hGenPOWHEG_Full, lumi, "unfold_Normalized_full_pas013", "dSigmadM",  0.000001, 0.06, norm, log, bincorr, print, false, HBBstyle, true, hGenMCNLO_Up, hGenMCNLO_Down);
  TOP11013Plot(h_unfold, hGenDistMADGRAPH, hAcceptDistFull, hGenMADGRAPH_Full, hGenMCNLO, hGenPOWHEG_Full, lumi, "unfold_Normalized_full_pas013", "dSigmadM",  0.000001, 0.06, norm, log, bincorr, print, false, HBBstyle, true, hGenMCNLO_Up, hGenMCNLO_Down, hNLOMtt);

  //chi2 test
  //int n = 5;
  //for(int i=1; i <=n ;i++){
  //  plot(h2ResponseM, hDataDist, hGenDist, hAcceptDist, "vsum", lumi, i, err, print, pseudo); 
  //}

  //for(int i=0; i<n ;i++){
  //  cout << "k term= " << i+1 << " : " << chi2[i] << endl;
  //}
}


