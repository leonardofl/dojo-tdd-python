from datetime import date

QUADRIENIO = "QUADRIENIO"
BIENIO = 'BIENIO'
ANO = 'ANO'
SEMESTRE = 'SEMESTRE'

PERIODICIDADES = [QUADRIENIO, BIENIO, ANO, SEMESTRE]

MUNICIPAL = 'MUNICIPAL'
ESTADUAL = 'ESTADUAL'
FEDERAL = 'FEDERAL'

ESFERAS = [MUNICIPAL, ESTADUAL, FEDERAL]

class PeriodosRetriever:

    def get_periodos(self, esfera, periodicidade, data_inicial, data_final=None):
        """O Radar Parlamentar precisa determinar um conjunto de períodos de análise para seu usuário.
           O tamanho de cada período (periodicidade) é definido pelo usuário.
           O período mais antigo é o período mais recente que contém a primeira votação da casa legislativa.
           O período mais recente é aquele que contém a data corrente.
           A determinação da data da primeira votação está abstraída nesse exemplo, já recebemos data_inicial.
           O ponto central do problema é que um período de análise não pode atravessar as fronteiras de uma legislação,
           pois não faz sentido rodar o algoritmo de clusterização com votações ocorridas em épocas em que as composições
           da casa legislativa diferiam totalmente.
           Exemplo: não podemos fazer uma única análise PCA juntando votos do senado ocorridos tanto no governo FHC quanto no governo Lula.
           O código original do Radar Parlamentar está aqui: https://github.com/radar-parlamentar/radar/blob/master/radar_parlamentar/modelagem/utils.py
           Argumentos:
                esfera - string em ESFERAS, define possíveis datas de início de períodos.
                periodicidade - string em PERIODICIDADES, define os tamanho dos períodos retornados.
                data_inicial - datetime.date.
                data_final - datetime.date; se não especificado, corresponde a data corrente.
            Retorno:
                Lista de períodos contínuos englobando data_inicial e data_final.
                Cada período é uma tupla de datetime.date,
                onde a primeira data é a data inicial do período e a segunda data é a data final do período.
        """
        self.esfera = esfera
        self.periodicidade = periodicidade
        self.data_inicial = data_inicial
        dia_inicial = 1
        mes_inicial = 1
        dia_final = 31
        mes_final = 12

        ano_inicial = self._get_ano_inicial()

        if periodicidade == QUADRIENIO:
            ano_final = ano_inicial + 3
        if periodicidade == BIENIO:
            ano_final = ano_inicial + 1
        if periodicidade == ANO or periodicidade == SEMESTRE:
            ano_final = ano_inicial

        data_inicio_periodo = date(ano_inicial, mes_inicial, dia_inicial)
        data_fim_periodo = date(ano_final, mes_final, dia_final)
        return [(data_inicio_periodo, data_fim_periodo)]

    def _get_ano_inicial(self):
        if self.esfera == FEDERAL or self.esfera == ESTADUAL:
            ano_referencia = 2011
        if self.esfera == MUNICIPAL:
            ano_referencia = 2009
        ano_referencia = ano_referencia - 4 * 500
        if self.periodicidade == QUADRIENIO:
            multiplo = 4
        elif self.periodicidade == BIENIO:
            multiplo = 2
        else:
            multiplo = 1
        defasagem = (abs(ano_referencia - self.data_inicial.year)) % multiplo
        return self.data_inicial.year - defasagem
