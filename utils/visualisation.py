import matplotlib.pyplot as plt
from prettytable import PrettyTable


def visualisation(data, title):
    data.plot.barh(title=title, legend=None).invert_yaxis()
    plt.xlabel("Count")
    plt.ylabel("Token")
    plt.show()
    table = PrettyTable()
    table.title = title
    table.add_column("Token", data.index)
    table.add_column("Count", data.iloc[:, 0])
    print(table)
