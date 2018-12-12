import json
from flask import jsonify, request
from app import es

analysis_attributes =["house_name","capacity","cost","description","landmark","apartment_type","property_type","city","purpose","review_count","rating_score","rating_frequency","address_details","state","street"]
sorting_attributes = ["cost","rating","date_updated"]