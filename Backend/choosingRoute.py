from query_geonames import getNearestIntersection
from findroute import getRoutes, getDistances
from pathEvaluation import SafetyOfBlocks

def choose_minimal_path():

    all_routes = getRoutes()
    current_minimum_weight = 100000
    minimal_path = -1

    for i in range(len(all_routes)):
        intersection_street1JSON = getNearestIntersection()
        intersection_street1 = intersection_street1JSON.get("street1")

        intersection_street2JSON = getNearestIntersection()
        intersection_street2 = intersection_street1JSON.get("street2")

        start_street = all_routes[i][0]
        end_street = all_routes[i][len(all_routes[i]) - 1]

        if intersection_street1 == start_street:
            dif_intersection_street = intersection_street2
        else:
            dif_intersection_street = intersection_street1

        temporary_total_weight = []
        count = 1
        total_distances = getDistances()
        for j in range(0, len(all_routes[i]) - 1):
            temporary_total_weight.extend(SafetyOfBlocks(dif_intersection_street, start_street, end_street))
            dif_intersection_street = start_street
            start_street = end_street
            count += 1
            end_street = all_routes[i][count]

        temporary_total_weight *= total_distances[i]
        if current_minimum_weight > temporary_total_weight:
            minimal_path = i
            current_minimum_weight = temporary_total_weight

    return all_routes[minimal_path]










