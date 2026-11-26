"""Banco SQLite, modelos ORM e dados fictícios para demonstração acadêmica."""
from datetime import date, datetime
from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DB = Path(__file__).resolve().parent / "healthbridge.db"
engine = create_engine(f"sqlite:///{DB}", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String(160), nullable=False)
    birth = Column(Date, nullable=False)
    blood = Column(String(8), default="Não informado")
    sex = Column(String(30), default="Não informado")
    allergies = Column(Text, default="")
    conditions = Column(Text, default="")
    meds = Column(Text, default="")
    status = Column(String(30), default="Estável")
    consent = Column(Boolean, default=False)
    consent_date = Column(String(60), default="Pendente")
    created_at = Column(DateTime, default=datetime.utcnow)
    records = relationship("Record", back_populates="patient", cascade="all, delete-orphan")

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    kind = Column(String(60), nullable=False)
    record_date = Column(Date, nullable=False)
    summary = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient", back_populates="records")

class Audit(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    action = Column(String(120), nullable=False)
    resource = Column(String(160), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

def initialize_database():
    """Cria tabelas e insere registros estritamente fictícios na primeira execução."""
    Base.metadata.create_all(engine)
    session = Session()
    try:
        if session.query(Patient).count() == 0:
            seed_patients = [
              ("Ana Lima","1984-04-12","O+","Feminino",["Penicilina"],["Hipertensão"],["Losartana"],True,"Acompanhamento",[("Consulta","2026-11-25","Revisão de acompanhamento e aferição de pressão."),("Exame","2026-11-18","Exames de rotina registrados.")]),
              ("Carlos Mendes","1959-07-08","A+","Masculino",["AAS"],["Diabetes","Hipertensão"],["Metformina","Losartana","AAS","Sinvastatina"],True,"Atenção",[("Consulta","2026-11-24","Acompanhamento de condição crônica."),("Internação","2026-10-10","Registro fictício de internação recente.")]),
              ("Beatriz Souza","1997-02-19","AB-","Feminino",[],[],[],True,"Estável",[("Consulta","2026-11-23","Consulta de rotina.")]),
              ("João Pereira","1975-09-22","B+","Masculino",["Dipirona"],["Asma"],["Salbutamol"],False,"Estável",[("Consulta","2026-11-21","Atualização de dados essenciais.")]),
              ("Sofia Almeida","1953-01-05","O-","Feminino",["Látex"],["Diabetes"],["Metformina","Insulina"],True,"Atenção",[("Consulta","2026-11-20","Acompanhamento clínico.")]),
            ]
            for n,b,bl,sex,allg,cond,meds,cons,st,records in seed_patients:
                patient = Patient(name=n, birth=date.fromisoformat(b), blood=bl, sex=sex,
                    allergies=", ".join(allg), conditions=", ".join(cond), meds=", ".join(meds),
                    consent=cons, consent_date="Demo: consentimento concedido" if cons else "Demo: revogado", status=st)
                session.add(patient)
                session.flush()
                for typ,dt,summary in records:
                    session.add(Record(patient_id=patient.id, kind=typ, record_date=date.fromisoformat(dt), summary=summary))
            for action,resource in [("Consulta de paciente","Ana Lima"),("Consentimento atualizado","João Pereira"),("Registro criado","Carlos Mendes")]:
                session.add(Audit(action=action, resource=resource))
            session.commit()
    finally:
        session.close()

initialize_database()
