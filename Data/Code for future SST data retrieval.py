#!/usr/bin/env python3

import os
import shutil
import hashlib
import time
import re
import itertools
import threading
import sys
import ssl
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from platform import python_version

################################################################
#
# Generated by: NSF NCAR Climate Data Gateway
# Created: 2024-10-21T19:04:11-06:00
#
# Your download selection includes data that might be secured using API Token based
# authentication. Therefore, this script can have your api-token. If you
# re-generate your API Token after you download this script, the download will
# fail. If that happens, you can either re-download the script or you can edit
# this script replacing the old API Token with the new one. View your API token
# by going to "Account Home":
#
# https://www.earthsystemgrid.org/account/user/account-home.html
#
# and clicking on the "API Token" link under "Personal Account". You will be asked
# to log into the application before you can view your API Token.
#
# Usage: python3 python-ucar.cgd.cesm2le.atm.proc.monthly_ave.SST-20241021T1904.py
# Version: 1.0.1
#
# Dataset
# ucar.cgd.cesm2le.atm.proc.monthly_ave.SST
# 6db903ae-e94b-45c5-a37d-0a56bc8c5279
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.monthly_ave.SST.html
# https://www.earthsystemgrid.org/dataset/id/6db903ae-e94b-45c5-a37d-0a56bc8c5279.html
#
# Dataset Version
# 1
# 14e5bacc-b74d-4ee3-a961-3de48f7607bc
# https://www.earthsystemgrid.org/dataset/ucar.cgd.cesm2le.atm.proc.monthly_ave.SST/version/1.html
# https://www.earthsystemgrid.org/dataset/version/id/14e5bacc-b74d-4ee3-a961-3de48f7607bc.html
#
################################################################

print('Please email feedback to esg-support@earthsystemgrid.org.\n')

data = [
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.201501-202412.nc','bytes':'10482477','md5Checksum':'1d86c3dcf1b24240b2c76dbb8939003e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.202501-203412.nc','bytes':'10495987','md5Checksum':'5f2ef2b050b6fc089c251ad833318925'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.203501-204412.nc','bytes':'10508074','md5Checksum':'0759dc0dc3b6dbb2fa45c4a71512c612'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.011.cam.h0.SST.204501-205412.nc','bytes':'10532575','md5Checksum':'122f89fa5f54c8794895d8c93e12dd4d'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.201501-202412.nc','bytes':'10475297','md5Checksum':'c3a70a84da6089cecfe52c1e6cd7bff8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.202501-203412.nc','bytes':'10485832','md5Checksum':'8e9ea02444f400be65b630bef5832b93'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.203501-204412.nc','bytes':'10518215','md5Checksum':'309148675ede6bfdaf927335c8e383d7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.012.cam.h0.SST.204501-205412.nc','bytes':'10521504','md5Checksum':'de3ed5be77f1ee334f78bf51ebcd3b14'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.201501-202412.nc','bytes':'10475259','md5Checksum':'25c61c0065cc4166ffad53aeb48e1d91'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.202501-203412.nc','bytes':'10493995','md5Checksum':'e903ca69a4d616c6c8745ccf7cb90f22'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.203501-204412.nc','bytes':'10499976','md5Checksum':'529cf3e969e747a30d2a06ede751ddb9'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.013.cam.h0.SST.204501-205412.nc','bytes':'10528895','md5Checksum':'68f8cdca6e1837208070cf8f67e42b15'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.201501-202412.nc','bytes':'10456686','md5Checksum':'3f04d662a3a65f5315506a6a301f3e48'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.202501-203412.nc','bytes':'10484737','md5Checksum':'e060adc9fe969c2ffac956e9baef2c3b'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.203501-204412.nc','bytes':'10520841','md5Checksum':'ada31aa15a0579cc1f8dcc9f32b35007'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.014.cam.h0.SST.204501-205412.nc','bytes':'10541578','md5Checksum':'6b393f4345b10c096ba8cfa8caad8b46'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.201501-202412.nc','bytes':'10457971','md5Checksum':'4deaf98ec087378225766f8cdbeedbfb'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.202501-203412.nc','bytes':'10479272','md5Checksum':'1f30714b884de4aebae3f4685142770e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.203501-204412.nc','bytes':'10495226','md5Checksum':'7ebce6d63e092ca36d4ec3254e7fc482'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.015.cam.h0.SST.204501-205412.nc','bytes':'10513178','md5Checksum':'1ea050bcbf29ed30ca88f16f5b8414be'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.201501-202412.nc','bytes':'10461007','md5Checksum':'106522455c36102244c73c1b35ef038e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.202501-203412.nc','bytes':'10482975','md5Checksum':'3eb7442db6ab43ce977c704139b1f77c'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.203501-204412.nc','bytes':'10493635','md5Checksum':'383d1702560bf3f614c61e174e8feb14'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.016.cam.h0.SST.204501-205412.nc','bytes':'10552228','md5Checksum':'75315f812e50eb2ebe7f4747da1bd5d4'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.201501-202412.nc','bytes':'10460834','md5Checksum':'d2a2df40b29e838fe84a9b0741dd1b29'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.202501-203412.nc','bytes':'10475326','md5Checksum':'75abf4e7d7aee867fcdd66a2d12bdd7e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.203501-204412.nc','bytes':'10498423','md5Checksum':'a3f105e04d69bc866212dee900f923d3'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.017.cam.h0.SST.204501-205412.nc','bytes':'10515733','md5Checksum':'ebb8ed2c318a15fbc4a49df9a3f668b1'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.201501-202412.nc','bytes':'10468045','md5Checksum':'b51e35452d24cd47f070193820bf25c9'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.202501-203412.nc','bytes':'10500128','md5Checksum':'1509458ad7df4cb9df5c50bb91f0d789'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.203501-204412.nc','bytes':'10511127','md5Checksum':'caffc33b0a1fcce7ff3fa075ac42e178'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.018.cam.h0.SST.204501-205412.nc','bytes':'10539980','md5Checksum':'68ed2cf29a19d5dc6ec90a94a656ff8e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.201501-202412.nc','bytes':'10452447','md5Checksum':'ca8ff7de9a606b7f497fb4686b6b0e79'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.202501-203412.nc','bytes':'10486982','md5Checksum':'a5f4f9d90be7ce1eca476e2892b2242c'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.203501-204412.nc','bytes':'10501107','md5Checksum':'fc63f70fdcb52334225a7ae45dc37e48'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.019.cam.h0.SST.204501-205412.nc','bytes':'10530553','md5Checksum':'0133cd2eed8ceabc31d48c38fc652f7d'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.201501-202412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.201501-202412.nc','bytes':'10475559','md5Checksum':'6b5cf2d712e15cbf0d820cac5e00956a'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.202501-203412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.202501-203412.nc','bytes':'10488257','md5Checksum':'5d4748311e0b7b7eac69e0d6b2996475'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.203501-204412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.203501-204412.nc','bytes':'10520910','md5Checksum':'658363fd8d0d5e132593048f6f0f6504'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.204501-205412.nc','filename':'b.e21.BSSP370smbb.f09_g17.LE2-1301.020.cam.h0.SST.204501-205412.nc','bytes':'10535103','md5Checksum':'0ae54f53fdcd03f9d52fc38c0d7e9b46'},]

def main(data):

    args = processArguments()

    for d in data:
        executeDownload(Download(args, d))

def processArguments():

    args = {}
    args.update({'apiToken': 'HgUErFsgKxHZT2ONJzh7Et5kyRfKHX4qMR9DaN2h'})
    args.update({'userAgent': 'python/{}/gateway/{}'.format(python_version(), '4.4.14-20240904-204054')})
    args.update({'attemptMax': 10})
    args.update({'initialSleepSeconds': 10})
    args.update({'sleepMultiplier': 3})
    args.update({'sleepMaxSeconds': 900})
    args.update({'insecure': False})

    if '-k' in sys.argv or '--insecure' in sys.argv:
        args.update({'insecure': True})

    if '-h' in sys.argv or '--help' in sys.argv:
        print('Usage: {} [options...]'.format(sys.argv[0]))
        print(' -h, --help        Show usage')
        print(' -k, --insecure    Allow insecure server connections (no certificate check) when using SSL')
        exit(0)

    return args

def executeDownload(download):

    if not os.path.isfile(download.filename):
        attemptAndValidateDownload(download)
        moveDownload(download)
    else:
        download.success = True
        download.valid = True

    reportDownload(download)

def moveDownload(download):

    if download.success and (download.valid or download.vwarning):
        os.rename(download.filenamePart, download.filename)

def reportDownload(download):

    if download.success and download.valid:
        print('{} download successful'.format(download.filename))

    if download.success and not download.valid and download.vwarning:
        print('{} download validation warning: {}'.format(download.filename, download.vwarning))

    if download.success and not download.valid and download.verror:
        print('{} download validation error: {}'.format(download.filename, download.verror))

    if not download.success and download.error:
        print('{} download failed: {}'.format(download.filename, download.error))

def attemptAndValidateDownload(download):

    while download.attempt:
        downloadFile(download)

    if download.success:
        validateFile(download)

def downloadFile(download):

    try :
        startOrResumeDownload(download)
    except HTTPError as error:
        handleHTTPErrorAttempt(download, error)
    except URLError as error:
        handleRecoverableAttempt(download, error)
    except TimeoutError as error:
        handleRecoverableAttempt(download, error)
    except Exception as error:
        handleIrrecoverableAttempt(download, error)
    else:
        handleSuccessfulAttempt(download)

def startOrResumeDownload(download):

    startAnimateDownload('{} downloading:'.format(download.filename))

    if os.path.isfile(download.filenamePart):
        resumeDownloadFile(download)
    else:
        startDownloadFile(download)

def startAnimateDownload(message):
    global animateMessage
    global animateOn

    animateMessage = message
    animateOn = True

    # making the animation run as a daemon thread allows it to
    # exit when the parent (main) is terminated or killed
    t = threading.Thread(daemon=True, target=animateDownload)
    t.start()

def stopAnimateDownload(outcome):
    global animateOutcome
    global animateOn

    animateOutcome = outcome
    animateOn = False

    # wait for animation child process to stop before any parent print
    time.sleep(0.3)

def animateDownload():
    global animateMessage
    global animateOutcome
    global animateOn

    for d in itertools.cycle(['.  ', '.. ', '...', '   ']):

        if not animateOn:
            print('\r{} {}'.format(animateMessage, animateOutcome), flush=True)
            break

        print('\r{} {}'.format(animateMessage, d), end='', flush=True)
        time.sleep(0.2)

def resumeDownloadFile(download):

    request = createRequest(download, createResumeHeaders(download))
    readFile(download, request)

def startDownloadFile(download):

    request = createRequest(download, createStartHeaders(download))
    readFile(download, request)

def createResumeHeaders(download):

    headers = createStartHeaders(download)
    headers.update(createRangeHeader(download))

    return headers

def createRequest(download, headers):

    request = urllib.request.Request(download.url, headers=headers)

    return request

def createStartHeaders(download):

    headers = {}
    headers.update(createUserAgentHeader(download))

    if download.apiToken:
        headers.update(createAuthorizationHeader(download))

    return headers

def createUserAgentHeader(download):

    return {'User-agent': download.userAgent}

def createAuthorizationHeader(download):

    return {'Authorization': 'api-token {}'.format(download.apiToken)}

def createRangeHeader(download):

    start = os.path.getsize(download.filenamePart)
    header = {'Range': 'bytes={}-'.format(start)}

    return header

def readFile(download, request):

    context = createSSLContext(download)

    with urllib.request.urlopen(request, context=context) as response, open(download.filenamePart, 'ab') as fh:
        collectResponseHeaders(download, response)
        shutil.copyfileobj(response, fh)

def createSSLContext(download):

    # See:
    #      https://docs.python.org/3/library/urllib.request.html
    #      https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection
    #      https://docs.python.org/3/library/ssl.html#ssl.SSLContext
    #
    # Excerpts:
    #      If context is specified it must be a ssl.SSLContext instance...
    #      http.client.HTTPSConnection performs all the necessary certificate and hostname checks by default.

    if download.insecure:
        return ssl._create_unverified_context()

    return None

def collectResponseHeaders(download, response):

    download.responseHeaders = response.info()
    if download.responseHeaders.get('ETag'):
        download.etag = download.responseHeaders.get('ETag').strip('"')

def handleHTTPErrorAttempt(download, httpError):

    if httpError.code == 416: # 416 is Range Not Satisfiable
        # likely the file completely downloaded and validation was interrupted,
        # therefore calling it successfully downloaded and allowing validation
        # to say otherwise
        handleSuccessfulAttempt(download)
    else:
        handleRecoverableAttempt(download, httpError)

def handleRecoverableAttempt(download, error):

    stopAnimateDownload('error')

    print('failure on attempt {} downloading {}: {}'.format(download.attemptNumber, download.filename, error))

    if download.attemptNumber < download.attemptMax:
        sleepBeforeNextAttempt(download)
        download.attemptNumber += 1
    else:
        download.attempt = False
        download.error = error

def sleepBeforeNextAttempt(download):

    sleepSeconds = download.initialSleepSeconds * (download.sleepMultiplier ** (download.attemptNumber - 1))

    if sleepSeconds > download.sleepMaxSeconds:
        sleepSeconds = download.sleepMaxSeconds

    print('waiting {} seconds before next attempt to download {}'.format(sleepSeconds, download.filename))
    time.sleep(sleepSeconds)

def handleIrrecoverableAttempt(download, error):

    stopAnimateDownload('error')

    download.attempt = False
    download.error = error

def handleSuccessfulAttempt(download):

    stopAnimateDownload('done')

    download.attempt = False
    download.success = True

def validateFile(download):

    try:
        validateAllSteps(download)
    except InvalidDownload as error:
        download.valid = False
        download.vwarning = str(error)
    except Exception as error:
        download.valid = False
        download.verror = error
    else:
        download.valid = True

def validateAllSteps(download):

    verrorData = validatePerData(download)
    verrorEtag = validatePerEtag(download)
    verrorStale = validateStaleness(download)

    if verrorData and verrorEtag:
        raise verrorData

    if verrorStale:
        raise verrorStale

def validatePerData(download):

    try:
        validateBytes(download)
        validateChecksum(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateBytes(download):

    size = os.path.getsize(download.filenamePart)
    if not download.bytes == size:
        raise InvalidSizeValue(download, size)

def validateChecksum(download):

    if download.md5Checksum:
        md5Checksum = readMd5Checksum(download)
        if not download.md5Checksum == md5Checksum:
            raise InvalidChecksumValue(download, md5Checksum)
    else:
        raise UnableToPerformChecksum(download)

def readMd5Checksum(download):

    hash_md5 = hashlib.md5()

    with open(download.filenamePart, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def validatePerEtag(download):

    try:
        validateChecksumEtag(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateChecksumEtag(download):

    if isEtagChecksum(download):
        md5Checksum = readMd5Checksum(download)
        if not download.etag == md5Checksum:
            raise InvalidChecksumValuePerEtag(download, md5Checksum)
    else:
        raise UnableToPerformChecksum(download)

def isEtagChecksum(download):

    return download.etag and re.fullmatch(r'[a-z0-9]+', download.etag)

def validateStaleness(download):

    try:
        validateStaleChecksum(download)
    except InvalidDownload as error:
        return error
    else:
        return None

def validateStaleChecksum(download):

    if isEtagChecksum(download):
        if not download.md5Checksum or download.md5Checksum != download.etag:
            raise StaleChecksumValue(download)

class InvalidDownload(Exception):

    pass

class InvalidSizeValue(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid byte size: downloaded file is {} bytes but should be {}'.format(actual, download.bytes))

class InvalidChecksumValue(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid checksum: downloaded file is {} but should be {}'.format(actual, download.md5Checksum))

class InvalidChecksumValuePerEtag(InvalidDownload):

    def __init__(self, download, actual):
        super().__init__('invalid checksum: downloaded file is {} but should be {} according to server'.format(actual, download.etag))

class UnableToPerformChecksum(InvalidDownload):

    def __init__(self, download):
        super().__init__('cannot verify checksum')

class StaleChecksumValue(InvalidDownload):

    def __init__(self, download):
        super().__init__('checksum value has changed')

class Download():

    def __init__(self, args, datum):

        self.apiToken = args.get('apiToken')
        self.userAgent = args.get('userAgent')
        self.attemptMax = args.get('attemptMax')
        self.initialSleepSeconds = args.get('initialSleepSeconds')
        self.sleepMultiplier = args.get('sleepMultiplier')
        self.sleepMaxSeconds = args.get('sleepMaxSeconds')
        self.insecure = args.get('insecure')

        self.url = datum.get('url')
        self.filename = datum.get('filename')
        self.bytes = int(datum.get('bytes'))
        self.md5Checksum = datum.get('md5Checksum')

        self.filenamePart = self.filename + '.part'
        self.success = False
        self.attempt = True
        self.attemptNumber = 1
        self.responseHeaders = {}
        self.etag = None
        self.error = None
        self.valid = False
        self.vwarning = None
        self.verror = None

    def __str__(self):
        return f'url: {self.url}, filename: {self.filename}, bytes: {self.bytes}, md5Checksum: {self.md5Checksum}'

if __name__ == '__main__':
    main(data)