# cyyoung_era
* Scrapes the web for MLB ERA leaders and CY Young winners and puts the info into a SQLITE DB
* Run era_or_cyyoung.py, will calls the classes and functions from the cy.py or era.py, depending
 on the choices the user makes
* Creates a database named baseball.sqlite if one does not already exist
* First time the era or cy funtions are called, checks if the cyyoung or era tables exists, if not, will create them
