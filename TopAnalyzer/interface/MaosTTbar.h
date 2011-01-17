#ifndef KoPFA_TOPAnalyzer_MaosTTbar_h
#define KoPFA_TOPAnalyzer_MaosTTbar_h

#include "TLorentzVector.h"
#include "TMinuit.h"

namespace Ko{

  //used for function fo minuit  
  extern TLorentzVector tmpl1_;
  extern TLorentzVector tmpl2_;
  extern TLorentzVector tmpmet_;

  double mtsq(const TLorentzVector &ptl, const TLorentzVector &qt, double ml, double mchi);
  double mtsq(const TVector3 &ptl, const TVector3 &qt, double ml, double mchi);

  class MaosTTbar{
   public:
    MaosTTbar(){}

    double MT2(const TLorentzVector& metvec, const TLorentzVector &lep1,const TLorentzVector &lep2, double mchi);

    // use Minuit minimizer, this returns MT2 value, must be called first.
    double MAOS(const TLorentzVector& metvec, const TLorentzVector &lep1,const TLorentzVector &lep2, double mchi, double mY, bool orig);

    double M(){
      return (Ko::tmpl1_+Ko::tmpl2_+tmpnu1_ + tmpnu2_).M(); 
    }

    double top1M(){
      TVector3 l1 = tmpl1_.Vect();
      TVector3 l2 = tmpnu1_.Vect();
      l1.SetZ(0.0);
      l2.SetZ(0.0);

      double El_T = TMath::Hypot(tmpl1_.M(), l1.Mag());
      double Echi_T = TMath::Hypot(0, l2.Mag());
      double cosh = TMath::CosH(tmpl1_.Eta() - tmpnu1_.Eta());
      double m = sqrt( tmpl1_.M()*tmpl1_.M() + 2.0*(El_T*Echi_T*cosh - l1.Dot(l2))) ;

      return m;
      //return (Ko::tmpl1_ + tmpnu1_).M();
    } 

    double top2M(){
      TVector3 l1 = tmpl2_.Vect();
      TVector3 l2 = tmpnu2_.Vect();
      l1.SetZ(0.0);
      l2.SetZ(0.0);

      double El_T = TMath::Hypot(tmpl2_.M(), l1.Mag());
      double Echi_T = TMath::Hypot(0, l2.Mag());
      double cosh = TMath::CosH(tmpl2_.Eta() - tmpnu2_.Eta());
      double m = sqrt( tmpl2_.M()*tmpl2_.M() + 2.0*(El_T*Echi_T*cosh - l1.Dot(l2))) ;

      return m;

      //return (Ko::tmpl2_ + tmpnu2_).M();
    } 

    int findNearestTopM(double& topMass1, double& topMass2)
    {
      const double topMass11 = (Ko::tmpl1_ + tmpnu1_).M();
      const double topMass12 = (Ko::tmpl1_ + tmpnu2_).M();
      const double topMass21 = (Ko::tmpl2_ + tmpnu1_).M();
      const double topMass22 = (Ko::tmpl2_ + tmpnu2_).M();

      // Mass difference with diagonal combination
      const double dMTop11 = fabs(topMass11 - topMass22);
      const double dMTop12 = fabs(topMass12 - topMass21);

      if ( dMTop11 < dMTop12 )
      {
        topMass1 = topMass11;
        topMass2 = topMass22;

        return 1;
      }
      else
      {
        topMass1 = topMass12;
        topMass2 = topMass21;

        return -1;
      }
    }

    TLorentzVector nu1(){return tmpnu1_; }
    TLorentzVector nu2(){return tmpnu2_; }

   private:

    double arglist[10];

    TLorentzVector tmpnu1_;
    TLorentzVector tmpnu2_;
  };
 
}

#endif
