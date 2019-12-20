import sys
sys.path.append('C:/Users/900224/Desktop/Aula13/Estrutura Cotacao/')
from model.papel import Papel
from dao.papel_dao import PapelDao
from dao.tipo_dao import TipoPapelDao
from dao.cotacao_diaria_dao import CotacaoDiariaDao
from model.cotacao_diaria import CotacaoDiaria

dao = PapelDao()
dao_tipo = TipoPapelDao()
cot_dao = CotacaoDiariaDao()

# papel = Papel()
# papel.codigo = 'Teste'
# papel.descricao = 'testes'
# papel.tipo_id = 2
#dao.insert(papel)

# papel = Papel()
# papel.codigo = 'Teste2'
# papel.descricao = 'testes2'
# papel.tipo_id = 2
# papel.id=10

#dao.insert(papel)
#dao.update(papel)
#dao.delete(9)

#Criando uma lista que recebe 
lista = cot_dao.list_all()
for p in lista:
    pl = p.valor_fechamento/p.lpa
    p.pl= pl


lista = sorted(lista, key = CotacaoDiaria.get_pl)

for c in lista:
    print(f'Codigo: {c.papel.codigo} - Descrição: {c.papel.descricao} - Fechamento: {c.valor_fechamento} - LPA: {c.lpa} - PL :{c.pl}')



