# Pós Graduação CDS – Fundamentos de Estatística
## Projeto do Aluno – dados da Olist			

A base de dados disponível no Kaggle (https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) é de um e-commerce brasileiro, com dados de 2016 a 2018 dos pedidos, dos produtos, dos clientes, vendedores e tempo de entrega. Este projeto visa criar dois modelos de regressão linear para prever a data de entrega e fazer testes de hipóteses para verificar se há diferença significante entre o tempo previsto pelo modelo e o tempo real de entrega em relação a algumas categorias de produtos.
A base total foi dividida em duas partes: 70% desenvolvimento e 30% validação.
Alterei as medidas do volume e do peso do produto de cm³ para litros, e de g para kg, respectivamente.

•	Analisando os dados de desenvolvimento (70%)  e validação (30%):

Percebe-se que a mediana, os quartis e o intervalo interquartílico não são sensíveis a outliers, permanecendo quase iguais em ambos os grupos de dados.

•	Histogramas:

Filtrei os dados até o 3 quartil + 1,5 IQR, a fim de excluir os outilers e plotar gráficos mais legíveis.

•	Correlação:

Mesmo com a transformação para o z_score, as correlações permaneceram as mesmas.

•	Modelos:

O primeiro modelo teve R² = 0.160 e equação:

 y = 7.57 + 0.01 * product_volume_l + 0.16 * product_weight_kg + 0.69 * dist_degrees

O segundo modelo, com as variáveis explicativas transformadas em z_score teve o mesmo R² = 0.160 e equação:

y = 11.92 + 0.24 * z_score_volume + 0.61 * z_score_weight + 3.73 * z_score_dist

•	Tempo de entrega preditos:

As previsões dos modelos 1 e 2 são próximas e mais assimétricas à direita do que a previsão do dataset.

•	Erro do dataset e dos modelos:
Os erros dos modelos são mais assimétricos à esquerda do que o erro do dataset, com desvio-padrão idênticos entre os erros dos modelos (8.698).

A média das previsões dos modelos (delta_time_model) estão quase idênticas ao tempo real de entrega (delta_time_real). Além disso, o desvio-padrão dos erros dos modelos (8.698) está menor do que o desvio-padrão do erro do dataset (10.211)
 
Portanto, mesmo com R² baixo, os dois modelos performaram melhor do que a previsão do dataset (delta_time_dataset).

•	Testes de Hipóteses:
Nível de significância de 5%:
1.	A categoria “casa_conforto_2ˮ tem uma média amostral maior do tempo real 
de espera do que a média de todo o conjunto de dados? 
Não há evidências suficientes para afirmar que a média da categoria é maior do que a média total. Aceita H0: média amostra <= média populacional.

2.	A categoria “livros_importadosˮ tem uma média amostral menor do tempo 
real de espera do que a média de todo o conjunto de dados?
A média do tempo real de espera da categoria “livros_importados” é significativamente menor do que a média total. Rejeita H0: média amostra >= média populacional

3.	A categoria “instrumentos_musicaisˮ tem uma média amostral diferente do 
tempo real de espera do que a média de todo o conjunto de dados?
Não há evidências suficientes para afirmar que a média da categoria “instrumentos musicais” é diferente da média total. Aceita H0: média amostra = média populacional
Nível de significância de 1%:
Nas categorias “cds_dvds_musicaisˮ, “flores”, “musica”, “artigos_de_festas” e “bebidas”, a média do tempo real de espera é diferente da média do tempo de espera predito pelo modelo 2? 
Aceita H₀: Não há evidências suficientes para afirmar que a média real de cada categoria é diferente da predita.
























