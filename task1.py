import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("T1", "S1", 25), ("T1", "S2", 20), ("T1", "S3", 15),
    ("T2", "S3", 15), ("T2", "S4", 30), ("T2", "S2", 10),
    ("S1", "M1", 15), ("S1", "M2", 10), ("S1", "M3", 20),
    ("S2", "M4", 15), ("S2", "M5", 10), ("S2", "M6", 25),
    ("S3", "M7", 20), ("S3", "M8", 15), ("S3", "M9", 10),
    ("S4", "M10", 20), ("S4", "M11", 10), ("S4", "M12", 15),
    ("S4", "M13", 5), ("S4", "M14", 10),
]


G.add_edge("source", "T1", capacity=1000)
G.add_edge("source", "T2", capacity=1000)

for from_node, to_node, capacity in edges:
    G.add_edge(from_node, to_node, capacity=capacity)

    if to_node.startswith("M"):
        G.add_edge(to_node, "sink", capacity=capacity)

flow_value, flow_dict = nx.maximum_flow(G, "source", "sink")

print("Максимальний потік:", flow_value)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(16, 12))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'capacity')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
plt.title("Граф логістичної мережі")
plt.show()

'''
Аналіз результатів
Найбільший потік забезпечує Термінал 1 — 60 одиниць

Маршрути з найменшою пропускною здатністю:

S4 → M13 (5 одиниць) — цей маршрут взагалі не використаний.

S4 → M14 (10 одиниць) — також не використаний.

S3 → M9 (10 одиниць) — не використаний.
Це створює вузькі місця, і навіть частина потужностей складів не була використана повністю.

Магазини з найменшим постачанням:

M3, M9, M12, M13, M14 — отримали 0 одиниць.
'''