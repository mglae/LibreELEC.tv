# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2016-present Team LibreELEC (https://libreelec.tv)

import xbmcaddon
import xbmcgui
import subprocess
import os.path

bin_p = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/')

if os.path.exists(os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'bin/mrxvt')):
  terminals = {
    0: "mrxvt -m -ls",
    1: "st -e sh -l"
    }

  sel = xbmcgui.Dialog().select('Choose terminal window', ['mrxvt', 'st'])
  if sel > -1:
    subprocess.Popen(["systemd-run","sh","-c",". /etc/profile;cd;exec " + terminals[sel]], shell=False, close_fds=True)
else:
  xbmcgui.Dialog().ok('', 'This is a console-only addon')
