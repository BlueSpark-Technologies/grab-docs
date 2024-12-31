# PS Testing (UAT & CP E2E)

# Which channel price must be tested in which application?
| # | Channel price | Testing bucket | Hybris Commerce | AEM | FACT-Finder | SAP ERP | SAP CRM | ProductBrain | MPA | Preisportale/Marktplätze | Algonomy | C2 Circle | Algolia | Breece | Zoovuu | Categories | 1 | SC_AMAZON | 2 | SC_EBAY | 3 | SC_SYNAXON | 3 | SC_BURDA | 3 | SC_B2B_PORTALE | 3 | SC_MERCATEO_OPEN | 3 | SC_MERCATEO_CLOSED | 4 | SC_CU | 5 | SC_SUBSCRIPTION | 6 | STORES* | 7 | WS_DE | 7 | WS_AT |  | SC_GEBRAUCHT_DE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| smoketest +1 |  |  |  | x | x | x | x |  |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x | x |  |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | ChannelPilot? |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | Burda |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | ChannelPilot & ??? |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | Mercateo (Unite) |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | Mercateo (Unite) |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  | ComputerUniverse |  |  |  |  |  | All |
| +1 |  |  |  | x | x | x |  |  |  | x |  |  |  | Only Apple |
| 2 | x | x | x | x | x | x |  | ChannelPilot | x |  | x | x |  | All |
| 3 | x | x | x | x | x | x |  | ChannelPilot | x |  | x |  | x | All |
| 3 | x | x | x | x | x | x |  | ChannelPilot | x |  | x |  | x | All |
|  | n/a |  |  |  |  |  |  |  |  |  |  |  |  |  |

#

Channel price

Testing bucket

Hybris Commerce

AEM

FACT-Finder

SAP ERP

SAP CRM

ProductBrain

MPA

Preisportale/Marktplätze

Algonomy

C2 Circle

Algolia

Breece

Zoovuu

Categories

1

SC_AMAZON

smoketest +1

x

x

x

x

All

2

SC_EBAY

+1

x

x

x

x

All

3

SC_SYNAXON

+1

x

x

x

ChannelPilot?

All

3

SC_BURDA

+1

x

x

x

Burda

All

3

SC_B2B_PORTALE

+1

x

x

x

ChannelPilot & ???

All

3

SC_MERCATEO_OPEN

+1

x

x

x

Mercateo (Unite)

All

3

SC_MERCATEO_CLOSED

+1

x

x

x

Mercateo (Unite)

All

4

SC_CU

+1

x

x

x

ComputerUniverse

All

5

SC_SUBSCRIPTION

+1

x

x

x

x

Only Apple

6

STORES*

2

x

x

x

x

x

x

ChannelPilot

x

x

x

All

7

WS_DE

3

x

x

x

x

x

x

ChannelPilot

x

x

x

All

7

WS_AT

3

x

x

x

x

x

x

ChannelPilot

x

x

x

All

SC_GEBRAUCHT_DE

n/a

# 7 Product categories and Test Executions:
| Product category | Test Execution w. existing product | Test Execution w. new product | Test Execution w. EOL/reactivated product | Tester |
|---|---|---|---|---|
| Notebooks | CPUAT-4533 | CPUAT-4534 |  |  |
| Home Electronics | CPUAT-4535 |  | CPUAT-4539 |  |
| Apple | CPUAT-4536 |  |  | Arian Teßmann |
| Mobile | CPUAT-4537 |  |  |  |
| Components | CPUAT-4538 |  |  |  |
| GW |  | CPUAT-4621 |  | Julian Grund(Stefan Teich) |
| Insurance, Services | CPUAT-4619 |  |  | Katrin Siegel |

Product category

Test Execution w. existing product

Test Execution w. new product

Test Execution w. EOL/reactivated product

Tester

* Notebooks

Notebooks

CPUAT-4533

CPUAT-4534

* Home Electronics

Home Electronics

CPUAT-4535

CPUAT-4539

* Apple

Apple

CPUAT-4536

Arian Teßmann

* Mobile

Mobile

CPUAT-4537

* Components

Components

CPUAT-4538

* GW

GW

CPUAT-4621

Julian Grund

(Stefan Teich)

* Insurance, Services

Insurance, Services

CPUAT-4619

Katrin Siegel

# Test cases UAT
Testplan: CPUAT-4532

| Test case | Content / test steps | Test case in JIRA | Tester |
|---|---|---|---|
| 1a | Lege einen VK1 an und prüfe WS-DE-Zeile (ggf. WS-AT)bei “VK1-gebunden” | CPUAT-4215 | Steffen / Pöschi |
| 1b | Lege einen VK1 an und prüfe WS-DE-Zeile (ggf. WS-AT)bei “Automatisch” | CPUAT-4216 |
| 2 | Amazon-Formel prüfen | CPUAT-4217 | Malte |
| Ebay-Formel prüfen |
| 3 | Synaxon | CPUAT-4218 |  |
| Burda |
| Mercateo 2x |
| B2B-Portale |
| 4 | CU | CPUAT-4219 |  |
| 5 | C2 Circle | CPUAT-4220 |  |
| 6 | Stores | CPUAT-4221 | Moritz |
| 7 | Sonderfall Versicherungen / Services | CPUAT-4618 | Katrin |
| 8 | Sonderfall GW | CPUAT-4620 | Julian / Stefan |
| Für E2E: | Prüfschritte je Applikation dranhängen |  |  |

Test case

Content / test steps

Test case in JIRA

Tester

1a

Lege einen VK1 an und prüfe WS-DE-Zeile (ggf. WS-AT)bei “VK1-gebunden”

CPUAT-4215

Steffen / Pöschi

1b

Lege einen VK1 an und prüfe WS-DE-Zeile (ggf. WS-AT)bei “Automatisch”

CPUAT-4216

2

Amazon-Formel prüfen

CPUAT-4217

Malte

Ebay-Formel prüfen

3

Synaxon

CPUAT-4218

Burda

Mercateo 2x

B2B-Portale

4

CU

CPUAT-4219

5

C2 Circle

CPUAT-4220

6

Stores

CPUAT-4221

Moritz

7

Sonderfall Versicherungen / Services

CPUAT-4618

Katrin

8

Sonderfall GW

CPUAT-4620

Julian / Stefan

Für E2E:

Prüfschritte je Applikation dranhängen

Themen:

* Preise / Preiszeilen löschen
* Übergangszeit testen (Teile von Preiszeilen sind bereits im Pricingservice aktiv)
* Preiszeilen Snap-Shot zum GoLive-Tag prüfen
* Überlappende Preiskampagnen (div. Datums-Prüfungen)

Preise / Preiszeilen löschen

Übergangszeit testen (Teile von Preiszeilen sind bereits im Pricingservice aktiv)

Preiszeilen Snap-Shot zum GoLive-Tag prüfen

Überlappende Preiskampagnen (div. Datums-Prüfungen)

## Übergangsphase der Preiszeilen-Migration
Testplan: CPUAT-4524

| Phase | Cyberparts | Microservices |
|---|---|---|
| 1. Alle Preiszeilen in Cyberparts(aktueller PRD-Zustand, wird nicht getestet) | n/a | Alle Preise werden nicht versendetneuändernAlle Produkt-Status |
| 2. Einzelne Preiszeile im MicroserviceTestfall: CPUAT-4499+ [CPUAT-4717] MS7 - Artikelstatus ausgelistet & Pricing - Cyberport JIRA+ [CPUAT-4716] MS7 - Artikelstatus Sortiment & Pricing - Cyberport JIRA+ [CPUAT-4715] MS7 - Artikelstatus neu anlegen & Pricing - Cyberport JIRA | Einzelne Preise werden nicht versendetneuändernAlle Produkt-Status | Einzelne Preise werden versendetneuändernAlle Produkt-Status |
| Übrige Preise werden versendetneuändernAlle Produkt-Status | Übrige Preise werden nicht versendetneuändernAlle Produkt-Status |
| 3. Alle Preiszeilen im Microservice | Alle Preise werden nicht versendetneuändernAlle Produkt-Status | Alle Preise werden versendetneuändernAlle Produkt-Status |

Phase

Cyberparts

Microservices

1. Alle Preiszeilen in Cyberparts

(aktueller PRD-Zustand, wird nicht getestet)

n/a

Alle Preise werden nicht versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

2. Einzelne Preiszeile im Microservice

Testfall: CPUAT-4499

+ [CPUAT-4717] MS7 - Artikelstatus ausgelistet & Pricing - Cyberport JIRA

+ [CPUAT-4716] MS7 - Artikelstatus Sortiment & Pricing - Cyberport JIRA

+ [CPUAT-4715] MS7 - Artikelstatus neu anlegen & Pricing - Cyberport JIRA

Einzelne Preise werden nicht versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

Einzelne Preise werden versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

Übrige Preise werden versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

Übrige Preise werden nicht versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

3. Alle Preiszeilen im Microservice

Alle Preise werden nicht versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

Alle Preise werden versendet

* neu
* ändern

neu

ändern

Alle Produkt-Status

