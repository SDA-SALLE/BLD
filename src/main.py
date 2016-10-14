# -*- coding: utf-8 -*-
#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
sys.path.append('core')
from clear import *
from emisions import *
from desagregation import *
from register import *
from speciation import *
from PMC import *
from unions import *

folder = os.path.join('..', 'data', 'out', '')
clear(folder)

year = raw_input('Insert year running: ')

#Archive CONVP in folder /data/in/CONVP.xlsx
archive = os.path.join('..', 'data', 'in', 'database_'+ year + '.xlsx')
emisionsconvp(archive, year)

#T/Year
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions_'+ year +'.csv')
emisionsTYear(archive, year)

#desagregation Hour
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions_'+ year +'.csv')
#final(archive)
desagregation(archive, year)


#unions
folderDesagregation = os.path.join('..', 'data', 'out', 'desagregation', '')
archives = listaCSV(folderDesagregation)

for archive in archives:
    archive = folderDesagregation + archive
    final(archive)

print 'Start speciation CONVP'

#Speciation
archivespeciation = os.path.join ('..', 'data', 'in', 'speciation', 'BLD_CONVP_SCP_PROF_PM25_' + year +'.xlsx')
folderCONVP = os.path.join('..','data', 'out', 'desagregation', '')
speciation(archivespeciation, folderCONVP)

#PMC
folderPMC = os.path.join('..','data', 'out', 'desagregation', '')
pmc(folderPMC)
folderout = os.path.join('..','data', 'out', 'speciation', '')
testingpmc(folderout)

#UNIONS
UNIONS(folderout, year)