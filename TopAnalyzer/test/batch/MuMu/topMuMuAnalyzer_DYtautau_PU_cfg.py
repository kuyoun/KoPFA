from KoPFA.TopAnalyzer.topMuMuAnalyzer_cff import process

import FWCore.ParameterSet.Config as cms

process.load("PFAnalyses.TTbarDIL.Sources.MU.MC.Fall10.patTuple_DYtautau_PU_cff")
process.muonTriggerFilterForMC = process.muonTriggerFilterForMCREDIGI38XPU
process.topWLeptonGenFilter.applyFilter = False