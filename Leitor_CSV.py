import csv
from dataclasses import dataclass, asdict

# Molde do Aluno: dados estruturados para salvar e metodo para retornar
class Discente:
    def __init__(self, dados):
        self.matricula = dados['matricula']
        self.nome_discente = dados['nome_discente']
        self.ano_ingresso = dados['ano_ingresso']
        self.periodo_ingresso = dados['periodo_ingresso']
        self.tipo_discente = dados['tipo_discente']
        self.status_discente = dados['status_discente']
        self.nivel_ensino = dados['nivel_ensino']
        self.nome_curso = dados['nome_curso']
        self.modalidade_educacao = dados['modalidade_educacao']
        self.nome_unidade = dados['nome_unidade']
        self.nome_unidade_gestora = dados['nome_unidade_gestora']

    def get_dados(self):
        return {
            'matricula': self.matricula,
            'nome_discente': self.nome_discente,
            'ano_ingresso': self.ano_ingresso,
            'periodo_ingresso': self.periodo_ingresso,
            'tipo_discente': self.tipo_discente,
            'status_discente': self.status_discente,
            'nivel_ensino': self.nivel_ensino,
            'nome_curso': self.nome_curso,
            'modalidade_educacao': self.modalidade_educacao,
            'nome_unidade': self.nome_unidade,
            'nome_unidade_gestora': self.nome_unidade_gestora
        }

# Função para Ler o CSV e criar a Lista de Objetos
def ler_csv(arquivo):
    lista_discentes = []
    
    with open(arquivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for linha in reader:
            discente = Discente(linha)
            lista_discentes.append(discente)
    
    return lista_discentes

# Função para Imprimir um Aluno
def imprimir_aluno(discente):
    dados = discente.get_dados()
    
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")
    print("*" * 80)

# Função para Salvar TODA a lista em Arquivo TXT
def salvar_txt(discentes, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        
        for discente in discentes:
            dados = discente.get_dados()
            
            for campo, valor in dados.items():
                file.write(f"{campo}: {valor}\n")
            file.write("-" * 30 + "\n")
    return

def main():
    # Ler o arquivo CSV
    discentes = ler_csv('dis-csv-discentes-de-graduacao-de-2026.csv')
    
    # Imprimir um dicente
    indice_discente = input(f"Digite o índice do discente (0 a {len(discentes) - 1}): ")
    imprimir_aluno(discentes[int(indice_discente)])
    
    # Salvar em arquivo TXT
    salvar_txt(discentes, 'discentes.txt')
    print(f"\nArquivo TXT gerado! Total de alunos: {len(discentes)}")

# Start do arquivo
if __name__ == "__main__":
    main()
