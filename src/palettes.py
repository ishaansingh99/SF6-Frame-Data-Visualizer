from PySide6.QtGui import QPalette, QColor, QBrush
from PySide6 import QtGui

# General idea:
# Use palette for general coloring
# Main menu buttons have images and will require specific coloring in stylesheets
# Style sheets will be used for shaping and stuff

# Main menu palette
mmb_gradient = QtGui.QRadialGradient(0.5, 0.5, 1, 0.5, 0.5)
mmb_gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectMode)
mmb_gradient.setColorAt(0, QColor.fromRgb(0, 0, 0, 255))
mmb_gradient.setColorAt(1, QColor.fromRgb(57, 0, 171, 255))

# Char window palette
cw_gradient = QtGui.QRadialGradient(0.5, 0.5, 1, 0.5, 0.5)
cw_gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectMode)
cw_gradient.setColorAt(0, QColor.fromRgb(135, 135, 135, 255))
cw_gradient.setColorAt(1, QColor.fromRgb(71, 71, 69, 255))

# Char window num buttons
num_gradient = QtGui.QRadialGradient(0.5,0.5,1,0.5,0.5)
num_gradient.setColorAt(0, QColor.fromRgb(15, 18, 17, 255))
num_gradient.setColorAt(1, QColor.fromRgb(71, 71, 69, 255))

# # Char window attack buttons
# num_gradient = QtGui.QRadialGradient(0.5,0.5,1,0.5,0.5)
# num_gradient.setColorAt(0, QColor.fromRgb(15, 18, 17, 255))
# num_gradient.setColorAt(1, QColor.fromRgb(71, 71, 69, 255))

# Set palettes
mm_palette = QPalette()
mm_palette.setBrush(QPalette.ColorRole.Window,QBrush(mmb_gradient))
# palette.setBrush(QPalette.ColorRole.Button,brush2)

cw_palette = QPalette()
cw_palette.setBrush(QPalette.ColorRole.Window,QBrush(cw_gradient))
cw_palette.setBrush(QPalette.ColorRole.Button,QBrush(num_gradient))
cw_palette.setColor(QPalette.ColorRole.ButtonText,QColor("white"))