
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;


namespace EnergyTracker.Models.SchemaModels
{
    [DisplayName("Project")]
    public class ProjectUnit
    {
        [Key]
        [Required]
        [DisplayName("Project Id")]
        public Guid ProjectId { get; set; }

        [Required]
        [DisplayName("Public project?")]
        [Description("If the project's data is publicly available for benchmarking and comparison")]
        public bool IsPublic { get; set; }

        [Required]
        [DisplayName("Project locked?")]
        [Description("If the project's data is locked, it can no longer be edited")]
        public bool IsLocked { get; set; }

        [Required]
        [DisplayName("Client/common name")]
        [Description("The client or common name for the project")]
        public string ClientName { get; set; }

        [DisplayName("Your reference code")]
        [Description("Your internal reference code for this project")]
        public string YourReferenceCode { get; set; }

        [DisplayName("Project aliases")]
        [Description("Your aliases for the project")]
        public List<string> Aliases { get; set; }

        [Description("A list of contributors and viewers for this project")]
        public List<ProjectCollaboratorUnit> Collaborators { get; set; }

        [Required]
        [DisplayName("Handover date")]
        public DateTime HandoverDate { get; set; }

        [DisplayName("Environmental strategy")]
        [Description("See /Lookups/EnvironmentalStrategies")]
        public string EnvironmentalStrategy { get; set; }

        [Required]
        [DisplayName("Gross Internal Area (GIA)")]
        [Description("The GIA for the entire project footprint. Unit: m2")]
        public decimal GrossInternalFloorArea { get; set; }

        [Required]
        [DisplayName("Sessions")]
        public List<SessionUnit> Sessions { get; set; } = new List<SessionUnit>();

        [Description("The individual buildings or structure groups that make up the project.")]
        public List<StructureUnit> Structures { get; set; } = new List<StructureUnit>();

        [Required]
        [Description("Based on CIBSE Guide F. See /Lookups/Sectors")]
        public List<string> Sectors { get; set; } = new List<string>();

        [Required]
        [Description("Based on CIBSE Guide F. See /Lookups/Types. Types that do not belong to the sectors selected will not be displayed.")]
        public List<string> Types { get; set; } = new List<string>();

        [Description("All the tags applied to this project")]
        public List<string> Tags { get; set; } = new List<string>();
    }


    public class ProjectCollaboratorUnit
    {
        [Required]
        [DisplayName("Collaborator Id")]
        [Description("The id for the user or company collaborating on the project")]
        public Guid CollaboratorId { get; set; }

        [Required]
        [DisplayName("Name")]
        public string CollaboratorName { get; set; }

        [Required]
        [DisplayName("Type")]
        [Description("The type of collaborator. See /lookups/collaboratorTypes")]
        public string CollaboratorType { get; set; }

        [Required]
        [DisplayName("Role")]
        [Description("The role of the collaborator. See /lookups/collaboratorRoles")]
        public string RoleOnProject { get; set; }

        [DisplayName("Collaborator Reference")]
        public string CollaboratorReferenceForProject { get; set; }

        [Required]
        [DisplayName("Added On")]
        public DateTime AddedOn { get; set; }

        [Required]
        [Description("The maximum level of access this collaborator has to the project. See /security for more details")]
        [DisplayName("Base Access Level")]
        public string BaseAccessLevel { get; set; }

        [Required]
        [DisplayName("Project creator?")]
        public bool IsCreator { get; set; }
    }

    public class StructureUnit
    {
        [Key]
        [Required]
        [DisplayName("Structure id")]
        public Guid StructureId { get; set; }

        [Required]
        [DisplayName("Name")]
        public string StructureName { get; set; } = "";

        [Required]
        [DisplayName("Gross Internal Area (GIA)")]
        [Description("The Gross Internal Area for this structure")]
        public decimal StructureGIA { get; set; } = 0;

        [Required]
        [Description("Occupancy")]
        public int Occupancy { get; set; } = 0;

        [Description("Based on CIBSE Guide F. See /Lookups/Sectors")]
        public List<string> Sectors { get; set; } = new List<string>();

        [Description("Based on CIBSE Guide F. See /Lookups/Types. Types that do not belong to the sectors selected will not be displayed.")]
        public List<string> Types { get; set; } = new List<string>();

        [Description("All the tags applied to this structure")]
        public List<string> Tags { get; set; } = new List<string>();
    }


    public class SessionUnit
    {
        [Key]
        [Required]
        public Guid SessionId { get; set; }

        [Required]
        [DisplayName("Session date")]
        public DateTime SessionDate { get; set; }

        [Required]
        [DisplayName("Gross Internal Area (GIA)")]
        [Description("Overriden by structure GIA, if supplied")]
        public decimal GrossInternalFloorArea { get; set; }

        [Required]
        [DisplayName("Occupancy")]
        [Description("Estimated or actual building occupancy")]
        public decimal Occupancy { get; set; }


        [DisplayName("Session Structure (optional)")]
        [Description("If supplied, provides occupancy and GIA")]
        public Guid? StructureId { get; set; }

        [Required]
        [Description("See /lookups/ReadingMethodologies")]
        public string Methodology { get; set; }

        [Required]
        [Description("See /lookups/Workstages")]
        public string Workstage { get; set; }

        [DisplayName("Calculation Software")]
        public string CalculationSoftware { get; set; }
        public string Notes { get; set; }

        [Required]
        [Description("Unit: kWh/m2.y")]
        [DisplayName("Total Annual Electricity Use")]
        public decimal TotalAnnualElectricityUse { get; set; }

        [Required]
        [Description("Unit: kWh/m2.y")]
        [DisplayName("Total Non-Electric Energy Use")]
        public decimal TotalNonElectricEnergyUse { get; set; }

        [Required]
        [Description("Unit: kWh/m2.y")]
        [DisplayName("Total Renewable Contribution")]
        public decimal TotalRenewableContribution { get; set; }

        [Required]
        [Description("Unit: kWh/m2.y")]
        [DisplayName("Operational Energy Total")]
        public decimal OperationalEnergyTotal { get; set; }

        [Required]
        [Description("Unit: kgCO2e")]
        [DisplayName("Operational Energy Carbon")]
        public decimal OperationalEnergyCarbon { get; set; }

        [DisplayName("Operational Energy Breakdown (optional)")]
        public OperationalEnergyBreakdown OperationalEnergyBreakdown { get; set; }

        [Required]
        [Description("Unit: kgCO2e")]
        [DisplayName("Total Embodied Carbon")]
        public decimal TotalEmbodiedCarbon { get; set; }

        [DisplayName("Embodied Carbon Breakdown (optional)")]
        public EmbodiedCarbonBreakdown EmbodiedCarbonBreakdown { get; set; }

        [Required]
        [Description("Unit: m3")]
        [DisplayName("Potable water use")]
        public decimal PotableWaterUse { get; set; }

        [Required]
        [DisplayName("Carbon factors")]
        public CarbonFactorUnit CarbonFactors { get; set; }
    }

    public class OperationalEnergyBreakdown
    {
        public List<OperationalEnergySection> Sections { get; set; }
    }

    public class OperationalEnergySection
    {

        [DisplayName("Section name")]
        public string SectionName { get; set; }

        [Description("Custom components are only valid in sections where this is true")]
        [DisplayName("Custom Comnponents Allowed")]
        public bool AllowsCustomComponents { get; set; }

        public List<OperationalEnergyComponent> Components { get; set; }
    }

    public class OperationalEnergyComponent
    {
        [Required]
        [DisplayName("Component name")]
        public string ComponentName { get; set; }

        [Required]
        public Unit Units { get; set; }

        [Required]
        [DisplayName("Component value")]
        public decimal ComponentValue { get; set; }

        [Required]
        [DisplayName("Generates power")]
        public bool GeneratesPower { get; set; } = false;

        [Description("Optional. See /lookups/FuelTypes. The mix total must equal 100%")]
        public List<Fuel> FuelMix { get; set; }
    }

    public class Unit
    {
        [Required]
        [DisplayName("Unit")]
        public string UnitString { get; set; }
    }

    public class Fuel
    {
        [Required]
        [DisplayName("Fuel Name")]
        public string FuelName { get; set; }

        [Required]
        [DisplayName("Percentage of total")]
        public decimal PercentageOfTotal { get; set; }
    }

    public class EmbodiedCarbonBreakdown
    {

        [Required]
        [DisplayName("Section Name")]
        public string SectionName { get; set; }

        [Description("You can only add custom components to sections where this is true")]
        public bool AllowsCustomComponents { get; set; }
        public List<EmbodiedCarbonComponent> Components { get; set; }
    }

    public class EmbodiedCarbonComponent
    {

        [Required]
        [DisplayName("Component Name")]
        public string ComponentName { get; set; }

        [Required]
        public Unit Units { get; set; }


        [Required]
        [DisplayName("Component Value")]
        public decimal ComponentValue { get; set; }


        [Required]
        [DisplayName("Sequesters Carbon")]
        public bool SequestersCarbon { get; set; } = false;

    }

    public class CarbonFactorUnit
    {
        [Required]
        [DisplayName("Electricity Carbon Factor")]
        public decimal ElectricityCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Electricity Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string ElectricityMethodology { get; set; }

        [Required]
        [DisplayName("Gas Carbon Factor")]
        public decimal GasCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Gas Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string GasMethodology { get; set; }

        [Required]
        [DisplayName("Oil Carbon Factor")]
        public decimal OilCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Oil Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string OilMethodology { get; set; }

        [Required]
        [DisplayName("Biodiesel Carbon Factor")]
        public decimal BiodieselFromBiomassCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Biodiesel Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string BiodieselMethodology { get; set; }

        [Required]
        [DisplayName("Coal Carbon Factor")]
        public decimal CoalCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Coal Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string CoalMethodology { get; set; }

        [Required]
        [DisplayName("Biomass Carbon Factor")]
        public decimal BiomassCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Biomass Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string BiomassMethodology { get; set; }

        [Required]
        [DisplayName("Biogas Carbon Factor")]
        public decimal BiogasCarbonFactor { get; set; } = 0;

        [Required]
        [DisplayName("Biogas Carbon Methodology")]
        [Description("Default is derived from SAP10.1 for the session year")]
        public string BiogasMethodology { get; set; }

    }
}
