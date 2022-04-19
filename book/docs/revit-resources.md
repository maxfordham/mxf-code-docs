# Revit Resources

exporting to IFC 

- [exporting-ifc-from-revit-part-3-user-defined-properties](https://bimcorner.com/exporting-ifc-from-revit-part-3-user-defined-properties/)


## Exporting to IFC with Units

- [](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2_TC1/HTML/link/project-units.htm)
- [](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/annex/annex-e/basic-unit-declaration.htm)
- [](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/ifcmeasureresource/content.htm)


## Adding conversion to a unit
- [](https://standards.buildingsmart.org/IFC/RELEASE/IFC2x/ADD1/HTML/ifcmeasureresource/IFC_R2X_UnitsMeasures_Examples.htm)

## Custom PropertySets vs Extending PropertySets

Defining property set in user defined property sets txt file.
 
![Defining property set](images/ifc_property_set_definition.png)

Set up in Revit's IFC exporter

![Revit IFC setup: General Tab](images/revit_general_setup.png)

Set up in Property sets tab.

![Revit IFC setup: Property Sets Tab](images/revit_property_sets_options.png)

We see that in IFC viewer that the IFC properties within the property set are not overwritten.
The user defined property we defined in the property set txt file is added.

![Property set in IFC viewer](images/propertyset_in_ifc_viewer.png)




