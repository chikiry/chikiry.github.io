# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# Modificación eliminar indigo del sistema. Proveedor: CTA
# ----------------------------------------------------------------------------
#######################################################################


import shutil
import xbmc
import time


addon_path = xbmc.translatePath(('special://home/addons/plugin.program.indigo')).decode('utf-8')
shutil.rmtree(addon_path, ignore_errors=True)







