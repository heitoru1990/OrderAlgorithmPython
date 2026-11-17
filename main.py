def main():
    orders = []

    # TODO: Some values, hard-coded, only to test the concept, once the read-file/read-DB system is implemented, remove this code
    orders.append({"Priority" : 1, "TimeEstimated" : 60})
    orders.append({"Priority" : 4, "TimeEstimated" : 70})
    orders.append({"Priority" : 2, "TimeEstimated" : 80})
    orders.append({"Priority" : 3, "TimeEstimated" : 10})
    orders.append({"Priority" : 4, "TimeEstimated" : 50})
    orders.append({"Priority" : 1, "TimeEstimated" : 5})
    orders.append({"Priority" : 5, "TimeEstimated" : 13})
    orders.append({"Priority" : 1, "TimeEstimated" : 10})
    orders.append({"Priority" : 2, "TimeEstimated" : 15})
    orders.append({"Priority" : 1, "TimeEstimated" : 8})
    # End of the Testing code

    totalUrgentOrders = 0
    totalTimeEstimated = 0.0
    averageTime = 0.0
    highestOrderTime = 0.0

    # Defines/Constants
    CRITICAL_TIME = 600
    ELEVATED_TIME = 480

    DEFAULT_ESTIMATED_TIME = 10

    if(len(orders) <= 0):
        print("Não existem dados sobre qualquer pedido, por favor adicione pedidos novos!")
        return

    highestOrderTime = orders[0]["TimeEstimated"]
    for order in orders:
        # First adjust the Priorities, if their values are invalid
        if(order["Priority"] < 1):
            order["Priority"] = 1

        if(order["Priority"] > 5):
            order["Priority"] = 5

        if(order["TimeEstimated"] <= 0):
            order["TimeEstimated"] = DEFAULT_ESTIMATED_TIME

        if(order["Priority"] < 3):
            totalUrgentOrders += 1

        estimated_time = order["TimeEstimated"]
        totalTimeEstimated += estimated_time

        if(highestOrderTime < estimated_time):
            highestOrderTime = estimated_time

    averageTime = totalTimeEstimated / len(orders)
    print(f"Nº de Pedidos Urgentes: {totalUrgentOrders}")
    print(f"Número total de minutos: {totalTimeEstimated}")
    print(f"Média dos minutos : {averageTime}")
    print(f"Maior Estimativa de Tempo: {highestOrderTime}")

    if(totalTimeEstimated > CRITICAL_TIME or totalUrgentOrders >= 5):
        print("CRITICA")
        return

    if(totalTimeEstimated > ELEVATED_TIME or totalUrgentOrders >= 3):
        print("ELEVADA")
        return

    print("NORMAL")

if __name__ == "__main__":
    main()