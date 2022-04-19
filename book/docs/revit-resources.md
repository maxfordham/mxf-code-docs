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
 
![Defining property set](images/ifc_property_set_definition.PNG)

Set up in Revit's IFC exporter

![Revit IFC setup: General Tab](images/revit_general_setup.PNG)

Set up in Property sets tab.

![Revit IFC setup: Property Sets Tab](images/revit_property_sets_options.PNG)

We see that in IFC viewer that the IFC properties within the property set are not overwritten.
The user defined property we defined in the property set txt file is added.

![Property set in IFC viewer](images/propertyset_in_ifc_viewer.PNG)

However, when looking at a Space, we see that the "Name" property is used multiple times for the different property sets.

![Property sets for space in IFC viewer](images/psets_for_space_in_viewer.PNG)

Maybe it would be best to create user-defined property sets based off of the IFC property sets and extend them with the properties we wish.


