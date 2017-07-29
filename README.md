# TabbedPanelItem Referer

## Concept

Contains the **TabbedPanelItemReferer** class, usefull when trying to build a
tabbedpanel based application and to separate concerns amongst several panels.

Instead of waiting for the Widget to be set, it becomes possible to use the
TabbedPanelItem to hold the information necessary for the content to be
generated.

## How to use

The **TabbedPanelItemReferer** should be used just like a **TabbedPanelItem**
would be.

When adding content to a **TabbedPanelItemReferer**, the underlying Widget will
get a vparent attribute with a reference to the **TabbedPanelItemReferer** that
will allow you to bind data to this specific referer.

## Tips and Gotchas

The **TabbedPanelItemReferer** is not natively supported by kivy and you might
encounter bugs and strange behaviors. Please feel free to let me know and/or
make pull requests if you do.

If you want to be able to track vparent changes:

In order to do so, you'll need to make vparent a property, as the
**TabbedPanelItemReferer** won't do it for you.

