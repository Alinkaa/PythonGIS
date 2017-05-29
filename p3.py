import arcpy
import os
arcpy.env.workspace = r'C:\Users\S1mple\Desktop\arcpy\PythEveryone10_1\3\p3'
arcpy.env.overwriteOutput = True
amenities = ['school','hospital','place_of_worship']
country = 'El Salvador'
arcpy.MakeFeatureLayer_management('CentralAmerica.shp','temply','"NAME" =  ' +"'"+country
                                  +"'")
arcpy.Clip_analysis('OSMpoints.shp','temply','clip.shp')
arcpy.CreateFileGDB_management(arcpy.env.workspace,'yourGDB.gdb')
for i in amenities:
    name='point'+i
    arcpy.MakeFeatureLayer_management('clip.shp',name,'"amenity" =  ' +"'"+i+"'")
    arcpy.CopyFeatures_management('point'+i,arcpy.env.workspace+r'\yourGDB.gdb'+r'\point'+i)
    arcpy.AddField_management('yourGDB.gdb\\'+'point'+i,'source',"TEXT")
    arcpy.AddField_management('yourGDB.gdb\\'+'point'+i,'GID',"DOUBLE")
    #arcpy.AlterField_management('yourGDB.gdb\\'+'point'+i,'id','GID')
