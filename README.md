# location_optimisation
The objective of this research is to identify optimal locations for Sheng Siong, a growing supermarket chain in Singapore. 

This work focuses on developing models, taking into consideration the various factors that influence the selection of an optimal store location.

Data for this research was collected from 2 main sources. Singapore sub-region data and population by sub-region was obtained from Data.gov.sg. Store location data of existing Sheng Siong stores and competitors, FairPrice and Giant stores, were obtained from their respective websites.

For this study, we consider the problem of optimally locating more than one new facility. 

Four different models were developed to analyze the influence of various factors in identifying optimum locations. Preliminary analysis showed that Singapore was divided in to 322 sub-regions. It was however noticed that there were several regions that had no or minimal population. To achieve a solution that is both optimal and practical, it was decided to set a threshold for population density of 0.01 per sub-region. By applying this threshold, the number of sub-regions were reduced to 279. 

To ensure that new store locations would
•	Cover the entire population (Maximum Coverage)
•	Minimize the distance of coverage of all the demand centers (p median problem)
•	Be closer to the Demand centers (weighted-p median problem)
•	Attract the population from the competitors’ stores (Gravity model)

Maximum Coverage, p median, weighted p median are executed using Lingo
Gravity Model is implemented using python

In the set covering approach, the objective value function of 62 indicates that the number of stores locations is 62. This includes the existing stores (35) in addition to new stores (27). Opening 27 new stores would ensure that areas where the population density is greater than 0.01 would have a Sheng Siong store within 2 kms of coverage radius.
Opening 27 new stores at once is neither a practical and nor a viable option for any organization, considering the manpower, budget and other resource limitations. Hence an interactive method was assumed for this scenario. It was assumed upon presenting and reviewing the findings from the first approach, the management of Sheng Siong would only be interested in finding the top 5 store locations.
In the P-median approach, the objective value obtained is 373.54. As the number new store locations is now restricted to 5, the objective function value represents the sum of distances from each sub-region to their respective store allocation. As the objective function was to minimize the total distance, this value obtained is in terms of km.
In the weighted p-median model, with inclusion of the weights of the demand points, which is the population in that region, the objective function works towards minimizing the total distances further based on population density. Hence an objective value of 13.88 km was obtained for this formulation.
For the gravity model, the greedy algorithm may depend on choices made so far, but not on future choices or all the solutions to the subproblem. It iteratively makes one greedy choice after another, reducing each given problem into a smaller one. In other words, a greedy algorithm never reconsiders its choices. Therefore the 13.59 billion choices were reduced to 1365 iterations. 
