"""
Example of drawing objects on different windows
and/or subwindows within the same window.
We split the main window in a 25 subwindows and draw something
in specific windows numbers.
Then open an independent window and draw a shape on it.
"""
print(__doc__)

from vtkplotter import Plotter, Text, datadir


# this is one instance of the class Plotter with 5 raws and 5 columns
vp1 = Plotter(shape=(5, 5), axes=0, bg="white")
# having set shape=(n,m), script execution after the show() is not held

# set a different background color for a specific subwindow (the last one)
vp1.renderers[24].SetBackground(0.8, 0.9, 0.9)  # use vtk method SetBackground()

# load the actors and give them a name
a = vp1.load(datadir+"airboat.vtk").legend("some legend")
b = vp1.load(datadir+"cessna.vtk", c="red")
c = vp1.load(datadir+"atc.ply")

# show a text in each renderer
for i in range(25):
    txt = Text("renderer\nnr."+str(i), c='k', s=0.5, font='arial')
    vp1.show(txt, at=i, interactive=0)

vp1.show(a, at=22)
vp1.show(b, at=23)
vp1.show(c, at=24, interactive=0)


############################################################
# declare a second independent instance of the class Plotter
vp2 = Plotter(pos=(500, 250), bg=(0.9, 0.9, 1))  # blue-ish background

vp2.load(datadir+"porsche.ply").legend("an other window")

vp2.show()  # show and interact with mouse and keyboard
