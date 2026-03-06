# Wireframing

Abbiamo visto quanto sia importante, nella realizzazione di un prodotto, comprendere e prevedere il comportamento degli utenti.  
Tuttavia, è ora necessario cominciare ad approcciarci alla fase di progettazione concreta del prodotto, quella in cui le nostre idee possono trasformarsi in qualcosa di tangibile e capace di rispondere realmente alle esigenze dei destinatari.  
Sarebbe un grave errore partendo da un’idea cominciare a realizzarla senza seguire gli step fondamentali del processo di design. Immaginiamo, ad esempio, di essere uno sviluppatore: vogliamo realizzare un sito web, un’applicazione oppure una nuova funzionalità da aggiungere a un prodotto già esistente. Tuttavia, invece di condividere l’idea con il team e procedere in modo strutturato, ci lanciamo direttamente nella scrittura del codice e nella realizzazione della versione finale del prodotto. A questo punto sorgono alcune domande fondamentali:

- cosa facciamo se una volta ultimato il lavoro emergono problemi o errori difficili e costosi da correggere?

- cosa facciamo se, al terminare dello sviluppo, ci accorgiamo che il prodotto non è realmente utile o non risponde ai bisogni degli utenti?

La risposta è semplice: avremmo sprecato tempo, energie e risorse che avremmo potuto risparmiare oppure impiegare diversamente.  
Il primo passo da compiere quando si comincia a progettare un prodotto è la creazione di un **wireframe**.  
Il wireframe infatti rappresenta un supporto preliminare che funge da documentazione iniziale: serve a mostrare in modo semplice e immediato come intendiamo sviluppare il progetto che abbiamo in mente, ovvero come vogliamo dare forma e struttura alla nostra idea. Il suo scopo principale è comunicare al team le nostre intenzioni progettuali offrendo una visione sintetica e chiara del prodotto. Possiamo considerarlo una prima bozza utile a facilitare la comunicazione tra designer e programmatori e che permette al team di mettere in pratica la corretta *information architecture*.  
Il modo più semplice e tradizionale per realizzare un wireframe è utilizzare carta e penna: si tratta infatti di eseguire uno schizzo rapido delle principali componenti dell’interfaccia.  
In questa fase, eventuali problemi evidenti possono essere individuati e corretti con pochissimo sforzo, evitando sprechi di tempo e risorse nelle fasi successive dello sviluppo.  
**Cosa può fare un wireframe:**

- dare una struttura visuale, cioè una forma, all’informazione che il prodotto deve avere.

- incoraggiare la discussione tra membri del team.

- determinare quali sono le funzioni e le caratteristiche della UI.

  
**Cosa non può fare un wireframe:**

- creare qualcosa di finito.

- un wireframe non ha ’funzioni funzionanti’, cioè non è interattivo.

- non garantisce una comprensione generale.

## Il contesto attuale e l’impatto sui wireframe

Viviamo in un periodo di profonda rivoluzione tecnologica.  
Questo cambiamento sta trasformando radicalmente il modo in cui i prodotti digitali vengono progettati: si passa da un approccio in cui ingegneri e sviluppatori realizzavano prodotti comprensibili soprattutto a loro stessi e ad altri esperti, a un approccio in cui il prodotto è costruito intorno all’utente con l’obiettivo di ottimizzare il più possibile la sua esperienza.  
Inoltre, i dispostivi con cui interagiamo ogni giorno si stanno moltiplicando e soprattutto diversificando: dagli schermi ultrawide delle TV, al monitor del nostro PC, allo smartphone fino ai display più piccoli come quelli degli smartwatch.  
Ovviamente, vent’anni fa tutta questa varietà non esisteva affatto ed è chiaro che tutto questo ha un forte impatto anche sul wireframing e sulla costruzione delle interfacce. La stessa applicazione, infatti, non può essere presentata nello stesso modo su uno smartphone e su uno schermo di un PC: deve adattarsi al contesto d’uso e al dispositivo. Un buon designer deve tenere di conto sia dei requisiti funzionali che di quelli non funzionali, in particolare deve tenere conto dei principi di *adaptability*, *responsive design* e *accessibility*. È fondamentale ricordare che utenti diversi possono avere esigenze differenti e che il designer non progetta mai per se stesso ma per soddisfare i bisogni degli utenti finali.

## Tipologie di wireframes

Dal punto di vista grafico, il wireframe è qualcosa di semplice infatti molto spesso non include font, colori, testi complessi o immagini.  
Possiamo distinguere i wireframe in base al loro grado di *fidelity*, cioè a quanto si avvicinano alla forma finale del progetto pur rimanendo schemi semplificati. Possiamo quindi avere:

- **Low fidelity wireframes:** contengono un basso grado di fedeltà, un esempio è uno schizzo dell’interfaccia su carta dove si rappresentano solamente le parti essenziali. Questo tipo di approccio contiene elementi estremamente basici, giusto per far capire al team come si vuole impostrare la UI.

- **High fidelity wireframes:** una rappresentazione dettagliata dell’interfaccia con però ancora uno stile basico, icone e pochi altri dettagli. Chiaramente le icone e le immagini inserite sono semplici figure geometriche oltre all’utilizzo di un testo semplice e un font non troppo elaborato. All’aumentare del livello di fidelity vengono aggiunte anche altre caratteristiche come informazioni più precise sul layout, spacing e testi più elaborati.

Spesso può succedere di produrre più versioni dello stesso wireframe, migliorandolo progressivamente partendo da un wireframe molto low-fidelity e arricchendolo volta volta, oppure realizzarne uno per ogni pagina di un sito o per ogni diversa schermata di un’applicazione.

<figure id="fig:placeholder">
<img src="Media_Wireframing/WirefraesFidelity.png" style="width:50.0%" />
<figcaption>da sinistra verso destra, incremento del grado di fidelity nel wireframe.</figcaption>
</figure>

# Dai wireframes ai wireflows

Fino ad ora abbiamo accennato che i wireframe vengono impiegati per descrivere visivamente l’interfaccia utente tramite degli schemi statici e non interattivi. Le azioni che l’utente compirà su quell’interfaccia, però, nella realtà non sono statiche. Servono quindi degli strumenti capaci di descrivere quelle che sono le azioni che un utente può compiere su quella determinata pagina o applicazione.

## Userflows

Gli **userflow** aiutano a descrivere possibili azioni disponibili per un particolare utente all’interno della nostra interfaccia.  
Servono quindi a mappare tutti i passaggi e i movimenti possibili dell’utente all’interno della nostra applicazione o sito web.  
Riflettendo quindi sui possibili punti di contatto che l’utente avrà con il sistema, possiamo definire un diagramma di flusso.  
Uno userflow, quindi, non è altro che una mappa dei passaggi che un utente compie per raggiungere un obiettivo all’interno di un’interfaccia digitale. In altre parole, è il percorso completo che l’utente segue dal momento in cui entra nel sistema fino a quando completa un’azione (per esempio: fa un login, acquista un prodotto, invia un modulo). L’obiettivo è quello di capire e progettare la sequenza di interazioni in modo logico, semplice e fluido eliminando ostacoli o confusioni. Questo aiuta i designer a costruire delle esperienze coerenti.  
Per avere un quadro generale fino ad ora, possiamo dire che il wireframe mostra come è fatta graficamente l’interfaccia mentre lo userflow ci mostra come può l’utente muoversi all’interno di essa.

<figure id="fig:placeholder">
<img src="Media_Wireframing/UserFlow.png" style="width:60.0%" />
<figcaption>Esempio di userflow.</figcaption>
</figure>

## Wireflows

<figure id="fig:placeholder">
<img src="Media_Wireframing/WireFlow.png" style="width:60.0%" />
<figcaption>Esempio di wireflow</figcaption>
</figure>

Un **wireflow** è una combinazione tra uno userflow e una serie di wireframe. Si tratta di un diagramma di flusso che anziché utilizzare simboli astratti come rettangoli o rombi, impiega dei wireframe di vere schermate dell’interfaccia. Mentre uno userflow rappresenta esclusivamente i passaggi logici compiuti dall’utente, il wireflow mostra anche come queste schermate appaiono visivamente e come l’utente si muove tra di esse. Per costruire quindi un wireflow occorre prima disegnare i wireframe per ogni schermata dell’interfaccia e successivamente collegare queste schermate tramite frecce che indicano cosa accade quando l’utente compie una certa azione che può essere il click di un bottone o l’inserimento di dati. Il risultato finale è uno strumento estremamente utile per comprendere e comunicare in modo chiaro il funzionamento di un flusso utente.

## Mockup

Un **mockup** è la rappresentazione ad alta fedeltà di un’interfaccia o di un prodotto digitale. Tale strumento serve per mostrare come apparirà visivamente il design finale del prodotto pur non essendo interattivo. Possiamo considerare il mockup come un’evoluzione del wireframe: alla struttura essenziale vengono aggiunti numerosi elementi di design come colori, font, immagini reali e altri dettagli grafici. Il mockup viene dunque utilizzato in una fase più avanzata del processo di progettazione e risulta utile per:

- rifinire e mostrare l’aspetto visivo finale dell’interfaccia.

- comunicare in modo chiaro il design.

- evidenziare lo stile del prodotto e magari anche compiere un confronto tra diverse versioni dello stesso mockup da presentare ad un cliente.

- supportare il dialogo tra designer e sviluppatori.

L’osservazione finale riguarda il fatto che nonostante la somiglianza al prodotto finale, il mockup non permette veri e propri test di usabilità perché rimane una rappresentazione statica del design con cui non è possibile interagire. Per raccogliere feedback concreti sul comportamento del prodotto e sulla sua esperienza d’uso è necessario comprendere i concetti di *pretotipo* e *prototipo*.

<figure id="fig:placeholder">
<img src="Media_Wireframing/WIREVSMOCK.png" style="width:50.0%" />
<figcaption>Evoluzione da wireframe a mockup</figcaption>
</figure>

# Pretotyping

Il concetto di pretotipo nasce da un’idea di Alberto Savoia, ex ingegnere di Google, il quale si ispira alla legge di Fallimento del Mercato. Secondo questa legge, circa l’80-90% dei nuovi prodotti lanciati sul mercato ogni anno finisce per fallire. Dunque, anche se un prodotto è ben progettato non implica che le persone siano disposte ad utilizzarlo o a pagarlo.  
Il **pretotipo** di un prodotto nasce proprio per verificare rapidamente se un’idea ha davvero potenziale di mercato, prima di investire tempo, energie e denaro nello sviluppo di un prototipo completo.  
L’unico modo per contrastare la legge del fallimento del mercato è testare il mercato stesso. Per farlo è necessario creare un esperimento che simuli il prodotto in modo abbastanza realistico da permettere l’osservazione del comportamento delle persone che lo utilizzeranno.  
Savoia sottolinea che un’idea, finché rimane nella mente, non vale nulla: deve uscire e trasformarsi in qualcosa di concreto, anche se imperfetto, per essere mostrata agli utenti e capire se funziona davvero. Sostanzialmente, i prototipi devono aiutare a “fallire in fretta” ma spesso non ci riescono: la loro realizzazione richiede tempo e denaro, e talvolta i team finiscono per affezionarsi al prototipo stesso. Questo porta a non accettarne il fallimento e a continuare ad aggiungere funzionalità inutili, con un conseguente spreco di risorse.  
Per ovviare a questo problema, Savoia propone questa soluzione chiamata pretotipo che si colloca tra le idee astratte e il prototipo. Il pretotipo consiste in una forma più rapida, semplice ed economica del prodotto da testare e ci aiuta a capire se vale la pena o meno realizzarlo veramente. Serve a raccogliere dati concreti sul reale interesse delle persone prima di investire in un prototipo più tecnico.  
Grazie al pretotyping, possiamo ottenere risposte sull’efficacia o sull’interesse verso il nostro prodotto in ore o giorni, anziché settimane o mesi.  
Poiché un pretotipo può fallire molto rapidamente, il team può correggere velocemente gli errori o decidere senza esitazioni se abbandonare l’idea e investire in alternative più promettenti. Infine, vediamo quali sono i sette pilastri su cui si basa il concetto di pretotyping:

1.  Obbedire alla legge di Fallimento del Mercato.

2.  Assicurarsi di star costruendo il prodotto giusto.

3.  Non perdersi in chiacchiere, idee e opinioni.

4.  Fidarsi solo dei propri dati, trust your own data!

5.  Fare pretotyping.

6.  Parlare con i numeri e con i fatti.

7.  Pensare globalmente e non localmente.

<figure id="fig:placeholder">
<img src="Media_Wireframing/preproprod.png" style="width:80.0%" />
<figcaption>Pretotipo, Prototipo, Prodotto</figcaption>
</figure>

## Approfondimento sulla legge di Fallimento del Mercato

Ogni anno vengono progettati e prodotti quasi 25000 nuovi prodotti, l’80% dei quali non vedrà mai la luce o non arriverà mai nelle case delle persone. Circa il 27% falliscono nel percorso di crescita dell’azienda, il 16% non raggiunge le aspettative degli utenti, trattasi quindi di fallimento di mercato, e per ben il 37% vengono cancellati durante la fase di lancio. Del 20% rimanente, il 14% sono prodotti che raggiungo il mercato e ci rimangono ma non hanno successo.  
Solo il 6% ha veramente successo.  
La legge di Fallimento del Mercato sostiene che la maggior parte dei nuovi prodotti fallirà nel mercato anche se la progettazione e lo sviluppo vengono eseguite in maniera corretta e competente.  
In legge, una persona è considerata innocente fino a prova contraria, mentre nella legge di mercato, bisogna considerare ogni prodotto come fallito fino a prova contraria.  
Due fenomeni interessanti che possiamo trovare nella realtà del mercato riguarda i prodotti etichettati come falsi positivi e quelli etichettati come falsi negativi. I primi sono tutti quei prodotti che all’apparenza sembravano perfetti, capaci di avere un grandissimo successo sul mercato ma che in realtà, nonostante i molti investimenti si sono rivelati un flop. I secondi invece sono tutti quei prodotti giudicati fallimentari ma che in realtà hanno avuto un successo eclatante. Twitter, Google, Tesla sono tutti esempi di falsi negativi.

## Come realizzare un pretotipo

Per realizzare un pretotipo è necessario seguire i seguenti step:

1.  Analizzare il problema che vogliamo risolvere e chiederci se effettivamente ha senso risolverlo: serve veramente quel prodotto?

2.  Scegliere il tipo di pretotipo più adatto al nostro scopo in base all’idea a cui vogliamo dare vita.

3.  Una volta scelto il tipo di pretotipo più adatto è necessario fare un’ipotesi di mercato per raccogliere e comprendere il numero di persone e utenti che sono realmente interessate al possibile futuro prodotto.

4.  Testare il pretotipo.

5.  Migliorare il migliorabile e capire ulteriormente la popolazione.

## Tipologie di pretotipo

Analizziamo adesso i diversi tipi di pretotipo che possiamo implementare in base al prodotto finale che vogliamo realizzare.

- **Fake door:** si tratta di una simulazione di un prodotto o servizio che ancora non esiste e viene utilizzata per misurare il reale interesse delle persone verso quell’ipotetico prodotto. Per realizzare una fake door è sufficiente, come suggerisce il nome, creare una porta d’ingresso finta che sia una pagina web, oppure un banner pubblicitario che invita l’utente a scoprire il prodotto non ancora sviluppato. Viene calcolato poi il numero di click sul banner pubblicitario per comprendere se l’idea può piacere o meno, oppure il numero di registrazioni sul sito web. Se i numeri dovessero essere bassi allora forse è meglio abbandonare l’idea. È chiaro però che questo metodo ci evita la creazione di un prototipo evitando un possibile spreco di risorse.

- **Mechanical Turk (Wizard of Oz):** si tratta di un esperimento in cui una persona reale simula manualmente le funzioni di un sistema automatizzato, dando all’utente l’illusione che in realtà quella tecnologia già esiste. Serve a capire se una funzione ‘intelligente’ è davvero utile prima di svilupparla nella realtà risparmiando così costi molto elevati in caso di mancato interesse da parte degli utenti. Un esempio è un chatbot che sembra automatizzato ma che in realtà dietro ad esso vi è un operatore umano.

- **Impersonator (The re-label):** questo tipo di pretotipo consiste nell’utilizzare un servizio già esistente facendolo passare per qualcosa di nuovo semplicemente cambiandone l’etichetta oppure il nome. Serve per testare un’idea senza costruire nulla da zero. Un esempio di questo metodo è applicare un diverso front-end a una API già esistente oppure, in altri campi, come per esempio quello farmaceutico: prendo un prodotto già esistente e ci metto una nuova etichetta sopra per vedere se gli utenti sono interessati o no.

- **Pinocchio:** si tratta di una versione fisica ma non funzionante del prodotto: un modello inanimato che permette di testare forma, dimensione e interazione fisica senza nessuna funzionalità reale. Questo tipo di pretotipo è più indicato verso i dispositivi fisici che quelli virtuali. Un esempio è creare un modello fittizio di un cellulare per capire se l’ergonomia è corretta e se il prodotto è maneggevole oppure troppo ingombrante.

- **One night stand:** consiste nell’offrire una versione completa ma temporanea del servizio che si vuole testare senza costruire un’infrastruttura definitiva. Serve per capire se il servizio ha valore per gli utenti prima di fare investimenti importanti. Un esempio è testare l’interesse nei confronti di un ristorante affittando magari un locale per un breve periodo e testare l’interesse delle persone in base all’affluenza.

- **Facade (the pretend-to-own):** in questo tipo di pretotipo simuliamo di avere risorse costose, affittandole o prendendole in prestito. Serve per testare l’interesse del pubblico per un qualche tipo di servizio che magari in quel momento non può essere sostenuto economicamente. Per esempio, un’idea è quella di aprire un servizio di noleggio di auto di lusso ma invece di comprarne una flotta ne viene affittato un certo numero e viene simulato l’intero servizio con applicazione per prenotazioni, consegna e tutti gli altri servizi annessi. Questo tipo di pretotipo lavora molto sull’immagine dell’azienda più che sul prodotto stesso.

Dopo aver sperimentato tramite l’impiego del pretotyping e aver raccolto prove sufficienti che l’idea possa generare reale interesse nel pubblico, possiamo passare ad una possibile strada successiva che è quella della costruzione del **Minimum Viable Product**.  
Questo rappresenta una prima versione funzionante, seppur ridotta, del prodotto finale. Il Minimum Viable Product contiene solamente le funzioni essenziali, cioè quelle che sono state ampiamente testate nelle fasi precedenti. In sostanza non abbiamo tra le mani qualcosa di definitivo ma abbiamo qualcosa di vendibile da cui è possibile ottenere del ricavo e dell’utile da sfruttare nella produzione definitiva del prodotto.

# Prototyping

Un **prototipo** è una versione sperimentale e preliminare di un progetto.  
In particolare, è l’oggetto più vicino in assoluto al prodotto finale e ci permette di avere una rappresentazione tangibile ed interattiva di esso.

## Aspetti fondamentali e multidimensionalità

In primis, dobbiamo sottolineare che esistono diversi tipi di prototipi che possono essere più o meno complessi sotto diversi aspetti e punti di vista.  
Tuttavia, il processo fondamentale alla base del prototyping consiste nel selezionare le caratteristiche chiave da testare e analizzare, attraverso il feedback degli utenti. Possiamo quindi analizzare i prototipi secondo diversi parametri ed il primo di questi è la *fidelity*.

<figure id="fig:placeholder">
<img src="Media_Wireframing/lowfidelity.png" style="width:50.0%" />
<figcaption>Low fidelity prototype.</figcaption>
</figure>

- **Low fidelity prototypes:** si tratta di prototipi molto economici, veloci da realizzare e da modificare. Permettono interazioni rapide ed incoraggiano il design thinking. Lo svantaggio di questo tipo di prototipo è che sono poco realistici, quindi difficili da valutare dagli utenti poichè semplificano troppo l’esperienza reale.

- **High fidelity prototypes:** sono realizzati in maniera più complessa, spesso programmati con software appositi. Offrono un’esperienza molto simile al prodotto finale producendo risultati di test accurati e realistici. Lo svantaggio è che per realizzarli è richiesto molto tempo e risorse, inoltre, i designer sono spesso riluttanti a compiere modifiche dopo ore/giorni di lavoro. Può capitare anche che gli utenti possano confondere il prototipo col prodotto reale creando bias nei feedback.

- **Mid fidelity prototypes:** questi si trovano a metà strada tra i due prima citati. Mantengono spesso la semplicità tipica dei low fidelity prototypes ma integrano elementi visivi e interattivi tipici dei high fidelity.

Come accennato precedentemente, la *fidelity* del prodotto può essere valutata su più dimensioni e non solamente rispetto a quanto realistico esso appare in relazione al prodotto finale. Le principali dimensioni, oltre a quella visuale, sono le seguenti:

- **Scope:** questo parametro indica l’ampiezza e la profondità del design rappresentato, cioè quanto del sistema è incluso nel prototipo e quanto è dettagliatamente sviluppato. In altre parole definisce quanto l’utente potrà vedere, esplorare e testare del prodotto. Lo scope può essere *orizzontale*, offre quindi una visione ampia ma superficiale del prodotto. Ad esempio un e-commerce in cui si può navigare, aggiungere prodotti al carrello senza però completare l’acquisto. Oppure lo scope può essere *verticale* e qui si concentra su una singola funzionalità sviluppata nel dettaglio e pienamente funzionale. Ad esempio, vogliamo testare esclusivamente il flusso completo di checkout per verificare se il sistema di acquisto funziona correttamente.

- **Functionality:** quanto il prototipo funziona devvero, ad esempio i pulsanti, i link o le azioni simulano davvero il comportamento reale?

- **Data:** il prototipo utilizza dati reali o dati fittizi?

- **Autonomy:** il prototipo può funzionare da solo oppure richiede l’intervento di qualcuno per simulare le azioni?

- **Platofrm:** indica il tipo di implementazione su cui si basa il prototipo ovvero se essa rappresenta una versione temporanea/intermedia oppure una versione più definitiva del prodotto, chiaramente più la versione è definitiva e più il prototipo si avvicina al prodotto finale e reale.

## Wireframes vs. Mockup vs. Prototipi

Spesso queste tre parole vengono confuse, ma in realtà indicano fasi diverse del processo di design. Per ricapitolare ciò che abbiamo visto finora:

- **Wireframe:** il wireframe è il disegno iniziale, la bozza strutturale del prodotto. Serve a rappresentare l’organizzazione degli elementi, la gerarchia delle informazioni e il flusso generale dell’interfaccia (wireflow). È uno strumento per far capire al team come funziona l’idea, senza concentrarsi ancora sull’aspetto estetico.

- **Mockup:** arricchendo il wireframe con colori, tipografie, immagini e dettagli visivi, otteniamo il mockup. Il mockup mostra come apparirà la UI, ma non è interattivo: rappresenta l’aspetto finale del prodotto, non il suo comportamento.

- **Prototype:** a partire da wireframe e mockup, si realizzano poi pretotipi e prototipi. Questi ultimi simulano l’esperienza utente e il funzionamento del prodotto, permettendo di testare flussi, interazioni e comportamenti reali. Di solito, se il pretotipo dà esito positivo, si procede con la creazione di un prototipo completo, che viene testato per individuare eventuali problemi, correggere gli errori e rifinire l’esperienza prima di passare alla fase di sviluppo effettivo.

# Introduzione a Figma

Figma è una web application molto popolare tra i designer, utilizzata per creare wireframe, mockup e prototipi di interfacce digitali, come siti web o applicazioni.  
Uno dei suoi principali vantaggi è la disponibilità di un piano gratuito per studenti, che lo rende facilmente accessibile anche in ambito accademico.  
Un altro punto di forza è la collaborazione in tempo reale: più persone possono lavorare contemporaneamente sullo stesso progetto, commentare, modificare e proporre idee, in modo simile a quanto avviene su un documento condiviso di Google o su una repository GitHub. Questo rende Figma particolarmente utile per i team di design che vogliono lavorare in modo coordinato ed efficiente.  
La piattaforma è supportata da una vasta comunità di utenti e da una ricca libreria di plugin che permettono di estendere le funzionalità del programma. Questi strumenti consentono, ad esempio, di generare icone, creare palette di colori personalizzate o automatizzare operazioni ripetitive.  
Per quanto riguarda l’organizzazione del lavoro, Figma utilizza un sistema di livelli (layers) che, pur differendo leggermente da quello di software come Photoshop, rimane intuitivo:

- ogni oggetto presente sulla tela è considerato un layer;

- raggruppare più oggetti insieme permette la realizzazione di un layer;

- inserire degli oggetti in un frame fa sì che il frame diventi un livello principale che contiene al suo interno altri sotto-livelli.

Questo sistema aiuta a mantenere i progetti ordinati e facilmente gestibili. Inoltre, Figma permette di utilizzare pagine multiple, ideali per suddividere zone diverse del lavoro, ad esempio tra wireframe, mockup e prototipi. Di recente è stata introdotta anche una funzionalità basata su LLM e AI, chiamata Figma Make, che consente di generare prototipi e diversi tipi di design a partire da un semplice prompt testuale.

<figure id="fig:placeholder">
<img src="Media_Wireframing/image.png" style="width:100.0%" />
<figcaption>Risultato del prompt "tennis website" generato da Figma Make</figcaption>
</figure>

