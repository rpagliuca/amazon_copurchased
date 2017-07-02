# -*- coding: utf-8 -*-
# Author: Rafael Pagliuca
# Created at: 2016-11-07
# Modified at: 2016-11-07

from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
from common.graphtools import *

class Project2:

    # Generate filename and create directory if not exists
    def filename(self, shortname, filename):
        fullpath = '../output/' + shortname + '/' + filename
        # Borrowed from @Krumelur (http://stackoverflow.com/a/12517490/1501575)
        if not os.path.exists(os.path.dirname(fullpath)):
            try:
                os.makedirs(os.path.dirname(fullpath))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                        raise
        return fullpath

    # Define network databases files
    def __init__(self):
        self.networks = [
            [
                'lesmiserables',
                'Les Misérables',
                '../data/moreno_lesmis/out.moreno_lesmis_lesmis',
            ],
            [
                'airport',
                'US Airports',
                '../data/opsahl-usairport/out.opsahl-usairport',
            ],
            [
                'email',
                'E-mails',
                '../data/arenas-email/out.arenas-email',
            ],
            [
                'hamsterster',
                'Hamsterster friendships',
                '../data/petster-friendships-hamster/out.petster-friendships-hamster-uniq',
            ],
        ]

    # Run the scripts on every network
    def run(self):
        # Iterate through all networks
        for network in self.networks:

            # Current network
            [shortname, fullname, datafile] = network

            # Logging
            print ""
            print "=============================="
            print "Reading network " + fullname + "..."
            print ""

            # First we load the datafile and create a NetworkX object
            # Source: http://konect.uni-koblenz.de/networks/wordnet-words
            # Import TSV file using Pandas
            # TSV -> Tab Separated Values
            df = pd.read_table(datafile, sep=' ', header=None, comment='%')
            try:
                G = nx.from_pandas_dataframe(df, 0, 1, 2)
            except:
                G = nx.from_pandas_dataframe(df, 0, 1)
            # Advice from Francisco Rodrigues
            # G = nx.read_edgelist(datafile, nodetype=int, data=(("weight",float),))

            # Now we use the GraphTools class to generate some summary plots
            gt = GraphTools(G)
            gt.enable_logging()

            ###############################################################

            # Task 0.1 - Read network files
            # (Done above)

            # Task 0.2 - Extract the largest component
            # (Done on class GraphTools)

            ###############################################################

            # Task 1.1A - Plot k_nn(i) vs. k(i)
            gt.knni_vs_ki_plot(self.filename(shortname, '1-1A_knni_vs_ki.pdf'))

            # Task 1.1B - Plot k_nn(k) vs. k
            gt.knn_vs_k_plot(self.filename(shortname, '1-1B_knn_vs_k.pdf'))

            # Task 1.2A - Get assortativity coefficient. Present them on a table.
            gt.knn_vs_k_assortativity_coefficient(self.filename(shortname, '1-2A_knn_vs_k_assortativity_coefficient.txt'))
            # Task 1.2B - Get assortativity coefficient (my own implementation)
            gt.knn_vs_k_assortativity_coefficient_alternative(self.filename(shortname, '1-2B_knn_vs_k_assortativity_coefficient_own_implementation.txt'))

            # Task 1.3 - Discussion only

            # Task 1.4 - Discussion only

            # Task 1.5 - Get Pearson correlation coefficient for 1.1 
            gt.knn_vs_k_pearson_correlation_coefficient(self.filename(shortname, '1-5_knn_vs_k_pearson_correlation_coefficient.txt'))

            # Task 1.6 - Get Spearman correlation coefficient for 1.1 
            gt.knn_vs_k_spearman_correlation_coefficient(self.filename(shortname, '1-6_knn_vs_k_spearman_correlation_coefficient.txt'))

            # Task 1.7 - Discussion only

            ###############################################################

            # Task 2.1 - Plot probability distribution of Degree
            gt.degree_distribution(self.filename(shortname, '2-1_degree_distribution.pdf'))

            # Task 2.2 - Plot probability distribution of Betweeness Centrality 
            gt.betweenness_centrality_distribution(self.filename(shortname, '2-2_betweenness_centrality_distribution.pdf'))

            # Task 2.3 - Plot probability distribution of Eigenvector Centrality
            gt.eigenvector_centrality_distribution(self.filename(shortname, '2-3_eigenvector_centrality_distribution.pdf'))

            # Task 2.4 - Plot probability distribution of Closeness Centrality
            gt.closeness_centrality_distribution(self.filename(shortname, '2-4_closeness_centrality_distribution.pdf'))

            # Task 2.5 - Plot probability distribution of PageRank
            gt.pagerank_distribution(self.filename(shortname, '2-5_pagerank_distribution.pdf'))

            ###############################################################

            # Task 3.1 - Plot scatterplot Degree vs. Betweenness Centrality (print Pearson correlation)
            # Create histograms with the same size, so it is possible to plot a scatterplot
            gt.plot_degree_vs_betweenness(self.filename(shortname, '3-1A_plot_degree_vs_betweenness.pdf'))
            gt.print_degree_vs_betweenness_correlation(self.filename(shortname, '3-1B_degree_vs_betweenness_correlation.txt'))

            # Task 3.2 - Plot scatterplot PageRank vs. Closeness Centrality (print Pearson correlation)
            # The same as above
            gt.plot_pagerank_vs_closeness(self.filename(shortname, '3-2A_plot_pagerank_vs_closeness_correlation.pdf'))
            gt.print_pagerank_vs_closeness_correlation(self.filename(shortname, '3-2B_pagerank_vs_closeness_correlation.txt'))

            # Task 3.3 - Discussion only

            ###############################################################

            # Task 4.1 - Random walk with 1000 steps. Repeat experiment 10 times. Print number of visits on each node.
            gt.plot_random_walk_visits_vs_degree(self.filename(shortname, '4-1_random_walk_visits_vs_degree.pdf'))
            
            # Task 4.2 - Random walk with 1000 steps. Repeat experiment 10 times. Print number of visits on each node.
            gt.plot_random_walk_visits_vs_eigenvector_centrality(self.filename(shortname, '4-2_random_walk_visits_vs_eigenvector_centrality.pdf'))

# Instantiate class and run
project2 = Project2()
project2.run()
print 'Done.'