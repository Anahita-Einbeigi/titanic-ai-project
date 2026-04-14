Titanic AI-projekt

Problem och dataset:

I det här projektet valde jag att arbeta med Titanic-datasetet från Kaggle. Målet är att förutsäga om en passagerare överlevde eller inte baserat på information som ålder, kön, biljettklass och andra faktorer.
Jag valde detta dataset eftersom det är relativt enkelt att förstå men ändå innehåller tillräckligt med variabler för att kunna bygga en fungerande maskininlärningsmodell. Det gör att fokus kan ligga på hela arbetsflödet i maskininlärning, från datahantering till modellutvärdering.
Detta är ett klassificeringsproblem, eftersom målet är att förutsäga en kategori (överlevde eller inte).

Datapreparering:

När jag analyserade datan upptäckte jag att vissa kolumner hade saknade värden, särskilt ålder och ibland embarkation. För att hantera detta fyllde jag:
   Ålder med medelvärdet
   Embarked med det vanligaste värdet (mode)
Jag tog också bort kolumner som inte var relevanta för problemet, såsom namn, biljett och passagerar-ID, eftersom de inte bidrar direkt till prediktionen.
Kategoriska variabler som kön och hamn omvandlades till numeriska värden med one-hot encoding, eftersom maskininlärningsmodeller endast kan arbeta med siffror.
En viktig observation var att datan inte var helt ren från början, vilket gjorde data preprocessing till en central del av projektet.

Visualisering:

Jag skapade en visualisering för att undersöka sambandet mellan kön och överlevnad. Resultatet visade tydligt att kvinnor hade betydligt högre överlevnad än män.
Detta gav en första indikation på att kön är en viktig feature i modellen.

Modell:

Jag valde att använda Logistic Regression som huvudmodell eftersom det är en enkel och stabil modell för klassificeringsproblem.
Datasetet delades upp i tränings- och testdata (70/30 split), och modellen tränades på träningsdatan.
För att jämföra använde jag även en Decision Tree-modell.
Jag valde dessa modeller för att förstå grundläggande skillnader mellan en linjär modell och en träd-baserad modell.

Utvärdering:

För att utvärdera modellerna använde jag:
  1)Accuracy
     Classification report (precision, recall, F1-score)
  2)Resultaten blev:
     Logistic Regression: 0.81 accuracy
    Decision Tree: 0.79 accuracy
Logistic Regression presterade alltså något bättre än Decision Tree.
Classification report visade också att modellen fungerar bättre för vissa klasser än andra, vilket är viktigt att förstå.

Modelljämförelse och analys:

Logistic Regression gav bäst resultat och blev därför den bästa modellen i detta projekt.
Skillnaden mellan modellerna visar att enklare linjära modeller kan fungera mycket bra på strukturerade dataset som Titanic.

Förbättringar:

En möjlig förbättring hade varit att använda mer avancerade modeller som Random Forest, som kan fånga mer komplexa samband i datan.
Man skulle också kunna göra mer feature engineering, till exempel skapa nya variabler från befintliga kolumner (t.ex. familjestorlek från SibSp och Parch).

Begränsningar och etik:

En viktig begränsning är att datasetet är historiskt och baserat på en specifik situation, vilket gör att resultaten inte kan generaliseras direkt till andra problem.
Det finns också tydlig bias i datan, till exempel att kön och biljettklass påverkar överlevnad kraftigt. Detta kan leda till att modellen lär sig snedvridna samband.
Därför bör modellen inte användas för verkliga beslut, utan endast som ett pedagogiskt exempel på maskininlärning.

Slutsats:

Projektet visar hela processen inom maskininlärning: från datainsamling och preprocessing till modellträning och utvärdering.
Logistic Regression gav bäst resultat med cirka 81% accuracy, vilket är ett bra resultat för en enkel modell utan avancerad optimering.
