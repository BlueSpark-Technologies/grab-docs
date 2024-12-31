# IHS Requirements Engineering

Die Einordnung von Produkten in das Unhealthy Inventory-Schema vollzieht sich aus der Kombination der gewichteten Dauer des Lagerbestands (Aging) und der aus vorangegangen Absatzzahlen prognostizierten Reichweite der Lagermenge bis zum Abverkauf (Coverage). Anhand dieser beiden Kennzahlen werden Produkte mit Lagerbestand folgendermaßen kategorisiert:

## Berechnung des gewichteten Alters (Aging)
Für die Berechnung des ‚Aging‘ eines Produktes ist die Dauer vom Warenerhalt bis zum (aktuellen) Lagerdatum relevant. Da sich die Lagermenge eines Produktes aus verschieden datierten Wareneingängen/Lieferungen zusammensetzen kann, werden unterschiedliche Lagerdauern berücksichtigt.

In diesem Kontext wird nach ‚First in, first out (FIFO)‘-Prinzip davon ausgegangen, dass zuerst erhaltene Wareneingänge auch zuerst verkauft werden; für die Berechnung werden somit ausschließlich die Mengen der letzten relevanten Wareneingänge hinzugezogen.

Relevante Bewegungsarten als Wareneingang für die Berechnung des Unhealthy Inventory:

| BWART | Bewegungsartentext |
|---|---|
| 101 | WE Wareneingang |
| 309 | UL Umbuch Mat an Mat |
| 511 | Kostenlose Lieferung |
| 501 | Eingang ohne Bestell |
| 712 | WE InvDiff. Lager |
| 971 | WE Wareneingang |
| 975 | UL Umbuch Mat an Mat |

BWART

Bewegungsartentext

101

WE Wareneingang

309

UL Umbuch Mat an Mat

511

Kostenlose Lieferung

501

Eingang ohne Bestell

712

WE InvDiff. Lager

971

WE Wareneingang

975

UL Umbuch Mat an Mat

Basis der Menge des Lagerbestands für die Berechnung des ‚Aging‘, stellt der freie Lagerbestand im Zentrallager abzüglich der offenen Bestellmenge dar. Die offene Bestellmenge ist definiert als die eingegangene Kundenbestellmenge abzüglich der bereits gesandten (Teil)Warenlieferungen für das Zentrallager.

Formal

Lagderdauer i (n) := Lagerdauer des i-ten (letzten) Wareneingangs

Stk. i (n) := Zugewiesene Stückzahl des i-ten (letzten) Wareneingangs (Die Gesamtstückzahl wird aufgeteilt und zunächst dem letzten Wareingang zugeschrieben, anschließend dem vorletzten Wareneingang, usw.)

Summe Lagerbestand = Lagerbestand des Produktes im Zentrallager (:= Freier Lagerbestand - Offene Bestellmenge)

Beispiel

| INVENTORY DATE | PRODUCT ID | RECEIPT DATE | AGE | RECEIPT_QTY | INVENTORY QTY | FREE INVENTORY QTY | OPEN RE-QUESTED QTY | INVENTORY RELATED QTY |
|---|---|---|---|---|---|---|---|---|
| 19.06.2018 | 5701-840 | 19.06.2018 | 0 | 20 | 29 | 32 | 3 | 20 |
| 19.06.2018 | 5701-840 | 14.06.2018 | 5 | 20 | 29 | 32 | 3 | 9 |
| 19.06.2018 | 5701-840 | 08.06.2018 | 11 | 20 | 29 | 32 | 3 | 0 |

INVENTORY DATE

PRODUCT ID

RECEIPT DATE

AGE

RECEIPT_QTY

INVENTORY QTY

FREE INVENTORY QTY

OPEN RE-QUESTED QTY

INVENTORY RELATED QTY

19.06.2018

5701-840

19.06.2018

0

20

29

32

3

20

19.06.2018

5701-840

14.06.2018

5

20

29

32

3

9

19.06.2018

5701-840

08.06.2018

11

20

29

32

3

0

AGE := Differenz zwischen Inventory_Date und Receipt_Date

RECEIPT_QTY := Wareneingangsmenge (hier: an drei Tagen sind jeweils 20 Stückmengen eingegangen)

INVENTORY_QTY := Freie Lagermenge abzüglich der offenen Auftragsmenge

INVENTORY_RELATED_QTY: Anzahl der Stückzahl des Lagerbestandes, der dem jeweiligen Wareingang zugeschrieben wird; sozusagen der Gewichtungsfaktor (hier: von 29 Produkten im Lagerbestand werden 20 Produkte nach Wareneingang vom 19.06. behandelt und 9 nach Wareneingang vom 14.06.)

In diesem Beispiel liegt die relevante Lagermenge für das Produkt ‚5701-840‘ bei 29 Stück. Gemäß FIFO werden 20 der 29 Stück dem chronologisch letzten Wareneingang zugeschrieben, wohingegen die restlichen 9 dem vorletzten Wareneingang zugeschrieben werden.

Das gewichtete Alter des Produktes mit den 29 Stück im Lager beträgt daraus:

Gewichtetes Alter            =             (0 * 20 + 5 * 9 +  11 * 0) / 29

=             1.551724              | vor Rundung

=             2                           | nach Rundung

## Berechnung der Reichweite (Coverage)
Die Reichweite stellt ein Mittelwert des täglichen Absatzes eines Produktes dar, welcher sich anhand der in Rechnung gestellten Menge (‚Billing Quantity‘) aus den letzten 84 Tage ergibt (1). Anschließend wird diese Menge in Relation zu dem Lagerbestands des Zentrallagers in Verhältnis gesetzt, um zu herauszufinden, wie viele Tage die derzeitige Lagermenge gegeben des gemittelten Absatzes pro Tag für einen kompletten Abverkauf benötigen würde (2).

Nachfolgende Sales Channels werden bei dieser Berechnung ausgeschlossen:

* 'Team Key Account'
* 'Team Projektsales'
* 'Team B2B'

'Team Key Account'

'Team Projektsales'

'Team B2B'

(1) Berechnung des gemittelten täglichen Absatzes

Verkäufe aus jüngerer Vergangenheit werden bei der Berechnung stärker gewichtet als länger zurückliegende. Die Gewichte bei der Berechnung sind wie folgt justiert:

* - 84 Tage bis Vortag: Faktor 1
* - 28 Tage bis Vortag: Faktor 3
* - 14 Tage bis Vortag: Faktor 7
* - 7 Tage   bis Vortag: Faktor 14

- 84 Tage bis Vortag: Faktor 1

- 28 Tage bis Vortag: Faktor 3

- 14 Tage bis Vortag: Faktor 7

- 7 Tage   bis Vortag: Faktor 14

Anschließend werden die um die genannten Faktoren gewichteten Summen der Verkaufszahlen aufsummiert um den Wert 364 geteilt.

Formal

Bill. Qty t := Die Summe an in Rechnung gestellter Stückmengen am Tag t

(2) Berechnung der Reichweite als Verhältnis von Lagerbestand und gemitteltem Absatz

Reichweite = Lagerbestand / gemittelter Absatz

Beispiel

| PRODUCT_ID | Summe Absatz7 Tage bis Vortag | Summe Absatz14 Tage bis Vortag | Summe Absatz28 Tage bis Vortag | Summe Absatz84 Tage bis Vortag |
|---|---|---|---|---|
| 5701-840 | 26 | 64 | 88 | 179 |

PRODUCT_ID

Summe Absatz

* 7 Tage bis Vortag

7 Tage bis Vortag

Summe Absatz

* 14 Tage bis Vortag

14 Tage bis Vortag

Summe Absatz

* 28 Tage bis Vortag

28 Tage bis Vortag

Summe Absatz

* 84 Tage bis Vortag

84 Tage bis Vortag

5701-840

26

64

88

179

In diesem Beispiel wurde das Produkt ‚5701-840‘ innerhalb der letzten 84 Tage mit insgesamt 179 Stück in Rechnung gestellt. Gemäß der stärkeren Gewichtung von Verkäufen in jüngerer Vergangenheit ergibt sich folgender Wert für die Reichweite:

(1) Gemittelter Absatz

Gemittelter Absatz          =                (26 * 14 + 64 * 7 + 88 * 3 + 179 * 1) / 364

=                 3.447802       | Vor Rundung

=                 3.45               | Nach Rundung

(2) Reichweite

Reichweite                   =                 29 / 3.45

=                 8.405797      | Vor Rundung

=                 8                   | Nach Rundung

Zu besprechen:

Umgang bei mehr Retouren als Fakturen, d.h. negativem Bedarf. Z.B. 7207-103 KW4-7 / 2019.

