"""
Split a mesh by connectivity and order the pieces
by increasing area.
"""
print(__doc__)
from vtkplotter import splitByConnectivity, load, show, datadir

em = load(datadir+"embryo.tif", threshold=80)

# return the list of the largest 10 connected meshes:
splitem = splitByConnectivity(em, maxdepth=40)[0:9]

splitem[0].alpha(0.5).phong()  # make the largest part transparent

show([em, splitem], N=2, axes=1)
