Problem och dataset:

I det här projektet valde jag att arbeta med Titanic-datasetet från Kaggle. Målet är att förutsäga om en passagerare överlevde eller inte baserat på information som ålder, kön och biljettklass.

Jag valde detta dataset eftersom det är relativt enkelt att förstå men ändå innehåller tillräckligt med variabler för att kunna bygga en maskininlärningsmodell. Det gör att fokus kan ligga på hela arbetsflödet i maskininlärning snarare än på för komplex data.

Detta är ett klassificeringsproblem eftersom målet är att förutsäga en kategori (överlevde eller inte).

Datapreparering:

När jag började undersöka datat märkte jag att vissa kolumner hade saknade värden, särskilt i kolumner som ålder och ibland embarkation. För att kunna använda datan i modellen fyllde jag dessa med medelvärde respektive vanligaste värde.

Jag tog också bort kolumner som inte kändes relevanta för problemet, till exempel namn, biljett och passagerar-ID, eftersom de inte direkt bidrar till att förutsäga överlevnad.

Kategoriska variabler som kön och hamn omvandlades till numeriska värden med one-hot encoding, eftersom maskininlärningsmodellen endast kan arbeta med siffror.

En viktig observation var att datan inte var helt ren från början, vilket gjorde preprocessing till en viktig del av projektet.

Visualisering:

Jag skapade en enkel visualisering för att undersöka hur överlevnad fördelades mellan män och kvinnor. Resultatet visade tydligt att kvinnor hade betydligt högre överlevnad.

Detta gav en första indikation på att kön är en mycket viktig feature i modellen.

Modell:

Jag valde att använda Logistic Regression eftersom det är en enkel och stabil modell för klassificeringsproblem.

Datasetet delades upp i tränings- och testdata (70/30 split), och modellen tränades på träningsdatan.

Jag valde att börja med en enkel modell istället för mer avancerade metoder för att tydligt förstå hela processen.

Utvärdering:

För att utvärdera modellen använde jag accuracy samt classification report.

Modellen fick ett resultat på ungefär 0.78 accuracy, vilket är ett rimligt resultat för en enkel modell på detta dataset.

Samtidigt visar resultatet att modellen inte är perfekt och gör fel i vissa fall.

Förbättringar:

En möjlig förbättring hade varit att testa mer avancerade modeller som Random Forest, som ofta kan fånga mer komplexa samband i datan.

Man skulle också kunna arbeta mer med feature engineering, till exempel skapa nya variabler baserat på befintliga kolumner.

Begränsningar och etik:

En viktig begränsning är att datasetet är historiskt och representerar en specifik situation, vilket gör att det inte är direkt överförbart till andra problem.

Det finns också en tydlig bias i datan, till exempel att kön påverkar överlevnad kraftigt. Detta kan göra att modellen lär sig snedvridna samband.

Modellen bör därför inte användas för verkliga beslut, utan snarare som ett pedagogiskt exempel på maskininlärning.
