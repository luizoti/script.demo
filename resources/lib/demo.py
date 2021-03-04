''' A dialog Windows teste '''

import sys
import xbmcgui # pylint: disable=import-error
import xbmc  # pylint: disable=import-error

getLocalizedString = sys.modules['__main__'].getLocalizedString

BUTTON_MAP = {
    "update": ["Update Library", 10],
    "clear": ["Clear Library", 20],
    "exit": ["Exit", 30]
}
EXIT_IDS = [10, 13]

class GUI(xbmcgui.WindowXMLDialog):
    ''' A teste class dialog '''
    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)


    def onInit(self):  # pylint: disable=invalid-name
        ''' Init methods '''
        self.update = self.getControl(BUTTON_MAP["update"][1])
        self.clean = self.getControl(BUTTON_MAP["clear"][1])
        self.exit = self.getControl(BUTTON_MAP["exit"][1])
        self.update.setLabel(BUTTON_MAP["update"][0])
        self.clean.setLabel(BUTTON_MAP["clear"][0])
        self.exit.setLabel(BUTTON_MAP["exit"][0])

    def onAction(self, action): # pylint: disable=invalid-name
        ''' Init methods '''
        if action in EXIT_IDS:
            self.closeDialog()

    def onFocus(self, control_id): # pylint: disable=invalid-name
        ''' OnFocus actions '''

    def onClick(self, control_id): # pylint: disable=invalid-name
        ''' OnClick actions '''
        if control_id in BUTTON_MAP["update"]:
            # self.doAction()
            xbmc.executebuiltin("UpdateLibrary(video)")
            xbmc.executebuiltin("UpdateLibrary(music)")
        if control_id in BUTTON_MAP["clear"]:
            xbmc.executebuiltin("CleanLibrary(video)")
            xbmc.executebuiltin("CleanLibrary(music)")
            # self.doAction()
        elif control_id in BUTTON_MAP["exit"]:
            self.closeDialog()

    def doAction(self):  # pylint: disable=invalid-name
        ''' Execute actions '''

    def closeDialog(self):  # pylint: disable=invalid-name
        ''' Cloese dialog windows function '''
        self.close()
