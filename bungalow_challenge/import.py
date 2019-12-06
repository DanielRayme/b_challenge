# Quick and dirty import script. Manual validation of some of the data :/

import csv
import datetime
from bungalow.models import PropertyModel  # imports the model
with open('challenge_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row["last_sold_date"]):
            row["last_sold_date"] = datetime.datetime.strptime(
                row["last_sold_date"], '%m/%d/%Y').strftime('%Y-%m-%d')
        else:
            row["last_sold_date"] = None
        if (row["rentzestimate_last_updated"]):
            row["rentzestimate_last_updated"] = datetime.datetime.strptime(
                row["rentzestimate_last_updated"], '%m/%d/%Y').strftime('%Y-%m-%d')
        else:
            row["rentzestimate_last_updated"] = None
        if (not row["last_sold_price"]): row["last_sold_price"] = None
        if (not row["rent_price"]): row["rent_price"] = None
        if (not row["zestimate_amount"]): row["zestimate_amount"] = None
        if (not row["home_size"]): row["home_size"] = None
        if (not row["property_size"]): row["property_size"] = None
        if (not row["year_built"]): row["year_built"] = None
        if (not row["bathrooms"]): row["bathrooms"] = None
        if (not row["rentzestimate_amount"]): row["rentzestimate_amount"] = None
        p = PropertyModel(** row)
        p.save()
