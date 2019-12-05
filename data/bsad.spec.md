In addition to the requirements of the JSON schema [bsad.schema.json]() _BSAD_
files must fulfil the ones specified the in this document.

## Specification
Due to limitations in the file format, some hard restrictions cannot be
practially specified by a JSON schema. These restriction must still be followed
and are listed below.
* The `tables` object must contain least one table for each of the phases
  _climb_, _cruise_ and _descent_.
* Each table must contain a specific set of columns depending on its
  `Datawealth`.
* Each of the columns requires a specific unit.

The following sections describes these restrictions more in depth.

### Datawealths
The `Datawealth` label included in the the header for each table has more
meaning than the schema implies. Each _datawealth_ corresponds to a set of
columns that __must__ be included in the data. The tables below describes the
data requirements for each _phase_ and _datawealth_.

#### Climb/Descent

| __RICH1__ | __RICH2__ | __RICH3__ | __POOR1__ | __POOR2__ |
| --------- | --------- | --------- | --------- | --------- |
| DISA      | DISA      | DISA      | DISA      | DISA      |
| ALTITUDE  | ALTITUDE  | ALTITUDE  | ALTITUDE  | ALTITUDE  |
| MASS      | MASS      | MASS      | MASS      | MASS      |
| MACH      | MACH      | MACH      | TIME      | TIME      |
| FUELFLOW  | FUELFLOW  | FUELFLOW  | FUEL      | FUEL      |
| THRUST    | THRUST    | ROC       | ROC       | DISTANCE  |
| DRAG      |           |           | DISTANCE  | CAS       |
|           |           |           | CAS       |           |

#### Cruise

| __RICH1__ | __RICH2__ |
| --------- | --------- |
| DISA      | DISA      |
| ALTITUDE  | ALTITUDE  |
| MASS      | MASS      |
| FUELFLOW  | FUELFLOW  |
| MACH      | TAS       |
| DRAG      |           |

#### Testdata

| __TESTPROFILE__ |
| --------------- |
| ALTITUDE        |
| MASS            |
| TIME            |
| FUEL            |
| DISTANCE        |
| MACH            |

#### Limits

| __BUFFETING__ |
| ------------- |
| ALTITUDE      |
| MASS          |
| MACH          |

### Column names & Units
The allowed columns names and units and the mapping between them are described
by the table below.

| Column   | Unit | Description |
| -------- | ---- | ----------- |
| DISA     | C    | ISA temperature deviation in Celsius. |
| ALTITUDE | ft   | Pressure altitude in feet. |
| MASS     | kg   | Mass in kilograms. |
| MACH     | ""   | Mach number. Dimensionless units are left blank. |
| FUELFLOW | kg/s | Fuel flow in kilograms per second. |
| DRAG     | N    | Drag, in newton. |
| THRUST   | N    | Thrust, in newton. |
| TAS      | kt   | True airspeed in knots. |
| TIME     | s    | Time, in seconds. Only available if integrated data. |
| FUEL     | kg   | Fuel, in kilograms. Only available if integrated data. |
| DISTANCE | m    | Distance, in metres. Only available if integrated data. |
| CAS      | kt   | Calibrated airspeed, in knots. |
| ROC      | m/s  | Rate of climb, in meters per second. Must be positive for the climb, negative for the descent. |
