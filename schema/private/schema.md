# NAAN

- [1. Property `NAAN > what`](#what)
- [2. Property `NAAN > where`](#where)
- [3. Property `NAAN > target`](#target)
- [4. Property `NAAN > when`](#when)
- [5. Property `NAAN > who`](#who)
  - [5.1. Property `NAAN > who > name`](#who_name)
  - [5.2. Property `NAAN > who > acronym`](#who_acronym)
    - [5.2.1. Property `NAAN > who > acronym > anyOf > item 0`](#who_acronym_anyOf_i0)
    - [5.2.2. Property `NAAN > who > acronym > anyOf > item 1`](#who_acronym_anyOf_i1)
  - [5.3. Property `NAAN > who > address`](#who_address)
- [6. Property `NAAN > na_policy`](#na_policy)
  - [6.1. Property `NAAN > na_policy > orgtype`](#na_policy_orgtype)
  - [6.2. Property `NAAN > na_policy > policy`](#na_policy_policy)
  - [6.3. Property `NAAN > na_policy > tenure`](#na_policy_tenure)
  - [6.4. Property `NAAN > na_policy > policy_url`](#na_policy_policy_url)
    - [6.4.1. Property `NAAN > na_policy > policy_url > anyOf > item 0`](#na_policy_policy_url_anyOf_i0)
    - [6.4.2. Property `NAAN > na_policy > policy_url > anyOf > item 1`](#na_policy_policy_url_anyOf_i1)
- [7. Property `NAAN > alternate_who`](#alternate_who)
  - [7.1. Property `NAAN > alternate_who > anyOf > NAAN_who`](#alternate_who_anyOf_i0)
  - [7.2. Property `NAAN > alternate_who > anyOf > item 1`](#alternate_who_anyOf_i1)
- [8. Property `NAAN > test_identifier`](#test_identifier)
- [9. Property `NAAN > service_provider`](#service_provider)
  - [9.1. Property `NAAN > service_provider > anyOf > item 0`](#service_provider_anyOf_i0)
  - [9.2. Property `NAAN > service_provider > anyOf > item 1`](#service_provider_anyOf_i1)
- [10. Property `NAAN > purpose`](#purpose)
- [11. Property `NAAN > why`](#why)
- [12. Property `NAAN > contact`](#contact)
  - [12.1. Property `NAAN > contact > anyOf > NAAN_contact`](#contact_anyOf_i0)
    - [12.1.1. Property `NAAN > contact > anyOf > NAAN_contact > name`](#contact_anyOf_i0_name)
    - [12.1.2. Property `NAAN > contact > anyOf > NAAN_contact > unit`](#contact_anyOf_i0_unit)
      - [12.1.2.1. Property `NAAN > contact > anyOf > NAAN_contact > unit > anyOf > item 0`](#contact_anyOf_i0_unit_anyOf_i0)
      - [12.1.2.2. Property `NAAN > contact > anyOf > NAAN_contact > unit > anyOf > item 1`](#contact_anyOf_i0_unit_anyOf_i1)
    - [12.1.3. Property `NAAN > contact > anyOf > NAAN_contact > tenure`](#contact_anyOf_i0_tenure)
      - [12.1.3.1. Property `NAAN > contact > anyOf > NAAN_contact > tenure > anyOf > item 0`](#contact_anyOf_i0_tenure_anyOf_i0)
      - [12.1.3.2. Property `NAAN > contact > anyOf > NAAN_contact > tenure > anyOf > item 1`](#contact_anyOf_i0_tenure_anyOf_i1)
    - [12.1.4. Property `NAAN > contact > anyOf > NAAN_contact > email`](#contact_anyOf_i0_email)
      - [12.1.4.1. Property `NAAN > contact > anyOf > NAAN_contact > email > anyOf > item 0`](#contact_anyOf_i0_email_anyOf_i0)
      - [12.1.4.2. Property `NAAN > contact > anyOf > NAAN_contact > email > anyOf > item 1`](#contact_anyOf_i0_email_anyOf_i1)
    - [12.1.5. Property `NAAN > contact > anyOf > NAAN_contact > phone`](#contact_anyOf_i0_phone)
      - [12.1.5.1. Property `NAAN > contact > anyOf > NAAN_contact > phone > anyOf > item 0`](#contact_anyOf_i0_phone_anyOf_i0)
      - [12.1.5.2. Property `NAAN > contact > anyOf > NAAN_contact > phone > anyOf > item 1`](#contact_anyOf_i0_phone_anyOf_i1)
  - [12.2. Property `NAAN > contact > anyOf > item 1`](#contact_anyOf_i1)
- [13. Property `NAAN > alternate_contact`](#alternate_contact)
  - [13.1. Property `NAAN > alternate_contact > anyOf > NAAN_contact`](#alternate_contact_anyOf_i0)
  - [13.2. Property `NAAN > alternate_contact > anyOf > item 1`](#alternate_contact_anyOf_i1)
- [14. Property `NAAN > comments`](#comments)
  - [14.1. Property `NAAN > comments > anyOf > item 0`](#comments_anyOf_i0)
    - [14.1.1. NAAN > comments > anyOf > item 0 > item 0 items](#autogenerated_heading_2)
  - [14.2. Property `NAAN > comments > anyOf > item 1`](#comments_anyOf_i1)
- [15. Property `NAAN > provider`](#provider)
  - [15.1. Property `NAAN > provider > anyOf > item 0`](#provider_anyOf_i0)
  - [15.2. Property `NAAN > provider > anyOf > item 1`](#provider_anyOf_i1)




**Title:** NAAN

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |




| Property                                   | Pattern | Type        | Deprecated | Definition          | Title/Description |
| ------------------------------------------ | ------- | ----------- | ---------- | ------------------- | ----------------- |
| + [what](#what )                           | No      | string      | No         | -                   | What              |
| + [where](#where )                         | No      | string      | No         | -                   | Where             |
| + [target](#target )                       | No      | object      | No         | -                   | Target            |
| + [when](#when )                           | No      | string      | No         | -                   | When              |
| + [who](#who )                             | No      | object      | No         | In #/$defs/NAAN_who | -                 |
| + [na_policy](#na_policy )                 | No      | object      | No         | In #/$defs/NAAN_how | -                 |
| - [alternate_who](#alternate_who )         | No      | Combination | No         | -                   | -                 |
| - [test_identifier](#test_identifier )     | No      | string      | No         | -                   | Test Identifier   |
| - [service_provider](#service_provider )   | No      | Combination | No         | -                   | Service Provider  |
| - [purpose](#purpose )                     | No      | string      | No         | -                   | Purpose           |
| - [why](#why )                             | No      | string      | No         | -                   | Why               |
| - [contact](#contact )                     | No      | Combination | No         | -                   | -                 |
| - [alternate_contact](#alternate_contact ) | No      | Combination | No         | -                   | -                 |
| - [comments](#comments )                   | No      | Combination | No         | -                   | Comments          |
| - [provider](#provider )                   | No      | Combination | No         | -                   | Provider          |








## <a name="what"></a>1. Property `NAAN > what`




**Title:** What

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** The NAAN value, e.g. 12345 as a string.











## <a name="where"></a>2. Property `NAAN > where`




**Title:** Where

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** URL of service endpoint accepting ARK identifiers.











## <a name="target"></a>3. Property `NAAN > target`




**Title:** Target

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |


**Description:** Dict of media-type = URL of service endpoints accepting ARK identifiers including substitution parameters `$arkpid` for full ARK or `$pid` for NAAN/suffix. A key of `DEFAULT`is used if no other keys match a requested media-type.











## <a name="when"></a>4. Property `NAAN > when`




**Title:** When

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |


**Description:** Date when this record was last modified.











## <a name="who"></a>5. Property `NAAN > who`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/$defs/NAAN_who                                                          |







| Property                   | Pattern | Type        | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [name](#who_name )       | No      | string      | No         | -          | Name              |
| - [acronym](#who_acronym ) | No      | Combination | No         | -          | Acronym           |
| - [address](#who_address ) | No      | string      | No         | -          | Address           |








### <a name="who_name"></a>5.1. Property `NAAN > who > name`




**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Official organization name











### <a name="who_acronym"></a>5.2. Property `NAAN > who > acronym`




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


#### <a name="who_acronym_anyOf_i0"></a>5.2.1. Property `NAAN > who > acronym > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









#### <a name="who_acronym_anyOf_i1"></a>5.2.2. Property `NAAN > who > acronym > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















### <a name="who_address"></a>5.3. Property `NAAN > who > address`




**Title:** Address

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `null`   |


**Description:** Physical address of organization












## <a name="na_policy"></a>6. Property `NAAN > na_policy`





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








### <a name="na_policy_orgtype"></a>6.1. Property `NAAN > na_policy > orgtype`




**Title:** Orgtype

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Organization type, FP = For profit, NP = Not for profit.











### <a name="na_policy_policy"></a>6.2. Property `NAAN > na_policy > policy`




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












### <a name="na_policy_tenure"></a>6.3. Property `NAAN > na_policy > tenure`




**Title:** Tenure

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** <start year YYYY of role tenure>[-<end of tenure> ]











### <a name="na_policy_policy_url"></a>6.4. Property `NAAN > na_policy > policy_url`




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


#### <a name="na_policy_policy_url_anyOf_i0"></a>6.4.1. Property `NAAN > na_policy > policy_url > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









#### <a name="na_policy_policy_url_anyOf_i1"></a>6.4.2. Property `NAAN > na_policy > policy_url > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |


















## <a name="alternate_who"></a>7. Property `NAAN > alternate_who`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |






| Any of(Option)                      |
| ----------------------------------- |
| [NAAN_who](#alternate_who_anyOf_i0) |
| [item 1](#alternate_who_anyOf_i1)   |


### <a name="alternate_who_anyOf_i0"></a>7.1. Property `NAAN > alternate_who > anyOf > NAAN_who`


|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [who](#who)                                                               |




### <a name="alternate_who_anyOf_i1"></a>7.2. Property `NAAN > alternate_who > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="test_identifier"></a>8. Property `NAAN > test_identifier`




**Title:** Test Identifier

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `null`   |


**Description:** A specific, concrete ARK that you plan to support and that you will permit us touse periodically for testing service availability.











## <a name="service_provider"></a>9. Property `NAAN > service_provider`




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


### <a name="service_provider_anyOf_i0"></a>9.1. Property `NAAN > service_provider > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









### <a name="service_provider_anyOf_i1"></a>9.2. Property `NAAN > service_provider > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="purpose"></a>10. Property `NAAN > purpose`




**Title:** Purpose

|              |                 |
| ------------ | --------------- |
| **Type**     | `string`        |
| **Required** | No              |
| **Default**  | `"unspecified"` |


**Description:** What are you planning to assign ARKs to using the requested NAAN?Options: documents(text or page images, eg, journal articles, technical reports); audio - and / or video - based objects; non-text, non-audio / visual documents(eg, maps, posters, musical scores); datasets (eg, spreadsheets, collections of spreadsheets); records (eg, bibliographic records, archival finding aids); physical objects(eg, fine art, archaeological artifacts, scientific samples)concepts (eg, vocabulary terms, disease codes); agents (people, groups, and institutions as actors, eg, creators, contributors, publishers, performers, etc); other; unspecified; 











## <a name="why"></a>11. Property `NAAN > why`




**Title:** Why

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"ARK"`  |


**Description:** Purpose for this record, 'ARK'











## <a name="contact"></a>12. Property `NAAN > contact`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |






| Any of(Option)                    |
| --------------------------------- |
| [NAAN_contact](#contact_anyOf_i0) |
| [item 1](#contact_anyOf_i1)       |


### <a name="contact_anyOf_i0"></a>12.1. Property `NAAN > contact > anyOf > NAAN_contact`


|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/$defs/NAAN_contact                                                      |







| Property                              | Pattern | Type        | Deprecated | Definition | Title/Description |
| ------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [name](#contact_anyOf_i0_name )     | No      | string      | No         | -          | Name              |
| - [unit](#contact_anyOf_i0_unit )     | No      | Combination | No         | -          | Unit              |
| - [tenure](#contact_anyOf_i0_tenure ) | No      | Combination | No         | -          | Tenure            |
| - [email](#contact_anyOf_i0_email )   | No      | Combination | No         | -          | Email             |
| - [phone](#contact_anyOf_i0_phone )   | No      | Combination | No         | -          | Phone             |








#### <a name="contact_anyOf_i0_name"></a>12.1.1. Property `NAAN > contact > anyOf > NAAN_contact > name`




**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |


**Description:** Name of contact











#### <a name="contact_anyOf_i0_unit"></a>12.1.2. Property `NAAN > contact > anyOf > NAAN_contact > unit`




**Title:** Unit

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** Name of contact organization




| Any of(Option)                            |
| ----------------------------------------- |
| [item 0](#contact_anyOf_i0_unit_anyOf_i0) |
| [item 1](#contact_anyOf_i0_unit_anyOf_i1) |


##### <a name="contact_anyOf_i0_unit_anyOf_i0"></a>12.1.2.1. Property `NAAN > contact > anyOf > NAAN_contact > unit > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









##### <a name="contact_anyOf_i0_unit_anyOf_i1"></a>12.1.2.2. Property `NAAN > contact > anyOf > NAAN_contact > unit > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















#### <a name="contact_anyOf_i0_tenure"></a>12.1.3. Property `NAAN > contact > anyOf > NAAN_contact > tenure`




**Title:** Tenure

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** <start year YYYY of role tenure>[-<end of tenure> ]




| Any of(Option)                              |
| ------------------------------------------- |
| [item 0](#contact_anyOf_i0_tenure_anyOf_i0) |
| [item 1](#contact_anyOf_i0_tenure_anyOf_i1) |


##### <a name="contact_anyOf_i0_tenure_anyOf_i0"></a>12.1.3.1. Property `NAAN > contact > anyOf > NAAN_contact > tenure > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









##### <a name="contact_anyOf_i0_tenure_anyOf_i1"></a>12.1.3.2. Property `NAAN > contact > anyOf > NAAN_contact > tenure > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















#### <a name="contact_anyOf_i0_email"></a>12.1.4. Property `NAAN > contact > anyOf > NAAN_contact > email`




**Title:** Email

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** Email address of contact




| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#contact_anyOf_i0_email_anyOf_i0) |
| [item 1](#contact_anyOf_i0_email_anyOf_i1) |


##### <a name="contact_anyOf_i0_email_anyOf_i0"></a>12.1.4.1. Property `NAAN > contact > anyOf > NAAN_contact > email > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









##### <a name="contact_anyOf_i0_email_anyOf_i1"></a>12.1.4.2. Property `NAAN > contact > anyOf > NAAN_contact > email > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















#### <a name="contact_anyOf_i0_phone"></a>12.1.5. Property `NAAN > contact > anyOf > NAAN_contact > phone`




**Title:** Phone

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** Telephone number for contact




| Any of(Option)                             |
| ------------------------------------------ |
| [item 0](#contact_anyOf_i0_phone_anyOf_i0) |
| [item 1](#contact_anyOf_i0_phone_anyOf_i1) |


##### <a name="contact_anyOf_i0_phone_anyOf_i0"></a>12.1.5.1. Property `NAAN > contact > anyOf > NAAN_contact > phone > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









##### <a name="contact_anyOf_i0_phone_anyOf_i1"></a>12.1.5.2. Property `NAAN > contact > anyOf > NAAN_contact > phone > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |














### <a name="contact_anyOf_i1"></a>12.2. Property `NAAN > contact > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="alternate_contact"></a>13. Property `NAAN > alternate_contact`





|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |






| Any of(Option)                              |
| ------------------------------------------- |
| [NAAN_contact](#alternate_contact_anyOf_i0) |
| [item 1](#alternate_contact_anyOf_i1)       |


### <a name="alternate_contact_anyOf_i0"></a>13.1. Property `NAAN > alternate_contact > anyOf > NAAN_contact`


|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [NAAN_contact](#contact_anyOf_i0)                                         |




### <a name="alternate_contact_anyOf_i1"></a>13.2. Property `NAAN > alternate_contact > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="comments"></a>14. Property `NAAN > comments`




**Title:** Comments

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |


**Description:** Comments about NAAN record




| Any of(Option)               |
| ---------------------------- |
| [item 0](#comments_anyOf_i0) |
| [item 1](#comments_anyOf_i1) |


### <a name="comments_anyOf_i0"></a>14.1. Property `NAAN > comments > anyOf > item 0`


|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |








|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |


| Each item of this array must be          | Description |
| ---------------------------------------- | ----------- |
| [item 0 items](#comments_anyOf_i0_items) | -           |


#### <a name="autogenerated_heading_2"></a>14.1.1. NAAN > comments > anyOf > item 0 > item 0 items


|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |












### <a name="comments_anyOf_i1"></a>14.2. Property `NAAN > comments > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |

















## <a name="provider"></a>15. Property `NAAN > provider`




**Title:** Provider

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `null`                                                                    |






| Any of(Option)               |
| ---------------------------- |
| [item 0](#provider_anyOf_i0) |
| [item 1](#provider_anyOf_i1) |


### <a name="provider_anyOf_i0"></a>15.1. Property `NAAN > provider > anyOf > item 0`


|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |









### <a name="provider_anyOf_i1"></a>15.2. Property `NAAN > provider > anyOf > item 1`


|              |        |
| ------------ | ------ |
| **Type**     | `null` |
| **Required** | No     |
















----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-07-11 at 10:54:22 -0400
