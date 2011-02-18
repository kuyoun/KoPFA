#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TLatex.h"
#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphAsymmErrors.h"
#include <iomanip>
#include <iostream>
#include <map>
#include <sstream>
#include "TGraph.h"

using namespace std;

string int2string(int i){
  stringstream ss;
  ss << i;
  string s= ss.str();
  return s;
}

string float2string(float f,int n){
  stringstream ss;
  ss << setiosflags(ios::fixed) << setprecision(n) << f;
  string s= ss.str();
  return s;
}

void printEff(RooHist* h){
   for(int i=0 ; i < h->GetMaxSize() ; i++){
    double x;
    double y;
    double xerrhi = h->GetErrorXhigh(i);
    double xerrlo = h->GetErrorXlow(i);
    double yerrhi = h->GetErrorYhigh(i);
    double yerrlo = h->GetErrorYlow(i);
    double eff =  h->GetPoint(i,x,y);
    cout << "[" << x-xerrlo  << "," << x+xerrhi << "] "  << " eff= " << y << "(+" << yerrhi << " -" << yerrlo << ")" << endl;
  }
}

void printEff(RooHist* h1, RooHist* h2, vector<double>& data, vector<double>& mc, TGraphAsymmErrors *&h_s){
  vector<double> tmpdata;
  vector<double> tmpmc;
  TGraphAsymmErrors *tmps = new TGraphAsymmErrors();
  for(int i=0 ; i < h1->GetMaxSize() ; i++){
    double x1;
    double y1;
    double xerrhi1 = h1->GetErrorXhigh(i);
    double xerrlo1 = h1->GetErrorXlow(i);
    double yerrhi1 = h1->GetErrorYhigh(i);
    double yerrlo1 = h1->GetErrorYlow(i);
    double eff1 =  h1->GetPoint(i,x1,y1);
    double x2;
    double y2;
    double xerrhi2 = h2->GetErrorXhigh(i);
    double xerrlo2 = h2->GetErrorXlow(i);
    double yerrhi2 = h2->GetErrorYhigh(i);
    double yerrlo2 = h2->GetErrorYlow(i);
    double eff2 =  h2->GetPoint(i,x2,y2);
    tmpdata.push_back(y1);
    tmpmc.push_back(y2);
    double scalefactor = y1/y2;
    cout << "data-[" << x1-xerrlo1  << "," << x1+xerrhi1 << "] "  << " eff= " << y1 << "(+" << yerrhi1 << " -" << yerrlo1 << ")" << endl;
    cout << "MC---[" << x2-xerrlo2  << "," << x2+xerrhi2 << "] "  << " eff= " << y2 << "(+" << yerrhi2 << " -" << yerrlo2 << ")" << endl;
    cout << "scale= " << scalefactor << endl;
    tmps->SetPoint(i,x1,scalefactor);
    tmps->SetPointEXhigh(i, xerrhi1);
    tmps->SetPointEXlow(i, xerrlo1);
    double errh = yerrhi1/y2;
    double errl = yerrlo1/y2;
    tmps->SetPointEYhigh(i, errh);
    tmps->SetPointEYlow(i, errl);

  }
  data = tmpdata;
  mc = tmpmc;
  h_s = tmps;
}

//vector<string> printEff(RooHist* h, map<int,vector<double> > seff){
//   for(int i=0 ; i < h->GetMaxSize() ; i++){
//    double x;
//    double y;
//    double xerrhi = h->GetErrorXhigh(i);
//    double xerrlo = h->GetErrorXlow(i);
//    double yerrhi = h->GetErrorYhigh(i);
//    double yerrlo = h->GetErrorYlow(i);
//    double eff =  h->GetPoint(i,x,y);
//    seff[i].push_back(y);
//    cout << "[" << x-xerrlo  << "," << x+xerrhi << "] "  << " eff= " << y << "(+" << yerrhi << " -" << yerrlo << ")" << endl;
//  }
//  return seff;
//}

void setRangeY(TCanvas *c, double min=0, double max=1.1){
  for(size_t i=0, n = c->GetListOfPrimitives()->GetSize(); i <n; ++i){
    TObject *o = c->GetListOfPrimitives()->At(i);
    if(o->InheritsFrom("TH1")) ((TH1*)o)->GetYaxis()->SetRangeUser(min,max);
  }
}

void setRangeY(TPad *c, double min=0, double max=1.1){
  for(size_t i=0, n = c->GetListOfPrimitives()->GetSize(); i <n; ++i){
    TObject *o = c->GetListOfPrimitives()->At(i);
    if(o->InheritsFrom("TH1")) ((TH1*)o)->GetYaxis()->SetRangeUser(min,max);
  }
}

void setTitleY(TCanvas *c, TString title){
  for(size_t i=0, n = c->GetListOfPrimitives()->GetSize(); i <n; ++i){
    TObject *o = c->GetListOfPrimitives()->At(i);
    if(o->InheritsFrom("TH1")) ((TH1*)o)->GetYaxis()->SetTitle(Form("%s",title.Data()));
  }
}

void setTitleY(TPad *c, TString title){
  for(size_t i=0, n = c->GetListOfPrimitives()->GetSize(); i <n; ++i){
    TObject *o = c->GetListOfPrimitives()->At(i);
    if(o->InheritsFrom("TH1")) ((TH1*)o)->GetYaxis()->SetTitle(Form("%s",title.Data()));
  }
}

RooHist* getHist(TFile *f, const TString &dir, const TString &plot, int color, int style){
  cout << "getHist" << endl;
  cout << dir.Data() << endl;
  f->cd(dir.Data());
  TCanvas* c = (TCanvas*) gDirectory->FindKey(plot)->ReadObj();
  TString obj="";
  if(dir.Contains("cnt")) obj = "hxy_cnt_eff";
  else obj = "hxy_fit_eff";
  RooHist* h = (RooHist*) c->FindObject(obj);
  TH1D* hf= (TH1D*) c->FindObject("frame_202425112");

  h->SetLineWidth(2);
  h->SetLineColor(color);
  h->SetLineStyle(style);
  h->SetMarkerColor(color);
  h->SetMarkerStyle(20);
  h->SetMarkerSize(0.7);
  h->GetYaxis()->SetTitleSize(0.0);
  delete c;
  return h;
}

RooHist* getHist(TCanvas* ctmp, const TString &dir, int color, int style){
  cout << "getHist" << endl;
  TString obj="";
  if(dir.Contains("cnt")) obj = "hxy_cnt_eff";
  else obj = "hxy_fit_eff";
  RooHist* h = (RooHist*) ctmp->FindObject(obj);

  h->SetLineWidth(2);
  h->SetLineColor(color);
  h->SetLineStyle(style);
  h->SetMarkerColor(color);
  h->SetMarkerStyle(20);
  h->SetMarkerSize(0.7);
  h->GetYaxis()->SetTitleSize(0.0);

  return h;
}

void plotNewEff(TFile *f1, TFile *f2, const TString & leg1, const TString & leg2, const vector<TString>& dir, const vector<TString>& plot, const TString& printName, const TString& hName, const vector<TString>& lname, bool print=true){
  vector<double> dataPT20_50;
  vector<double> mcPT20_50;
  f1->cd(dir[0]);
  TCanvas* c1 = (TCanvas*) gDirectory->FindKey(plot[0])->ReadObj();
  setTitleY(c1,"Isolation Efficiency"); 
  if(plot[0].Contains("eta")){
    setRangeY(c1,0.7,1.1);
  }else{
    setRangeY(c1,0.5,1.1);

  }

  c1->Draw();
  TLegend *isolabel = new TLegend(.55,.20 ,.65,.45 );
  isolabel->SetHeader("rel. iso.");
  TCanvas * c = new TCanvas("c","c",800,300);

  for(int i=0; i < dir.size() ; i++){
    RooHist* h1 = getHist(f1, dir[i], plot[i], i+2, 2);
    RooHist* h2 = getHist(f2, dir[i], plot[i], i+2, 1);
    TGraphAsymmErrors* htemp = new TGraphAsymmErrors();
    vector<double> & data( h1->GetMaxSize() );
    vector<double> & mc( h2->GetMaxSize() );
    printEff(h1,h2,data,mc,htemp);
    dataPT20_50.push_back(data[3]);
    mcPT20_50.push_back(mc[3]);
    h1->Draw("PSame");
    h2->Draw("PSame");
    isolabel->AddEntry(h1, Form("%s",lname[i].Data()), "LP");
    if(i==0) doLegend(h1, h2, leg1, leg2);
    //htemp->Draw("PSame");
    //scale factor
    for(int j=0; j < h1->GetMaxSize(); j++){
      double x;
      double y;
      htemp->GetPoint(j,x,y);
      cout << "x= " << x << " y= " << y << endl;
    }
    c->cd();
    c->Draw();
    htemp->SetLineColor(i+2);
    htemp->SetMarkerColor(i+2);
    htemp->SetLineWidth(1.5);
    if(i == 0) {
      htemp->GetYaxis()->SetTitle("Scale Factor");
      htemp->GetXaxis()->SetTitle("p_{T} (GeV)");
      htemp->Draw("ALP");
    }
    else htemp->Draw("LPSame"); 
  }
  c1->cd(); 
  cout << "data" << " " ;
  for(int i=0; i < dataPT20_50.size() ;i++) cout << dataPT20_50[i] << ", " ;
  cout << endl;
  cout << "mc  " << " " ;
  for(int i=0; i < mcPT20_50.size() ;i++) cout << mcPT20_50[i] << ", " ;
  cout << endl;

  isolabel->SetFillColor(0);
  isolabel->SetTextSize(0.04);
  isolabel->SetLineColor(0);
  if(print){
    isolabel->Draw();
  }
  
  SetLatex(0.50,0.60);

  c->cd();
  isolabel->Draw();
  c1->Print(Form("c_eff_%s_%s",printName.Data(),hName.Data()));
  c1->Print(Form("c_sf_%s_%s",printName.Data(),hName.Data()));
}

void plot2Eff(TFile *f1, TFile* f2, const TString & leg1, const TString & leg2, const TString& dir1, const TString &dir2, const TString& plot1, const TString & plot2, const TString& printName, const TString& hName){

  gStyle->SetPadTickX(1);
  f1->cd(dir1);
  TCanvas* c1 = (TCanvas*) gDirectory->FindKey(plot1)->ReadObj();
  setRangeY(c1,0.5,1.1);
  //getObjects(c1);

  RooHist* h1 = getHist(f1, dir1, plot1, 4, 20);
  cout << "data-----" << plot1 << "---" << hName << "----" << endl;
  printEff(h1);

  RooHist* h2 = getHist(f2, dir2, plot2, 2, 20);
  cout << "MC-----" << plot2 << "---"<< hName << "---" << endl;
  printEff(h2);

  c1->Draw();
  h1->Draw("P Same");
  h2->Draw("P Same");

  doLegend(h1, h2, leg1, leg2);
  c1->Print("c_"+printName+"_"+hName+".png");
  c1->Print("c_"+printName+"_"+hName+".eps");

}


void plotEff(TFile* f, const TString& dir, const TString& hName){
  TCanvas * c = (TCanvas *) f->Get(Form("%s",dir.Data()));
  getObjects(c);
  RooHist* h = (RooHist*) c->FindObject(Form("%s",hName.Data()));
  h->SetLineWidth(2);
  h->SetLineColor(4);
  h->SetMarkerColor(4);
  h->SetMarkerStyle(20);
  h->SetMarkerSize(1.0);

  cout << "---" << plot << "---" << hName << "---" << endl;
  printEff(h);

  c->Draw();
}

void plot2DEff(TFile* f, TFile* f_MC, const TString& dir, const TString& plot, const TString& hName){
  gStyle->SetPalette(1);
  f->cd(dir);
  TCanvas* c = (TCanvas*) gDirectory->FindKey(plot)->ReadObj();
  TH2* h = (TH2F*) c->FindObject(plot);
  cout << "---" << plot << "---" << hName << "---" << endl;
  h->SetMarkerSize(2.1);
  h->GetXaxis()->SetMoreLogLabels(true); 
  h->SetLabelOffset(0.0005);
  h->SetTitleOffset(1.08);
  c->SetLogx();
  c->Draw();
  c->Print("c_"+plot+"_"+hName+".png");
  c->Print("c_"+plot+"_"+hName+".eps");

  f_MC->cd(dir);
  TCanvas* c2 = (TCanvas*) gDirectory->FindKey(plot)->ReadObj();
  TH2* h2 = (TH2F*) c2->FindObject(plot);
  cout << "---" << plot << "---" << hName << "---" << endl;
  h2->SetMarkerSize(2.1);
  h2->GetXaxis()->SetMoreLogLabels(true);
  h2->SetLabelOffset(0.0005);
  h2->SetTitleOffset(1.08);
  c2->SetLogx();
  c2->Draw();  
  c2->Print("c_"+plot+"_"+hName+"_mc.png");
  c2->Print("c_"+plot+"_"+hName+"_mc.eps");


  int nbinx = h->GetNbinsX();
  int nbiny = h->GetNbinsY();
  string tablefordata;
  string tableformc;
  string tableforscale;
  string columnfortable;
  for(int i=1; i <=nbinx ; i++){
    string si = int2string(i);
    string slowedge = int2string(h->GetBinLowEdge(i));
    int highedge = h->GetBinLowEdge(i) + h->GetBinWidth(i);
    string shighedge = int2string(highedge);
    string temp = "$"+slowedge + " \\GeV < p_{T} < " + shighedge+ " \\GeV$";
    tablefordata += temp; 
    tableformc += temp; 
    tableforscale += temp; 
    for(int j=1; j <=nbiny ; j++){  
      string sj = int2string(j);
      if(i==1) { 
        string slowedgey = float2string(h->ProfileY()->GetBinLowEdge(j),1);
        float highedgey = h->ProfileY()->GetBinLowEdge(j) + h->ProfileY()->GetBinWidth(j);
        string shighedgey = float2string(highedgey,1);

        if(j==1) { 
          columnfortable += "Selection";
          columnfortable = columnfortable + " ~&~ " + " $|\\eta|<"+ shighedgey +"$";
        }else if( j == nbiny ){
          columnfortable = columnfortable + " ~&~ " + "$"+slowedgey + "<|\\eta|<"+ shighedgey +"$";
          columnfortable += "\\\\ \\hline"; 
        }else columnfortable = columnfortable + " ~&~ " + "$"+slowedgey + "<|\\eta|<"+ shighedgey +"$";
      }

      float effdata = h->GetBinContent(i,j);
      float errdata = h->GetBinError(i,j);
      float effmc = h2->GetBinContent(i,j);
      float errmc = h2->GetBinError(i,j);

      string seffdata = float2string(effdata,4);
      string serrdata = float2string(errdata,4);
      string seffmc = float2string(effmc,4);
      string serrmc = float2string(errmc,4);
  
      tablefordata = tablefordata+" ~&~ "+seffdata + "$\\pm$" + serrdata;
      tableformc = tableformc+" ~&~ "+seffmc + "$\\pm$" + serrmc;

      float scale = h->GetBinContent(i,j)/h2->GetBinContent(i,j);
      float scale_err = h->GetBinError(i,j)/h2->GetBinContent(i,j);
 
      string sscale = float2string(scale,4);
      string sscale_err = float2string(scale_err,4);

      tableforscale = tableforscale+" ~&~ "+ sscale+ "$\\pm$"+ sscale_err;
    }
   
    tablefordata = tablefordata + "\\\\ \n";
    tableformc = tableformc + "\\\\ \n";
    tableforscale = tableforscale + "\\\\ \n";
  }

  cout.precision(5);
  cout << "efficiency for data" << endl;
  cout << columnfortable << endl;
  cout << tablefordata << endl;
  cout << "efficiency for mc" << endl;
  cout << columnfortable << endl;
  cout << tableformc << endl;
  cout << "scale factor" << endl;
  cout << columnfortable << endl;
  cout << tableforscale << endl;

}

void getObjects( TCanvas *c){

  TObject *obj;
  TIter next(c->GetListOfPrimitives());
  while ((obj=next())) {
    cout << "Reading: " << obj->GetName() << endl;
    if (obj->InheritsFrom("TH1F")) {
      cout << "TH1F: " << obj->GetName() << endl;
    }else if (obj->InheritsFrom("TH1D")) {
      cout << "TH1D: " << obj->GetName() << endl;
    }else if (obj->InheritsFrom("RooHist")) {
      cout << "RooHisto: " << obj->GetName() << endl;
    }else if (obj->InheritsFrom("RooPlot")) {
      cout << "RooPlot: " << obj->GetName() << endl;
    }else{
      cout << "Ohter: " << obj->GetName() << endl;
    }

  }
}


void doLegend(TGraphAsymmErrors *g1, TGraphAsymmErrors *g2, const TString& lab1, const TString& lab2) {
    TLegend *leg = new TLegend(.68,.25 ,.88,.40 );
    leg->AddEntry(g1, Form("%s",lab1.Data()), "LP");
    leg->AddEntry(g2, Form("%s",lab2.Data()), "LP");
    leg->SetFillColor(0);
    leg->SetTextSize(0.04);
    leg->SetLineColor(0);
    leg->Draw();
}

void SetLatex(double x, double y){
  TLatex *label= new TLatex;
  label->SetNDC();
  label->SetTextSize(0.04);
  //label->DrawLatex(x,y,"CMS Preliminary 2010");
  label->DrawLatex(x,y-0.05,"36.1 pb^{-1} at #sqrt{s} = 7 TeV");
  label->DrawLatex(x,y-0.1,"#DeltaR=0.4");
}

