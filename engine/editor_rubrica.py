import os
import csv
from schemas.rubrica_schema import RubricaSchema, RubricaCreateSchema, RubricaUpdateSchema, RubricaDeleteSchema
class EditorRubrica:

    def __init__(self, data_path: str):
        try:            
            if not os.path.exists(data_path):
                raise FileNotFoundError(f"Directory '{data_path}' non trovata.")
            
            self.data_path = data_path

            self.carica_contatti()

            self.maxId = self.contatti.sort(key=lambda x: (x[0]), reverse = True)[0][0]


        except Exception as e:
            print(f"Errore durante l'inizializzazione: {e}")
            raise

    def carica_contatti(self):
        """Carica i contatti dal file CSV e restituisce i dati come stringa."""
        try:
            with open(self.data_path, 'r') as rubrica_file:
                # Carica i contatti dal file CSV e restituisci i dati come stringa
                reader = csv.reader(rubrica_file) # Salta l'intestazione

                contatti = list(reader)[1:]
                contatti.sort(key=lambda x: (x[2], x[1]))  # Ordina per cognome e nome
                contatti = [contatto for contatto in contatti if any(contatto)]  # Rimuove eventuali righe vuote

                print(f"Contatti caricati da '{self.data_path}'.")
                print(f"Numero di contatti: {len(contatti)}")

                self.contatti = contatti

                return {
                    "status": "success",
                    "data": contatti
                }

        except Exception as e:
            print(f"Errore durante il caricamento dei dati: {e}")
            raise

    
    def mostra_contatti(self):
        """Stampa i contatti in console."""
        try:
            print("Contatti:")
            for contatto in self.contatti:
                print(f"Nome: {contatto[1]}, Cognome: {contatto[2]}, Telefono: {contatto[3]}")

        except Exception as e:
            print(f"Errore durante la visualizzazione dei contatti: {e}")
            raise

    def aggiungi_contatto(self, contatto: RubricaCreateSchema):
        """Aggiunge un nuovo contatto alla rubrica."""
        try:

            if not isinstance(contatto, RubricaCreateSchema):
                raise ValueError("Il contatto deve essere un'istanza di RubricaCreateSchema.")
            
            contatto.id = self.maxId + 1
            self.maxId += 1


            with open(self.data_path, 'a', newline='') as rubrica_file:
                writer = csv.writer(rubrica_file)
                writer.writerow(contatto)
                print(f"Contatto aggiunto: {contatto}")

        except Exception as e:
            print(f"Errore durante l'aggiunta del contatto: {e}")
            raise