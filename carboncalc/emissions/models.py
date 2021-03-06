# Copied in from autogenerated model, slightly tweaked.
# Defines object-relational classes for data tables in emissions database.

from __future__ import unicode_literals

from django.db import models

class AppsMax(models.Model):
    cz = models.TextField(blank=True, null=True)
    sp_code = models.TextField(blank=True, null=True)
    dbh_in = models.FloatField(blank=True, null=True)
    height_ft = models.FloatField(blank=True, null=True)
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'apps_max'


class AzimuthClasses(models.Model):
    azimuth_class = models.IntegerField(primary_key=True, blank=True, null=False)
    degree = models.TextField(blank=True, null=True)
    degree_start = models.FloatField(blank=True, null=True)
    degree_end = models.FloatField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'azimuth_classes'


class BuildingClasses(models.Model):
    distance_ft_field = models.TextField(db_column='distance__ft_', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    distance_start = models.FloatField(blank=True, null=True)
    distance_end = models.IntegerField(blank=True, null=True)
    class_field = models.IntegerField(primary_key=True, db_column='class', blank=True, null=False)  # Field renamed because it was a Python reserved word.
    class_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'building_classes'


class CzLookup(models.Model):
    cz = models.TextField(primary_key=True, blank=True, null=False)
    abbrev = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cz_lookup'


class DbhClasses(models.Model):
    dbh_inch_start = models.FloatField(blank=True, null=True)
    dbh_inch_end = models.IntegerField(blank=True, null=True)
    dbh_class = models.IntegerField(primary_key=True, blank=True, null=False)
    mid = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbh_classes'


class DbhClassesInterp(models.Model):
    midlowfake = models.FloatField(blank=True, null=True)
    midhighfake = models.FloatField(blank=True, null=True)
    midlow = models.FloatField(blank=True, null=True)
    midhigh = models.FloatField(blank=True, null=True)
    class_low = models.FloatField(blank=True, null=True)
    class_high = models.FloatField(blank=True, null=True)
    palm_low_ft = models.FloatField(blank=True, null=True)
    palm_high_ft = models.FloatField(blank=True, null=True)
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'dbh_classes_interp'


class EmisFactorsCooling(models.Model):
    climate_region = models.TextField(db_column='Climate_region', blank=True, null=True)  # Field name made lowercase.
    cz = models.TextField(primary_key=True, blank=True, null=False)
    reference_city = models.TextField(db_column='Reference_City', blank=True, null=True)  # Field name made lowercase.
    co2_avg_emis_factor_kg_mwh_field = models.FloatField(db_column='CO2_Avg_Emis_Factor__kg_MWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    co2_avg_emis_factor_kg_kwh_field = models.FloatField(db_column='CO2_Avg_Emis_Factor__kg_kWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    methane_avg_emis_factor_kg_mwh_field = models.FloatField(db_column='Methane_Avg_Emis_Factor__kg_MWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    methane_avg_emis_factor_kg_kwh_field = models.FloatField(db_column='Methane_Avg_Emis_Factor__kg_kWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    nitrous_oxide_avg_emis_factor_kg_mwh_field = models.FloatField(db_column='Nitrous_Oxide_Avg_Emis_Factor__kg_MWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    nitrous_oxide_avg_emis_factor_kg_kwh_field = models.FloatField(db_column='Nitrous_Oxide_Avg_Emis_Factor__kg_kWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'emis_factors_cooling'


class EmisFactorsHeating(models.Model):
    fuel_type = models.TextField(primary_key=True, db_column='Fuel_Type', blank=True, null=False)  # Field name made lowercase.
    co2_emis_factor_kg_mbtu_field = models.FloatField(db_column='CO2_emis_factor__kg_Mbtu_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    methane_emis_factor_kg_mbtu_field = models.FloatField(db_column='Methane_emis_factor__kg_Mbtu_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    nitrous_oxide_emis_factor_kg_mbtu_field = models.FloatField(db_column='Nitrous_oxide_emis_factor__kg_Mbtu_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'emis_factors_heating'


class EnergyPrices(models.Model):
    climate_zone = models.TextField(db_column='Climate_Zone', blank=True, null=True)  # Field name made lowercase.
    cz = models.TextField(primary_key=True, blank=True, null=False)
    cool_kwh_field = models.FloatField(db_column='Cool____kWh_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    heat_gj_field = models.TextField(db_column='Heat____GJ_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    heat_mbtu_field = models.FloatField(db_column='Heat____Mbtu_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    sources = models.TextField(db_column='Sources', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'energy_prices'


class Energylong2(models.Model):
    cz = models.TextField(blank=True, null=True)
    vintage = models.TextField(blank=True, null=True)
    benefit_type = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    dbh_class = models.IntegerField(blank=True, null=True)
    dist = models.TextField(blank=True, null=True)
    azimuth = models.TextField(blank=True, null=True)
    energy_reduction = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'energylong2'


class EqptReductionCooling(models.Model):
    cz = models.TextField(blank=True, null=True)
    lu = models.TextField(blank=True, null=True)
    crosswalk = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    reduction = models.TextField(blank=True, null=True)  # This field type is a guess.
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'eqpt_reduction_cooling'


class EqptReductionHeating(models.Model):
    cz = models.TextField(blank=True, null=True)
    lu = models.TextField(blank=True, null=True)
    crosswalk = models.TextField(blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    reduction = models.TextField(blank=True, null=True)  # This field type is a guess.
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'eqpt_reduction_heating'


class GlobalWarmingPotential(models.Model):
    avg_emissions_factor_type = models.TextField(primary_key=True, db_column='Avg_Emissions_Factor_Type', blank=True, null=False)  # Field name made lowercase.
    global_warming_potential = models.IntegerField(db_column='Global_Warming_Potential', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'global_warming_potential'


class GtrSlim(models.Model):
    cz = models.TextField(blank=True, null=True)
    sp_code = models.TextField(blank=True, null=True)
    growth_assign = models.TextField(blank=True, null=True)
    biomass_assign = models.TextField(blank=True, null=True)
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'gtr_slim'


class MaxCoolHeat(models.Model):
    cz = models.TextField(blank=True, null=True)
    type_max = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    vintage = models.TextField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    pkey = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'max_cool_heat'


class Palms(models.Model):
    x = models.IntegerField(primary_key=True, db_column='X', blank=True, null=False)  # Field name made lowercase.
    sp_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palms'


class SpeciesMaster(models.Model):
    datano_field = models.IntegerField(primary_key=True, db_column='datano_', blank=True, null=False)  # Field renamed because it ended with '_'.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    speciescode = models.TextField(db_column='SpeciesCode', blank=True, null=True)  # Field name made lowercase.
    genus = models.TextField(db_column='Genus', blank=True, null=True)  # Field name made lowercase.
    scientificname = models.TextField(db_column='ScientificName', blank=True, null=True)  # Field name made lowercase.
    commonname = models.TextField(db_column='CommonName', blank=True, null=True)  # Field name made lowercase.
    tree_type = models.TextField(db_column='Tree_Type', blank=True, null=True)  # Field name made lowercase.
    growth_assign = models.TextField(db_column='Growth_Assign', blank=True, null=True)  # Field name made lowercase.
    ht_ft_field = models.TextField(db_column='ht__ft_', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    cdia_ft_field = models.TextField(db_column='cdia__ft_', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    biomass_assign = models.TextField(db_column='Biomass_Assign', blank=True, null=True)  # Field name made lowercase.
    biomass_code = models.TextField(db_column='Biomass_Code', blank=True, null=True)  # Field name made lowercase.
    fol_bio_dw_fw = models.FloatField(db_column='Fol_Bio_dw_fw', blank=True, null=True)  # Field name made lowercase.
    fol_bio_kg_m2 = models.FloatField(db_column='Fol_Bio_kg_m2', blank=True, null=True)  # Field name made lowercase.
    dw_density = models.IntegerField(db_column='DW_Density', blank=True, null=True)  # Field name made lowercase.
    tree_shape = models.TextField(db_column='Tree_Shape', blank=True, null=True)  # Field name made lowercase.
    sc_code = models.TextField(db_column='SC__Code', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    grow_to_age = models.TextField(db_column='Grow_to_Age', blank=True, null=True)  # Field name made lowercase.
    h2o_stor_cap_mm_field = models.TextField(db_column='H2O_Stor_Cap__mm_', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    x_1 = models.IntegerField(db_column='X_1', blank=True, null=True)  # Field name made lowercase.
    x_2 = models.IntegerField(db_column='X_2', blank=True, null=True)  # Field name made lowercase.
    x_3 = models.IntegerField(db_column='X_3', blank=True, null=True)  # Field name made lowercase.
    x_4 = models.IntegerField(db_column='X_4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'species_master'
