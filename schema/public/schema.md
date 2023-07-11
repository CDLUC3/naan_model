# PublicNAAN

- [1. Property `PublicNAAN > what`](#what)
- [2. Property `PublicNAAN > where`](#where)
- [3. Property `PublicNAAN > target`](#target)
- [4. Property `PublicNAAN > when`](#when)
- [5. Property `PublicNAAN > who`](#who)
  - [5.1. Property `PublicNAAN > who > name`](#who_name)
  - [5.2. Property `PublicNAAN > who > acronym`](#who_acronym)
    - [5.2.1. Property `PublicNAAN > who > acronym > anyOf > item 0`](#who_acronym_anyOf_i0)
    - [5.2.2. Property `PublicNAAN > who > acronym > anyOf > item 1`](#who_acronym_anyOf_i1)
- [6. Property `PublicNAAN > na_policy`](#na_policy)
  - [6.1. Property `PublicNAAN > na_policy > orgtype`](#na_policy_orgtype)
  - [6.2. Property `PublicNAAN > na_policy > policy`](#na_policy_policy)
  - [6.3. Property `PublicNAAN > na_policy > tenure`](#na_policy_tenure)
  - [6.4. Property `PublicNAAN > na_policy > policy_url`](#na_policy_policy_url)
    - [6.4.1. Property `PublicNAAN > na_policy > policy_url > anyOf > item 0`](#na_policy_policy_url_anyOf_i0)
    - [6.4.2. Property `PublicNAAN > na_policy > policy_url > anyOf > item 1`](#na_policy_policy_url_anyOf_i1)
- [7. Property `PublicNAAN > alternate_who`](#alternate_who)
  - [7.1. Property `PublicNAAN > alternate_who > anyOf > PublicNAAN_who`](#alternate_who_anyOf_i0)
  - [7.2. Property `PublicNAAN > alternate_who > anyOf > item 1`](#alternate_who_anyOf_i1)
- [8. Property `PublicNAAN > test_identifier`](#test_identifier)
- [9. Property `PublicNAAN > service_provider`](#service_provider)
  - [9.1. Property `PublicNAAN > service_provider > anyOf > item 0`](#service_provider_anyOf_i0)
  - [9.2. Property `PublicNAAN > service_provider > anyOf > item 1`](#service_provider_anyOf_i1)
- [10. Property `PublicNAAN > purpose`](#purpose)




**Title:** PublicNAAN

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |




| Property                                 | Pattern | Type        | Deprecated | Definition                | Title/Description |
| ---------------------------------------- | ------- | ----------- | ---------- | ------------------------- | ----------------- |
| + [what](#what )                         | No      | string      | No         | -                         | What              |
| + [where](#where )                       | No      | string      | No         | -                         | Where             |
| + [target](#target )                     | No      | object      | No         | -                         | Target            |
| + [when](#when )                         | No      | string      | No         | -                         | When              |
| + [who](#who )                           | No      | object      | No         | In #/$defs/PublicNAAN_who | -                 |
| + [na_policy](#na_policy )               | No      | object      | No         | In #/$defs/NAAN_how       | -                 |
| - [alternate_who](#alternate_who )       | No      | Combination | No         | -                         | -                 |
| - [test_identifier](#test_identifier )   | No      | string      | No         | -                         | Test Identifier   |
| - [service_provider](#service_provider ) | No      | Combination | No         | -                         | Service Provider  |
| - [purpose](#purpose )                   | No      | string      | No         | -                         | Purpose           |








## <a name="what"></a>1. Property `PublicNAAN > what`




**Title:** What

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** The NAAN value, e.g. 12345 as a string.











## <a name="where"></a>2. Property `PublicNAAN > where`




**Title:** Where

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** URL of service endpoint accepting ARK identifiers.











## <a name="target"></a>3. Property `PublicNAAN > target`




**Title:** Target

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |


**Description:** Dict of media-type = URL of service endpoints accepting ARK identifiers including substitution parameters `$arkpid` for full ARK or `$pid` for NAAN/suffix. A key of `DEFAULT`is used if no other keys match a requested media-type.











## <a name="when"></a>4. Property `PublicNAAN > when`




**Title:** When

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |


**Description:** Date when this record was last modified.











## <a name="who"></a>5. Property `PublicNAAN > who`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/$defs/PublicNAAN_who                                                    |







| Property                   | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [name](#who_name )       | No      | string      | No         | -          | Name              |
| - [acronym](#who_acronym ) | No      | Combination | No         | -          | Acronym           |








### <a name="who_name"></a>5.1. Property `PublicNAAN > who > name`




**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Official organization name











### <a name="who_acronym"></a>5.2. Property `PublicNAAN > who > acronym`




**Title:** Acronym

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** Optional display acronym derived from DNS name




| Any of(Option)                  |
| ------------------------------- |
| [item 0](#who_acronym_anyOf_i0) |
| [item 1](#who_acronym_anyOf_i1) |


#### <a name="who_acronym_anyOf_i0"></a>5.2.1. Property `PublicNAAN > who > acronym > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









#### <a name="who_acronym_anyOf_i1"></a>5.2.2. Property `PublicNAAN > who > acronym > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |


















## <a name="na_policy"></a>6. Property `PublicNAAN > na_policy`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/$defs/NAAN_how                                                          |







| Property                               | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [orgtype](#na_policy_orgtype )       | No      | string      | No         | -          | Orgtype           |
| + [policy](#na_policy_policy )         | No      | string      | No         | -          | Policy            |
| + [tenure](#na_policy_tenure )         | No      | string      | No         | -          | Tenure            |
| - [policy_url](#na_policy_policy_url ) | No      | Combination | No         | -          | Policy Url        |








### <a name="na_policy_orgtype"></a>6.1. Property `PublicNAAN > na_policy > orgtype`




**Title:** Orgtype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Organization type, FP = For profit, NP = Not for profit.











### <a name="na_policy_policy"></a>6.2. Property `PublicNAAN > na_policy > policy`




**Title:** Policy

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Which practices do you plan to implement when you assign the base name of your ARKs? The ARK base name is between your NAAN and any suffix; for example, in ark:12345/x6np1wh8k/c3.xsl the base name is x6np1wh8k. This information can help others make the best use of your ARKs. Please submit updates as your practices evolve. 
'''
NR = No re-assignment. Once a base identifier-to-object association
     has been made public, that association shall remain unique into
     the indefinite future.
OP = Opacity. Base identifiers shall be assigned with no widely
     recognizable semantic information.
CC = A check character is generated in assigned identifiers to guard
     against common transcription errors.
'''












### <a name="na_policy_tenure"></a>6.3. Property `PublicNAAN > na_policy > tenure`




**Title:** Tenure

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** <start year YYYY of role tenure>[-<end of tenure> ]











### <a name="na_policy_policy_url"></a>6.4. Property `PublicNAAN > na_policy > policy_url`




**Title:** Policy Url

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** URL to narrative policy statement




| Any of(Option)                           |
| ---------------------------------------- |
| [item 0](#na_policy_policy_url_anyOf_i0) |
| [item 1](#na_policy_policy_url_anyOf_i1) |


#### <a name="na_policy_policy_url_anyOf_i0"></a>6.4.1. Property `PublicNAAN > na_policy > policy_url > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









#### <a name="na_policy_policy_url_anyOf_i1"></a>6.4.2. Property `PublicNAAN > na_policy > policy_url > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |


















## <a name="alternate_who"></a>7. Property `PublicNAAN > alternate_who`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |






| Any of(Option)                            |
| ----------------------------------------- |
| [PublicNAAN_who](#alternate_who_anyOf_i0) |
| [item 1](#alternate_who_anyOf_i1)         |


### <a name="alternate_who_anyOf_i0"></a>7.1. Property `PublicNAAN > alternate_who > anyOf > PublicNAAN_who`


|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [who](#who)                                                               |




### <a name="alternate_who_anyOf_i1"></a>7.2. Property `PublicNAAN > alternate_who > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="test_identifier"></a>8. Property `PublicNAAN > test_identifier`




**Title:** Test Identifier

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `null`   |


**Description:** A specific, concrete ARK that you plan to support and that you will permit us touse periodically for testing service availability.











## <a name="service_provider"></a>9. Property `PublicNAAN > service_provider`




**Title:** Service Provider

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** A "service provider" is different from the NAAN holder organization. It provides technical assistance to the the NAAN organization such as content hosting, access, discovery, etc.




| Any of(Option)                       |
| ------------------------------------ |
| [item 0](#service_provider_anyOf_i0) |
| [item 1](#service_provider_anyOf_i1) |


### <a name="service_provider_anyOf_i0"></a>9.1. Property `PublicNAAN > service_provider > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









### <a name="service_provider_anyOf_i1"></a>9.2. Property `PublicNAAN > service_provider > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="purpose"></a>10. Property `PublicNAAN > purpose`




**Title:** Purpose

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"unspecified"` |


**Description:** What are you planning to assign ARKs to using the requested NAAN?Options: documents(text or page images, eg, journal articles, technical reports); audio - and / or video - based objects; non-text, non-audio / visual documents(eg, maps, posters, musical scores); datasets (eg, spreadsheets, collections of spreadsheets); records (eg, bibliographic records, archival finding aids); physical objects(eg, fine art, archaeological artifacts, scientific samples)concepts (eg, vocabulary terms, disease codes); agents (people, groups, and institutions as actors, eg, creators, contributors, publishers, performers, etc); other; unspecified; 










----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-07-11 at 10:54:22 -0400
