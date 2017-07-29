'''
TabbedPanelItemHelper
=====================

Provides a class usable when the need arises to use data bound to a
TabbedPanelItem instead of the parent TabbedPanel.

Adds a 'vparent' attribute to the Widget used for display that references
the TabbedPanelItemHelper.

Note:
    It is recommended that the vparent attribute be an ObjectAttribute
    so as to allow bindings to it.

Author
======
Ayowel
'''

from kivy.uix.tabbedpanel import TabbedPanelItem

__all__ = ['TabbedPanelItemHelper']

class TabbedPanelItemHelper(TabbedPanelItem):
    '''See module information
    '''
    def add_widget(self, widget):
        '''Adds the vparent attribute to the Widget used for render
        '''
        if self.content and self.content.vparent == self:
            self.content.vparent = object()
        
        super(TabbedPanelItemHelper, self).add_widget(widget)
        
        if self.content: self.content.vparent = self

    def remove_widget(self, widget):
        '''Removes the vparent attribute from the widget used for render
        '''
        if self.content and self.content.vparent == self:
            self.content.vparent = object()

        super(TabbedPanelItemHelper, self).remove_widget(widget)

if __name__ == '__main__':

    from kivy.base import runTouchApp
    from kivy.lang.builder import Builder

    app = Builder.load_string('''
TabbedPanel:
    TabbedPanelItemHelper:

        info: "I'm a good guy"

        Label:
            vparent:
            text: self.vparent.info
    ''')

    runTouchApp(app)

