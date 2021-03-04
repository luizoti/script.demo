''' Default module '''
import sys
import xbmcaddon  # pylint: disable= import-error

Addon = xbmcaddon.Addon('script.demo')

# Script constants
__scriptname__ = Addon.getAddonInfo('name')
__id__ = Addon.getAddonInfo('id')
__author__ = Addon.getAddonInfo('author')
__version__ = Addon.getAddonInfo('version')
__path__ = Addon.getAddonInfo('path')

getLocalizedString = Addon.getLocalizedString
getSetting = Addon.getSetting

print('[SCRIPT][%s] version %s initialized!' % (__scriptname__, __version__))

if __name__ == "__main__":
    import resources.lib.demo as demo
    ui = demo.GUI('dialog.xml', __path__, 'default', '1080i')
    ui.doModal()
    print('[SCRIPT][%s] version %s exited!' % (__scriptname__, __version__))
    del ui

sys.modules.clear()
