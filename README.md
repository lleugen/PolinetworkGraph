# [PolinetworkGraph](https://lleugen.github.io/PolinetworkGraph/)

This is a graph of the many [Telegram](https://telegram.org/) groups of the [Polinetwork](https://polinetwork.github.io/it/index.html) built by/for the students of [Politecnico di Milano](https://www.polimi.it/). Hopefuly this addition will be a useful tool for finding new groups to join.

### Tools used
[Telegram API](https://core.telegram.org/)
[Telethon](https://docs.telethon.dev/en/latest/)
[Gephi](https://gephi.org/)
[Sigma.js exporter for Gephi](https://gephi.org/plugins/#/plugin/sigmaexporter)

### Process
I used the telegram API to collect the necessary data (group names, number of participants and their ids). Then I computed for each pair of groups the number of members they have in common. I wrote this data into csv files which I then imported into Gephi, which allows to build a graph and has useful algorithms for adjusting the layout and computing statistics. I used Yifan Hu and Noverlap for layout and Modularity class for generating a node partition. Finally I exported the graph using the sigma.js plugin. You can test it locally by setting up a simple server (example in [server.py]) (simply opening the index.html file in the browser doesn't work because of security issues)

### Contributors
[Eugenio Ostrovan](https://github.com/lleugen)
