from database import db
import requests

class Atividade(db.Model):
    __tablename__ = 'atividades'
    id_atividade = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.Text, nullable=True)
    respostas = db.relationship('Resposta', backref='atividade', cascade='all, delete-orphan')


class Resposta(db.Model):
    __tablename__ = 'respostas'
    id_resposta = db.Column(db.Integer, primary_key=True)
    resposta = db.Column(db.Text, nullable=True)
    nota_atividade = db.Column(db.Float, nullable=True)
    id_atividade = db.Column(db.Integer, db.ForeignKey('atividades.id_atividade'), nullable=False)
    id_aluno = db.Column(db.Integer, nullable=True)

class AtividadeNotFound(Exception):
    pass

def obter_nome_aluno(id_aluno):
    try:
        response = requests.get(f'http://localhost:5000/api/alunos/{id_aluno}')
        if response.status_code == 200:
            return response.json().get('nome', 'Desconhecido')
    except requests.RequestException:
        pass
    return 'Desconhecido'


def listar_atividades():
    atividades = Atividade.query.all()
    return [{
        'id_atividade': a.id_atividade,
        'enunciado': a.enunciado,
        'respostas': [
            {
                'id_aluno': r.id_aluno,
                'nome_aluno': obter_nome_aluno(r.id_aluno),
                'resposta': r.resposta,
                'nota': r.nota_atividade
            } for r in a.respostas
        ]
    } for a in atividades]

def obter_atividade(id_atividade):
    atividade = Atividade.query.get(id_atividade)
    if not atividade:
        raise AtividadeNotFound

    return {
        'id_atividade': atividade.id_atividade,
        'enunciado': atividade.enunciado,
        'respostas': [
            {
                'id_aluno': r.id_aluno,
                'nome_aluno': obter_nome_aluno(r.id_aluno),
                'resposta': r.resposta,
                'nota': r.nota_atividade
            } for r in atividade.respostas
        ]
    }