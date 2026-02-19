from fastapi import APIRouter
from dal import get_alerts_by_border_and_priority, get_top_urgent_zones, get_distance_distribution, get_low_visibility_high_activity, get_hot_zones




route = APIRouter(prefix="/analytics")

@route.get('/alerts-by-border-and-priority')
def alerts_by_border_and_priority():
    return get_alerts_by_border_and_priority()

@route.get('/top-urgent-zones')
def top_urgent_zones():
    return get_top_urgent_zones()

@route.get('/distance-distribution')
def distance_distribution():
    return get_distance_distribution()

@route.get('/low-visibility-high-activity')
def low_visibility_high_activity():
    return get_low_visibility_high_activity()

@route.get('/hot-zones')
def hot_zones():
    return get_hot_zones()