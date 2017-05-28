import arcpy
from arcpy import env  
from arcpy.sa import *
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
env.workspace = r'D:\gispython\Lesson1\Lesson1'

Contour('foxlake', r'D:\gispython\Lesson1\Lesson1\foxlake2.shp', 250, 0)
arcpy.AddMessage("All done!")


