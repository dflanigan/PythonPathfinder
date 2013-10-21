#! /usr/bin/env python

from list_things import show_furniture

import house.bedroom
import house.kitchen
import house.living_room


show_furniture(house.bedroom.furniture)
show_furniture(house.kitchen.furniture)
show_furniture(house.living_room.furniture)
