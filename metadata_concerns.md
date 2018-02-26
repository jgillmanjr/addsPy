These are concerns generated about the metadata (such as the docs or
the schema files) as I've been working on this.

## Aircraft Reports (PIREPS) ##
[Field Docs](https://aviationweather.gov/dataserver/fields?datatype=airep)

[XSD (XML Schema)](https://aviationweather.gov/docs/dataserver/schema/aircraftreport1_0.xsd)

* The documention refers to `pirep_type` for field 17. However, the XSD and actual XML specify the name as `report_type`
* The `vert_gust_kt` field indicates `m/s` for the unit.