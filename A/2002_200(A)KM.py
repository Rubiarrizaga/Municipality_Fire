import arcpy
from arcpy import env 
env.workspace = r"C:/Com_cent_fin/2002-2003"
#Para crear el buffer
puntos = r"C:/Com_cent_fin/2002-2003/RP_2002-2003(A).shp"
buffer = r"C:/Com_cent_fin/2002-2003\buffer_200KM(A).shp"
distance = "200 Kilometers"
tipo_buffer = "PLANAR"

arcpy.Buffer_analysis(
    in_features= puntos,
    out_feature_class= buffer,
    buffer_distance_or_field=distance,
    method=tipo_buffer
)
print("Buffer Creado")
#para crear el Spatial Join
muni = r"C:/Com_cent_fin/municipios_sirgas-chile_gcs_v030120/MUNICIPIOS_SIRGAS-CHILE_GCS_V0301.shp"
buffer = r"C:/Com_cent_fin/2002-2003\buffer_200KM(A).shp"
out_fc= r"C:/Com_cent_fin/2002-2003\SJ_200KM(A).shp"

arcpy.SpatialJoin_analysis(
    target_features=muni,
    join_features=buffer,
    out_feature_class=out_fc,
    join_operation= "JOIN_ONE_TO_MANY",
    match_option = "INTERSECT"
   #search_radius=200000,
)
print("SJ Creado")

#Borrar los ID vacios del J_20KM.shp...
#in_features = r"C:/Com_cent_fin/2002-2003\SJ_200KM.shp"
#out_feature_class  = r"C:/Com_cent_fin/2002-2003\SJ_200KM_select.shp"
#where_clause = '"X_1" <> 0'
#arcpy.Select_analysis(in_features, out_feature_class , where_clause)
#print("seleccionado")
#XY To Line (para crear las lineas)
#arcpy.XYToLine_management(in_table=r"C:/Com_cent_fin/2002-2003\SJ_200KM_select.shp", out_featureclass=r"C:/Com_cent_fin/2002-2003\vect_200KM.shp", startx_field="X_1", starty_field="Y_1", endx_field="POINT_X_1", endy_field="POINT_Y_1")
#print("vectores creados")

#Para calcular la distancia o medida de la linea
#arcpy.AddField_management(in_table=r"C:/Com_cent_fin/2002-2003\vect_200KM.shp", field_name="LENGTH", field_type="DOUBLE") 
#print("vector agregado")
#arcpy.CalculateField_management(in_table=r"C:/Com_cent_fin/2002-2003\vect_200KM.shp", field="LENGTH", expression="!SHAPE.LENGTH!", expression_type="PYTHON_9.3")
#print("distancia calculada")

#Para pegar las dos tablas
#arcpy.JoinField_management(in_data=r"C:/Com_cent_fin/2002-2003\SJ_200KM_select.shp", in_field="FID", join_table=r"C:/Com_cent_fin/2002-2003\vect_200KM.shp", join_field="FID")
#print("tablas pegadas")

#Agregar el codigo de angulos

#Borrar columnas
#arcpy.env.workspace = r"C:/Com_cent_fin/2002-2003"
#inFeatures = r"C:/Com_cent_fin/2002-2003\SJ_120KM_select.shp"
#outFeatureClass = r"C:/Com_cent_fin/2002-2003\v2014a2015_120KM.shp"
#dropFields = ["COD_REG", "Join_Count", "NOM_REG", "COD_REG", "NOM_PROV", "COD_PROV", "Escenario", "POINT_X_1", "POINT_Y_1","la1_1", "lo1_1"]
#arcpy.CopyFeatures_management(inFeatures, outFeatureClass)
#arcpy.DeleteField_management(outFeatureClass, dropFields)
#print("columnas borradas")