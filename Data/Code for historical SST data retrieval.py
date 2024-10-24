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
# Created: 2024-10-21T19:47:13-06:00
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
# Usage: python3 python-ucar.cgd.cesm2le.atm.proc.monthly_ave.SST-20241021T1947.py
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
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.195001-195912.nc','bytes':'10398474','md5Checksum':'1b6a01e5684360aca341ffa3fa9af2bf'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.196001-196912.nc','bytes':'10394893','md5Checksum':'855337717f8c9809bc3d523454633731'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.197001-197912.nc','bytes':'10379733','md5Checksum':'97ec961fc81aa95cc64edc6190852cdd'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.198001-198912.nc','bytes':'10412809','md5Checksum':'b28be4acbc6803911e9fed238852b664'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.199001-199912.nc','bytes':'10444888','md5Checksum':'8673accfb2072e8f3376263a891200a9'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.200001-200912.nc','bytes':'10455153','md5Checksum':'2055be9c96d51bd384386ca6549e940e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.011.cam.h0.SST.201001-201412.nc','bytes':'5279284','md5Checksum':'813b8a1f8f420aaef41b24cb3c8adea3'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.195001-195912.nc','bytes':'10403917','md5Checksum':'a19cb5a5124327f303a307318c94e723'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.196001-196912.nc','bytes':'10398068','md5Checksum':'9408621a7440b1716e118b402e80df2f'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.197001-197912.nc','bytes':'10417039','md5Checksum':'448d0b6a239a2f014c2580279ef1d056'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.198001-198912.nc','bytes':'10423234','md5Checksum':'9eb3d562b4cad95e7213db8fe8f2632b'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.199001-199912.nc','bytes':'10454599','md5Checksum':'330fd3ce5aa24776182cf574077b81e5'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.200001-200912.nc','bytes':'10460430','md5Checksum':'fc23a65e13da6028c266e2aff2254cb3'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.012.cam.h0.SST.201001-201412.nc','bytes':'5279225','md5Checksum':'9ecd0d035884d2f785490e94dd7297fe'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.195001-195912.nc','bytes':'10396213','md5Checksum':'2a6f63f2bed77fac893b60898b20c6ca'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.196001-196912.nc','bytes':'10412024','md5Checksum':'f6eb96658d32c431ce5e7e87b243c20b'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.197001-197912.nc','bytes':'10394424','md5Checksum':'8a92f6e7ac9b4208e4dfa56de90a5db8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.198001-198912.nc','bytes':'10413979','md5Checksum':'a84d8259a427f3a1d7b211e28973e1f7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.199001-199912.nc','bytes':'10435475','md5Checksum':'3f52db160d604591e90e6b2122ef2e26'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.200001-200912.nc','bytes':'10456246','md5Checksum':'aa2837ccdeaca94de2fb27ed9698b1bf'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.013.cam.h0.SST.201001-201412.nc','bytes':'5259464','md5Checksum':'cd4de746685e3e574ad94864eccfabf8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.195001-195912.nc','bytes':'10402342','md5Checksum':'9be6608e6a84832f75d678d31b741617'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.196001-196912.nc','bytes':'10385466','md5Checksum':'e0e35c9a2e3cfb0d89edffa69336c7c6'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.197001-197912.nc','bytes':'10379227','md5Checksum':'dd2bd1b16e87824edced6933cf894f48'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.198001-198912.nc','bytes':'10405795','md5Checksum':'2beee0ab3ca1866a2dd8139ad955f699'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.199001-199912.nc','bytes':'10436658','md5Checksum':'e02f2f40817f8f63ee22d62b3e231027'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.200001-200912.nc','bytes':'10462081','md5Checksum':'176166a7472c88e299253e89b8106ed2'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.014.cam.h0.SST.201001-201412.nc','bytes':'5274468','md5Checksum':'a0a2974e820dda8fffc0e970b9629bb8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.195001-195912.nc','bytes':'10381595','md5Checksum':'13cc71e11300c82e327f3a7f7ecbd3b5'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.196001-196912.nc','bytes':'10386291','md5Checksum':'df59c4388adb9ad5c507df697058f8ae'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.197001-197912.nc','bytes':'10408983','md5Checksum':'e384966c35a2be85a47cbcd84bf6fbfe'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.198001-198912.nc','bytes':'10409080','md5Checksum':'a5eb853223fba5b0a1b6f5ba144989ff'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.199001-199912.nc','bytes':'10435579','md5Checksum':'c157e35a8b8447ad2c31bb5416d5dbde'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.200001-200912.nc','bytes':'10448047','md5Checksum':'b24824254becd48c87f8185b82ff3c71'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.015.cam.h0.SST.201001-201412.nc','bytes':'5271727','md5Checksum':'2b5d12b48d44d0405e4cb94678914edd'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.195001-195912.nc','bytes':'10417194','md5Checksum':'449bec5bd6c74db38edb567c06e7f853'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.196001-196912.nc','bytes':'10389161','md5Checksum':'5d9d8428ee2360f0625275fb869c903a'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.197001-197912.nc','bytes':'10395452','md5Checksum':'1d25e80ce1d372cc56b4fe623b3e6174'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.198001-198912.nc','bytes':'10401947','md5Checksum':'5d64137ed02802c4ef69a0ebcfa8a33d'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.199001-199912.nc','bytes':'10426614','md5Checksum':'27bf316f4f9e9b4e0c2ee23efafce2f9'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.200001-200912.nc','bytes':'10456796','md5Checksum':'6a8e4241a5f84ea240f1faf69d69773f'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.016.cam.h0.SST.201001-201412.nc','bytes':'5264730','md5Checksum':'ccc0aed6f843cd7ca3bf95c569acbfb4'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.195001-195912.nc','bytes':'10399658','md5Checksum':'0f7fac80c998f272eb2135578141e1cf'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.196001-196912.nc','bytes':'10382284','md5Checksum':'e601f523c38dfb83a1df756345eaf972'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.197001-197912.nc','bytes':'10400758','md5Checksum':'9ed79de8ad731bd120583c26e71066d5'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.198001-198912.nc','bytes':'10416804','md5Checksum':'36ae86906d797a64939db1113a85ac4e'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.199001-199912.nc','bytes':'10430799','md5Checksum':'cb9408d5058868cf6c0c0e8bf810d1ca'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.200001-200912.nc','bytes':'10445838','md5Checksum':'f00c11dd03cd44a6e69e9aad79de5ea7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.017.cam.h0.SST.201001-201412.nc','bytes':'5269987','md5Checksum':'d934b322e66947c78ac8c59990675eef'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.195001-195912.nc','bytes':'10409029','md5Checksum':'b37821eed68f48a6b1bba4e4f867651a'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.196001-196912.nc','bytes':'10407432','md5Checksum':'3d7b054a224870a82d15a29dfd5b99f7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.197001-197912.nc','bytes':'10396246','md5Checksum':'14cc4a5c020e53cf6a640012d83ec2ff'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.198001-198912.nc','bytes':'10420426','md5Checksum':'375f365c96602e585d140261679323fb'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.199001-199912.nc','bytes':'10429792','md5Checksum':'8f9f80e62bae1b6e6665488031eeb0e7'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.200001-200912.nc','bytes':'10451904','md5Checksum':'f141e971f9253987508088157baaf904'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.018.cam.h0.SST.201001-201412.nc','bytes':'5262841','md5Checksum':'77bd5ab95b6462f09288a248dbee0476'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.195001-195912.nc','bytes':'10404716','md5Checksum':'ad78cee76758f292f7094b55d8bf0651'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.196001-196912.nc','bytes':'10383206','md5Checksum':'be5a86ec71f366f2cf0c1348be1ed8b1'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.197001-197912.nc','bytes':'10392028','md5Checksum':'0049c4e93b335119728e154db8b9b2c6'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.198001-198912.nc','bytes':'10405697','md5Checksum':'ae80587b811c69c5bd4a3cc4c4c71290'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.199001-199912.nc','bytes':'10429008','md5Checksum':'c363fb6c180ec8d85138c1919c3a5c39'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.200001-200912.nc','bytes':'10448221','md5Checksum':'d2a51aa0fb8420897e6a0ba6d51fede5'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.019.cam.h0.SST.201001-201412.nc','bytes':'5266717','md5Checksum':'4f62ef8f18efeaa677ecbadbda235b10'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.195001-195912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.195001-195912.nc','bytes':'10396979','md5Checksum':'2967d7f8d9ad9f543fd755ddf17b60d3'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.196001-196912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.196001-196912.nc','bytes':'10399539','md5Checksum':'a52891d2db826eec53c1737e55a4827f'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.197001-197912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.197001-197912.nc','bytes':'10396185','md5Checksum':'8b53776abe12300733340b1f3dae0f42'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.198001-198912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.198001-198912.nc','bytes':'10424496','md5Checksum':'9b6c833f9aa12c2ddcad62f2088e993b'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.199001-199912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.199001-199912.nc','bytes':'10446733','md5Checksum':'23b774d59b899590159f322b42fcd4e8'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.200001-200912.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.200001-200912.nc','bytes':'10448879','md5Checksum':'401b6d229dd88096d33d479362ffc569'},
     {'url':'https://tds.ucar.edu/thredds/fileServer/datazone/campaign/cgd/cesm/CESM2-LE/atm/proc/tseries/month_1/SST/b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.201001-201412.nc','filename':'b.e21.BHISTsmbb.f09_g17.LE2-1301.020.cam.h0.SST.201001-201412.nc','bytes':'5261754','md5Checksum':'7036800ba7a89be7b236c20c573ccb95'},]

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
