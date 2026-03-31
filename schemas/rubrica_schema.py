from datetime import datetime
import pydantic

class RubricaSchema(pydantic.BaseModel):
    """
    Schema per la rubrica telefonica, con validazione dei campi e formattazione dei dati.

    @param id: Identificatore univoco del contatto.
    @param nome: Nome del contatto, con lunghezza minima di 3 caratteri e massima di 50.
    @param cognome: Cognome del contatto, con lunghezza minima di 3 caratteri e massima di 50.
    @param telefono: Numero di telefono del contatto, con validazione per essere un numero italiano (tra 3000000000 e 4000000000).
    @param email: Indirizzo email del contatto, con validazione tramite regex per assicurare un formato corretto.
    
    @param created_at: Data e ora di creazione del contatto.
    @param updated_at: Data e ora dell'ultima modifica del contatto.
    """
    id: int
    nome: str = pydantic.Field(..., min_length=3, max_length=50)
    cognome: str = pydantic.Field(..., min_length=3, max_length=50)
    telefono: int = pydantic.Field(..., gt=3000000000, lt=4000000000)
    email: str = pydantic.Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    created_at: datetime
    updated_at: datetime


class RubricaCreateSchema(RubricaSchema):
    """
    Schema per la creazione di un nuovo contatto nella rubrica telefonica, con validazione dei campi e formattazione dei dati.

    @created_at: Data e ora di creazione del contatto, impostata automaticamente al momento della creazione.
    @updated_at: Data e ora dell'ultima modifica del contatto, impostata automaticamente al momento della creazione.
    """
    created_at: datetime = pydantic.Field(default_factory=datetime.now)
    updated_at: datetime = pydantic.Field(default_factory=datetime.now)

class RubricaUpdateSchema(RubricaSchema):
    """
    Schema per l'aggiornamento di un contatto esistente nella rubrica telefonica, con validazione dei campi e formattazione dei dati.

    @updated_at: Data e ora dell'ultima modifica del contatto, impostata automaticamente al momento dell'aggiornamento.
    """
    updated_at: datetime = pydantic.Field(default_factory=datetime.now)

class RubricaDeleteSchema(pydantic.BaseModel):
    """
    Schema per la cancellazione di un contatto nella rubrica telefonica, con validazione del campo id.
    """
    id: int