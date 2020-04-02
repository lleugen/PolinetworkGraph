# [PolinetworkGraph](lleugen.github.io/PolinetworkGraph)

This is a graph of the many [Telegram](telegram.org) groups of the [Polinetwork](polinetwork.github.io) built by/for the students of [Politecnico di Milano](polimi.it). Hopefuly this addition will be a useful tool for finding new groups to join.

###Tools used
[Telegram API](https://core.telegram.org/)
[Telethon](https://docs.telethon.dev/en/latest/)
[Gephi](https://gephi.org/)
[Sigma.js exporter for Gephi](https://gephi.org/plugins/#/plugin/sigmaexporter)

###Process
I used the telegram API to collect the necessary data (group names, number of participants and their ids). Then i computed for each pair of groups the number of members they have in common. I wrote this data into csv files which I then imported into Gephi, which allows to build a graph and has useful algorithms for adjusting the layout and computing statistics. I used Yifan Hu and Noverlap for layout and Modularity class for generating a node partition.

###Contributors
[Eugenio Ostrovan](github.com/lleugen)
