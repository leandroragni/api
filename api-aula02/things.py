# things.py

import falcon
import json

class ThingsResource(object):
    def on_get(self, req, resp):
        alunos = [
            {
                'id': 1,
                'nome': 'Leandro',
                'idade': 36
            },
            {
                'id': 2,
                'nome': 'Synapse',
                'idade': 22
            },
            {
                'id': 3,
                'nome': 'Python',
                'idade': 10
            }
        ]

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(students)

    def on_get(self, req, resp, id):

        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        alunos = [
            {
                'id': 1,
                'nome': 'Leandro',
                'idade': 36
            },
            {
                'id': 2,
                'nome': 'Synapse',
                'idade': 22
            },
            {
                'id': 3,
                'nome': 'Python',
                'idade': 10
            }
        ]

        resposta = {}

        for aluno in alunos:
            if aluno['id'] == identificador:
                resposta = aluno


        resp.status = falcon.HTTP_200
        resp.body = json.dumps(resposta)
    
    def on_post(self, req, resp):
        alunos = [
            {
                'id': 1,
                'nome': 'Leandro',
                'idade': 36
            },
            {
                'id': 2,
                'nome': 'Synapse',
                'idade': 22
            },
            {
                'id': 3,
                'nome': 'Python',
                'idade': 10
            }
        ]

        novoAluno = json.loads(req.stream.read().decode('utf-8'))
        alunos.append(novoAluno)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(alunos)

    def on_put(self, req, resp, id):
        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        alunos = [
            {
                'id': 1,
                'nome': 'Leandro',
                'idade': 36
            },
            {
                'id': 2,
                'nome': 'Synapse',
                'idade': 22
            },
            {
                'id': 3,
                'nome': 'Python',
                'idade': 10
            }
        ]

        alunoAlterado = json.loads(req.stream.read().decode('utf-8'))

        for index, aluno in enumerate(alunos):
            if aluno['id'] == identificador:
                alunos[index]['nome'] = alunoAlterado['nome']
                alunos[index]['idade'] = alunoAlterado['idade']

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(alunos)

    def on_delete(self, req, resp, id):
        try:
            identificador = int(id)
        except:
            erro = {
                'mensagem': 'Id informado invalido'
            }
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(erro)
            return

        alunos = [
            {
                'id': 1,
                'nome': 'Leandro',
                'idade': 36
            },
            {
                'id': 2,
                'nome': 'Synapse',
                'idade': 22
            },
            {
                'id': 3,
                'nome': 'Python',
                'idade': 10
            }
        ]

        for index, aluno in enumerate(alunos):
            if aluno['id'] == identificador:
                alunos.pop(index)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(alunos)

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/things/{id}', things)