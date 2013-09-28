#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/ChargedLeptons.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/IdentifiedFinalState.hh"
#include "Rivet/Projections/UnstableFinalState.hh"
#include "Rivet/Projections/LeptonClusters.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/AnalysisLoader.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/Tools/ParticleIdUtils.hh"
#include "Rivet/RivetAIDA.hh"
#include "Rivet/Particle.fhh"

#include <boost/assign/list_inserter.hpp>
#include <boost/assign.hpp>

// Follow Rivet coding style guidelines
//   - https://rivet.hepforge.org/trac/wiki/CodingStyleGuide
//   - http://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS

#define MOREPLOT

using namespace std;

namespace Rivet {

class CMS_TOP_12_028 : public Analysis {
public:
  enum DECAYMODE {
    DECAYMODE_NONE = 0, DECAYMODE_EE, DECAYMODE_MM, DECAYMODE_EM,
    DECAYMODE_SIZE
  };

  enum CUTSTEP {
    CUTSTEP_ALL = 0, CUTSTEP_LEPTON, CUTSTEP_DILEPTON, CUTSTEP_JET, CUTSTEP_MET, CUTSTEP_BTAG,
    CUTSTEP_SIZE
  };

  constexpr static double _top_massPDG = 173.5;
  constexpr static double _w_massPDG = 80.385;
  constexpr static int _ghost_b_id = 7;

public:
  CMS_TOP_12_028() : Analysis("CMS_TOP_12_028") {
  }

  bool hasBDescendants(const GenParticle* p) {
    const GenVertex* v = p->end_vertex();
    if ( !v ) return false;
    for ( HepMC::GenVertex::particles_out_const_iterator dau = v->particles_out_const_begin();
          dau != v->particles_out_const_end(); ++dau ) {
      if ( PID::hasBottom((*dau)->pdg_id()) ) return true;
      else if ( hasBDescendants(*dau) ) return true;
    }
    return false;
  }

  void init() {
    // Leptons
    FinalState fsForDressup;
    std::vector<std::pair<double, double> > etaForDressup;
    etaForDressup.push_back(std::make_pair(-2.5, 2.5));

    IdentifiedFinalState allMuons(-2.4, 2.4);
    allMuons.acceptIdPair(MUON);
    LeptonClusters muons(fsForDressup, allMuons, 0.1, true, etaForDressup, 20*GeV);

    IdentifiedFinalState allElectrons(-2.4, 2.4);
    allElectrons.acceptIdPair(ELECTRON);
    LeptonClusters electrons(fsForDressup, allElectrons, 0.1, true, etaForDressup, 20*GeV);

    addProjection(muons, "muons");
    addProjection(electrons, "electrons");

    // Neutrinos
    IdentifiedFinalState neutrinos(-5.0, 5.0, 0*GeV);
    neutrinos.acceptIdPair(NU_MU);
    neutrinos.acceptIdPair(NU_E);
    addProjection(neutrinos, "neutrinos");

    // Jets
    VetoedFinalState fsForJets(FinalState(-5.0, 5.0));
    fsForJets.vetoNeutrinos();
    fsForJets.addVetoOnThisFinalState(muons);
    fsForJets.addVetoOnThisFinalState(electrons);
    addProjection(fsForJets, "fsForJets");
    //addProjection(FastJets(fsForJets, FastJets::ANTIKT, 0.5), "jets");
    addProjection(MissingMomentum(fsForJets), "metJet");

    // For the B hadrons
    UnstableFinalState ufs(-2.5, 2.5);
    addProjection(ufs, "unstables");

    // Book histograms
    // Plots definitions in the PAS twiki
    //    https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsTOP12028
    int nHist = 0;
    _h_lepton1_pT = bookHistogram1D("lepton1_pT", ++nHist, 1, 1);
    _h_lepton1_eta = bookHistogram1D("lepton1_eta", ++nHist, 1, 1);

    _h_lepton2_pT = bookHistogram1D("lepton2_pT", ++nHist, 1, 1);
    _h_lepton2_eta = bookHistogram1D("lepton2_eta", ++nHist, 1, 1);

    _h_dilepton_pT = bookHistogram1D("dilepton_pT", ++nHist, 1, 1);
    _h_dilepton_mass = bookHistogram1D("dilepton_mass", ++nHist, 1, 1);

    _h_bjet1_pT = bookHistogram1D("bjet1_pT", ++nHist, 1, 1);
    _h_bjet1_eta = bookHistogram1D("bjet1_eta", ++nHist, 1, 1);

    _h_bjet2_pT = bookHistogram1D("bjet2_pT", ++nHist, 1, 1);
    _h_bjet2_eta = bookHistogram1D("bjet2_eta", ++nHist, 1, 1);

    _h_leptonJet_mass = bookHistogram1D("leptonJet_mass", ++nHist, 1, 1);

    _h_top1_pT = bookHistogram1D("top1_pT", ++nHist, 1, 1);
    _h_top1_rapidity = bookHistogram1D("top1_rapidity", ++nHist, 1, 1);

    _h_top2_pT = bookHistogram1D("top2_pT", ++nHist, 1, 1);
    _h_top2_rapidity = bookHistogram1D("top2_rapidity", ++nHist, 1, 1);

    _h_top_pT = bookHistogram1D("top_pT", ++nHist, 1, 1);
    _h_top_rapidity = bookHistogram1D("top_rapidity", ++nHist, 1, 1);

#ifdef MOREPLOT
    _h_w_mass   = bookHistogram1D("w_mass", 50, 30, 180);
    _h_top_mass = bookHistogram1D("top_mass", 50, 80, 250);
#endif

    _h_ttbar_pT = bookHistogram1D("ttbar_pT", ++nHist, 1, 1);
    _h_ttbar_mass = bookHistogram1D("ttbar_mass", ++nHist, 1, 1);
    _h_ttbar_rapidity = bookHistogram1D("ttbar_rapidity", ++nHist, 1, 1);
  }

  void analyze(const Event& event) {
    double weight = event.weight();

    // Figure out generator internal information
    const GenEvent& genEvent = event.genEvent();
    // Separate samples by production mechanism
    const int parton1Id = genEvent.pdf_info()->id1();
    const int parton2Id = genEvent.pdf_info()->id2();
    if ( parton1Id == 0 and parton2Id == 0 ) {
      // Gluon-Gluon collision
    }
    else if ( parton1Id != 0 and parton2Id != 0 ) {
      // Quark-Quark collision
      weight = 0;
    }
    else
    {
      // Quark-Gluon collision
      weight = 0;
    }

    // Retrieve leptons and check lepton multiplicity
    //const ParticleVector electrons = applyProjection<IdentifiedFinalState>(event, "electrons").particlesByPt();
    //const ParticleVector muons     = applyProjection<IdentifiedFinalState>(event, "muons"    ).particlesByPt();
    const ParticleVector electrons = applyProjection<LeptonClusters>(event, "electrons").particlesByPt();
    const ParticleVector muons     = applyProjection<LeptonClusters>(event, "muons"    ).particlesByPt();
    DECAYMODE decayMode = DECAYMODE_NONE;
    if ( electrons.size() == 2 and muons.size() == 0 ) decayMode = DECAYMODE_EE;
    else if ( electrons.size() == 0 and muons.size() == 2 ) decayMode = DECAYMODE_MM;
    else if ( electrons.size() == 1 and muons.size() == 1 ) decayMode = DECAYMODE_EM;
    else {
      MSG_DEBUG("Event failed lepton multiplicity cut");
      MSG_DEBUG("  nElectron = " << electrons.size());
      MSG_DEBUG("  nMuon     = " << muons.size()    );
      vetoEvent;
    }

    // Select dilepton pair
    FourMomentum lepton_momentum[2];
    int dilepton_charge;
    if ( decayMode == DECAYMODE_EE ) {
      dilepton_charge = PID::threeCharge(electrons[0]) + PID::threeCharge(electrons[1]);
      lepton_momentum[0] = electrons[0].momentum();
      lepton_momentum[1] = electrons[1].momentum();
    }
    else if ( decayMode == DECAYMODE_MM ) {
      dilepton_charge = PID::threeCharge(muons[0]) + PID::threeCharge(muons[1]);
      lepton_momentum[0] = muons[0].momentum();
      lepton_momentum[1] = muons[1].momentum();
    }
    else
    {
      dilepton_charge = PID::threeCharge(electrons[0]) + PID::threeCharge(electrons[0]);
      lepton_momentum[0] = electrons[0].momentum();
      lepton_momentum[1] = muons[0].momentum();
      if ( lepton_momentum[0].pT() < lepton_momentum[1].pT() ) {
        std::swap(lepton_momentum[0], lepton_momentum[1]);
      }
    }
    dilepton_charge /= 3;
    if ( dilepton_charge != 0 ) {
      MSG_DEBUG("Event failed opposite signed lepton cut, charge = " << dilepton_charge);
      vetoEvent;
    }
    FourMomentum dilepton_momentum = lepton_momentum[0]+lepton_momentum[1];
    const double dilepton_mass = std::sqrt(std::max(0., dilepton_momentum.mass2()));

    // Find jets. Do the jet clustering after inserting ghost B hadrons into the event
    const VetoedFinalState& fsForJets = applyProjection<VetoedFinalState>(event, "fsForJets");
    ParticleVector particlesForJets = fsForJets.particles();
    const UnstableFinalState& ufs = applyProjection<UnstableFinalState>(event, "unstables");
    foreach ( const Particle& p, ufs.particles() ) {
      if ( !PID::hasBottom(p.pdgId()) ) continue;
      if ( hasBDescendants(&p.genParticle()) ) continue; // Avoid double counting like B*->B+gamma

      // Put ghost b hadrons into particle collection for jets
      // These ghost b hadrons acts as pointing vectors not to change jet clustering (arXiv:0802.1188)
      Particle ghostB(_ghost_b_id, 1e-20*p.momentum());
      particlesForJets.push_back(ghostB);
    }
    // Do the FastJet algorithm.
    // The "fsForJets" are dummy here. This constructor can be replaced from Rivet 2.0
    FastJets jetAlg(fsForJets, FastJets::ANTIKT, 0.5);
    jetAlg.calc(particlesForJets);
    const Jets jets = jetAlg.jetsByPt(30*GeV, MAXDOUBLE, -2.4, 2.4);
    if ( jets.size() < 2 ) {
      MSG_DEBUG("Event failed jet multiplicity cut, nJet = " << jets.size());
      vetoEvent;
    }

    // MET
    //const MissingMomentum& metJet = applyProjection<MissingMomentum>(event, "metJet");
    //FourMomentum met = -metJet.visibleMomentum(); // This MET definition is inconsistent with pseudo-top
    const ParticleVector neutrinos = applyProjection<IdentifiedFinalState>(event, "neutrinos").particlesByPt();
    if ( neutrinos.size() < 2 ) {
      MSG_DEBUG("Event failed neutrino multiplicity cut, nNeutrino = " << neutrinos.size());
      vetoEvent;
    }
    FourMomentum met = neutrinos[0].momentum() + neutrinos[1].momentum();
    //if ( decayMode != DECAYMODE_EM and met.perp() < 40*GeV ) {
    //  MSG_DEBUG("Event failed missing ET cut, MET = " << met.perp());
    //  vetoEvent;
    //}

    Jets bjets;
    foreach ( const Jet& jet, jets ) {
      if ( !jet.containsParticleId(_ghost_b_id) ) continue; // Find ghost b hadrons as stable bprime
      bjets.push_back(jet);
    }
    if ( bjets.size() < 2 ) {
      MSG_DEBUG("Event failed b-tagging cut, nBJet = " << bjets.size());
      vetoEvent;
    }

    // Find the best W candidates
    FourMomentum wCands_momentum[2];
    int neutrinoIndex[2] = {-1, -1};
    if ( true ) { // Trick to hide temp variables
      const FourMomentum w00 = lepton_momentum[0]+neutrinos[0].momentum();
      const FourMomentum w11 = lepton_momentum[1]+neutrinos[1].momentum();
      const FourMomentum w01 = lepton_momentum[0]+neutrinos[1].momentum();
      const FourMomentum w10 = lepton_momentum[1]+neutrinos[0].momentum();
      const double w00_mass = std::sqrt(std::min(0., w00.mass2()));
      const double w11_mass = std::sqrt(std::min(0., w11.mass2()));
      const double w01_mass = std::sqrt(std::min(0., w01.mass2()));
      const double w10_mass = std::sqrt(std::min(0., w10.mass2()));

      if ( abs(w00_mass-_w_massPDG)+abs(w11_mass-_w_massPDG) < abs(w01_mass-_w_massPDG)+abs(w10_mass-_w_massPDG) ) {
        wCands_momentum[0] = w00;
        wCands_momentum[1] = w11;
        neutrinoIndex[0] = 0;
        neutrinoIndex[1] = 1;
      }
      else {
        wCands_momentum[0] = w01;
        wCands_momentum[1] = w10;
        neutrinoIndex[0] = 1;
        neutrinoIndex[1] = 0;
      }

      //if ( abs(wCands_momentum[0].mass()-_w_massPDG) > 40 or abs(wCands_momentum[1].mass()-_w_massPDG) > 40 ) {
      //  vetoEvent;
      //}
    }

    // Then proceed to top candidates, doing every jet combinations
    FourMomentum tCands_momentum[2];
    FourMomentum lbCands_momentum[2];
    // Before top combination, check existence of W candidate
    if ( neutrinoIndex[0] == -1 or neutrinoIndex[1] == -1 ) {
      //MSG_DEBUG("Event failed W combination. We don't veto this event but W/top related variables will be null");
      MSG_DEBUG("Event failed W candidate combination");
      vetoEvent;
    }
    else {
      int bjetIndex[2] = {-1, -1};
      double massRes = 1e9;
      for ( int i=0, n=bjets.size(); i<n; ++i ) {
        const FourMomentum tmpTPair1 = wCands_momentum[0]+bjets[i].momentum();
        const double tmpTPair1_mass = std::sqrt(std::min(0., tmpTPair1.mass2()));
        for ( int j=0; j<n; ++j ) {
          if ( i == j ) continue;
          const FourMomentum tmpTPair2 = wCands_momentum[1]+bjets[j].momentum();
          const double tmpTPair2_mass = std::sqrt(std::min(0., tmpTPair2.mass2()));
          const double tmpMassRes = abs(tmpTPair1_mass-_top_massPDG) + abs(tmpTPair2_mass-_top_massPDG);
          if ( tmpMassRes > massRes ) continue;

          massRes = tmpMassRes;
          bjetIndex[0] = i;
          bjetIndex[1] = j;
        }
      }
      if ( bjetIndex[0] != -1 and bjetIndex[1] != -1 ) {
        tCands_momentum[0] = wCands_momentum[0]+bjets[bjetIndex[0]].momentum();
        tCands_momentum[1] = wCands_momentum[1]+bjets[bjetIndex[1]].momentum();
        lbCands_momentum[0] = lepton_momentum[0]+bjets[bjetIndex[0]].momentum();
        lbCands_momentum[1] = lepton_momentum[1]+bjets[bjetIndex[1]].momentum();
      }
      else {
        MSG_DEBUG("Event failed top candidate combination");
        vetoEvent;
      }
    }

    //if ( abs(tCands_momentum[0].mass()-_top_massPDG) > 40 or abs(tCands_momentum[1].mass()-_top_massPDG) > 40 ) {
    //  vetoEvent;
    //}

    if ( tCands_momentum[0].pT() < tCands_momentum[1].pT() ) {
      std::swap(tCands_momentum[0], tCands_momentum[1]);
      //std::swap(lbCands_momentum[0], lbCands_momentum[1]);
    }

    // Selection is done, start filling histograms
    _h_lepton1_pT->fill(lepton_momentum[0].pT(), weight);
    _h_lepton1_eta->fill(lepton_momentum[0].eta(), weight);
    _h_lepton2_pT->fill(lepton_momentum[1].pT(), weight);
    _h_lepton2_eta->fill(lepton_momentum[1].eta(), weight);

    _h_dilepton_pT->fill(dilepton_momentum.pT(), weight);
    _h_dilepton_mass->fill(dilepton_mass, weight);

    _h_bjet1_pT->fill(bjets[0].momentum().pT(), weight);
    _h_bjet1_eta->fill(bjets[0].momentum().eta(), weight);
    _h_bjet2_pT->fill(bjets[1].momentum().pT(), weight);
    _h_bjet2_eta->fill(bjets[1].momentum().eta(), weight);

    _h_leptonJet_mass->fill(lbCands_momentum[0].mass(), weight);
    _h_leptonJet_mass->fill(lbCands_momentum[1].mass(), weight);

    // Additional cuts to go to particle level definition
    if ( decayMode != DECAYMODE_EM and ( dilepton_mass < 20 or abs(dilepton_mass-91.2) < 15 ) ) {
      MSG_DEBUG("Event failed dilepton mass cut, m(l+l-) = " << dilepton_mass);
      vetoEvent;
    }

    const double t1Pt = tCands_momentum[0].pT();
    const double t2Pt = tCands_momentum[1].pT();
    const double t1Rapidity = tCands_momentum[0].rapidity();
    const double t2Rapidity = tCands_momentum[1].rapidity();
    _h_top1_pT->fill(t1Pt, weight);
    _h_top1_rapidity->fill(t1Rapidity, weight);
    _h_top2_pT->fill(t2Pt, weight);
    _h_top2_rapidity->fill(t2Rapidity, weight);

    _h_top_pT->fill(t1Pt, weight);
    _h_top_rapidity->fill(t1Rapidity, weight);
    _h_top_pT->fill(t2Pt, weight);
    _h_top_rapidity->fill(t2Rapidity, weight);

    const FourMomentum ttCand_momentum = tCands_momentum[0]+tCands_momentum[1];
    _h_ttbar_pT->fill(ttCand_momentum.pT(), weight);
    _h_ttbar_mass->fill(ttCand_momentum.mass(), weight);
    _h_ttbar_rapidity->fill(ttCand_momentum.rapidity(), weight);

#ifdef MOREPLOT
    _h_w_mass->fill(wCands_momentum[0].mass(), weight);
    _h_w_mass->fill(wCands_momentum[1].mass(), weight);
    _h_top_mass->fill(tCands_momentum[0].mass(), weight);
    _h_top_mass->fill(tCands_momentum[1].mass(), weight);
#endif
  }

  void finalize() {
    normalize(_h_lepton1_pT);
    normalize(_h_lepton1_eta);
    normalize(_h_lepton2_pT);
    normalize(_h_lepton2_eta);

    normalize(_h_dilepton_pT);
    normalize(_h_dilepton_mass);

    normalize(_h_bjet1_pT);
    normalize(_h_bjet1_eta);
    normalize(_h_bjet2_pT);
    normalize(_h_bjet2_eta);

    normalize(_h_leptonJet_mass);

    normalize(_h_top1_pT);
    normalize(_h_top1_rapidity);
    normalize(_h_top2_pT);
    normalize(_h_top2_rapidity);

    normalize(_h_top_pT);
    normalize(_h_top_rapidity);

    normalize(_h_ttbar_pT);
    normalize(_h_ttbar_mass);
    normalize(_h_ttbar_rapidity);

#ifdef MOREPLOT
    normalize(_h_w_mass);
    normalize(_h_top_mass);
#endif

  }

private:
#ifdef MOREPLOT
  AIDA::IHistogram1D* _h_w_mass;
  AIDA::IHistogram1D* _h_top_mass;
#endif

  // Histogram naming convention : _h_(objectName)_(variableName)
  AIDA::IHistogram1D* _h_lepton1_pT;
  AIDA::IHistogram1D* _h_lepton1_eta;
  AIDA::IHistogram1D* _h_lepton2_pT;
  AIDA::IHistogram1D* _h_lepton2_eta;

  AIDA::IHistogram1D* _h_dilepton_pT;
  AIDA::IHistogram1D* _h_dilepton_mass;

  AIDA::IHistogram1D* _h_bjet1_pT;
  AIDA::IHistogram1D* _h_bjet1_eta;
  AIDA::IHistogram1D* _h_bjet2_pT;
  AIDA::IHistogram1D* _h_bjet2_eta;

  AIDA::IHistogram1D* _h_leptonJet_mass;

  AIDA::IHistogram1D* _h_top1_pT;
  AIDA::IHistogram1D* _h_top1_rapidity;
  AIDA::IHistogram1D* _h_top2_pT;
  AIDA::IHistogram1D* _h_top2_rapidity;

  AIDA::IHistogram1D* _h_top_pT;
  AIDA::IHistogram1D* _h_top_rapidity;

  AIDA::IHistogram1D* _h_ttbar_pT;
  AIDA::IHistogram1D* _h_ttbar_mass;
  AIDA::IHistogram1D* _h_ttbar_rapidity;

};

// This global object acts as a hook for the plugin system
AnalysisBuilder<CMS_TOP_12_028> plugin_CMS_TOP_12_028;

}
