from flask import Blueprint

from geonamesIntersection import getNearestIntersection
from findroute import getRoutes, getDistances, getCornerCoords
from pathEvaluation import SafetyOfBlocks
from getCoords import getCoords

routes_page = Blueprint('routes_page', __name__)


@routes_page.route("/optimal")
def choose_minimal_path():
    #coords = getCoords()
    coords = [(37.763884, -122.450358), (37.761578217554515, -122.4516110576457)]
    all_routes = getRoutes(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
    current_minimum_weight = 100000
    minimal_path = -1

    for i in range(len(all_routes)):
        intersection_street1JSON = getNearestIntersection(coords[0][0], coords[0][1])
        intersection_street1 = intersection_street1JSON.get("intersection").get("street1")
        print(intersection_street1)

        intersection_street2JSON = getNearestIntersection(coords[0][0], coords[0][1])
        intersection_street2 = intersection_street1JSON.get("intersection").get("street2")

        intersection_street3JSON = getNearestIntersection(coords[1][0], coords[1][1])
        intersection_street3 = intersection_street3JSON.get("intersection").get("street1")

        intersection_street4JSON = getNearestIntersection(coords[1][0], coords[1][1])
        intersection_street4 = intersection_street4JSON.get("intersection").get("street2")

        start_street = all_routes[i][0]
        end_street = all_routes[i][len(all_routes[i]) - 1]

        if intersection_street1 == start_street:
            dif_intersection_street = intersection_street2
        else:
            dif_intersection_street = intersection_street1

        if intersection_street3 == all_routes[i][-1]:
            all_routes[i].append(intersection_street4)
        else:
            all_routes[i].append(intersection_street3)

        temporary_total_weight = []
        count = 1
        total_distances = getDistances(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
        all_safety_weights = []
        for j in range(len(all_routes[i]) - 1):
            temporary_total_weight.extend(SafetyOfBlocks(dif_intersection_street, start_street, end_street))
            dif_intersection_street = start_street
            start_street = end_street
            end_street = all_routes[i][count]
            count += 1

        temp_avg = sum(temporary_total_weight)/len(temporary_total_weight)
        temporary_total_weight = float(total_distances[i]) * float(temp_avg)
        all_safety_weights.append(temporary_total_weight)
        if current_minimum_weight > temporary_total_weight:
            minimal_path = i
            current_minimum_weight = temporary_total_weight



    return getCornerCoords(i, coords[0][0], coords[0][1], coords[1][0], coords[1][1])











