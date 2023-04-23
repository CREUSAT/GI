from sqlalchemy import create_engine, Column, Integer, String, Float, LargeBinary, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()


class Propriete(Base):
    __tablename__ = 'Proprietes'

    ID_Propriete = Column(Integer, primary_key=True)
    Nom_Propriete = Column(String(50))
    Adresse = Column(String(100))
    Taille = Column(Integer)
    Nb_Chambres = Column(Integer)
    Cout_Acquisition = Column(Float)
    Taxe1 = Column(Float)
    Taxe2 = Column(Float)
    ID_Locataires_louant = Column(String(50))
    photos = relationship('Photo', backref='propriete')

    def __repr__(self):
        return f"<Propriete(ID_Propriete='{self.ID_Propriete}', Nom_Propriete='{self.Nom_Propriete}', Adresse='{self.Adresse}', Taille='{self.Taille}', Nb_Chambres='{self.Nb_Chambres}', Cout_Acquisition='{self.Cout_Acquisition}', Taxe1='{self.Taxe1}', Taxe2='{self.Taxe2}', ID_Locataires_louant='{self.ID_Locataires_louant}')>"


class Photo(Base):
    __tablename__ = 'Photos'

    ID_Photo = Column(Integer, primary_key=True)
    ID_Propriete = Column(Integer)
    Image = Column(LargeBinary)
    Description = Column(String(100))

    __table_args__ = (ForeignKeyConstraint([ID_Propriete], ['Proprietes.ID_Propriete']), {})
    
    def __repr__(self):
        return f"<Photo(ID_Photo='{self.ID_Photo}', ID_Propriete='{self.ID_Propriete}', Description='{self.Description}')>"
