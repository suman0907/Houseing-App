from . import test
import uuid
from utils import *
from flask import jsonify, request
from app import es
from app.settings import *
from information import ES_DREAMHOUSE_INDEX
DREAMHOUSE_DOC_NAME = "Property"

@test.route('/', methods=['GET'])
def tes():
    return jsonify({"msg" : "welcome to your dream house"})


def init_dream(app):
    #es.indices.delete(ES_DREAMHOUSE_INDEX, ignore=[400, 404])

    body = {

        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "analyzer_shingle_snow": {
                            "tokenizer": "standard",
                            "filter": [
                                "standard",
                                "lowercase",
                                "filter_snow",
                                "filter_shingle"
                            ]
                        },
                        "analyzer_snow": {
                            "tokenizer": "keyword",
                            "filter": [
                                "standard",
                                "lowercase",
                                "filter_snow"
                            ]
                        }
                    },
                    "filter": {
                        "filter_shingle": {
                            "type": "shingle",
                            "max_shingle_size": 5,
                            "min_shingle_size": 2,
                            "output_unigrams": "true"
                        },
                        "filter_snow": {
                            "type": "snowball",
                            "language": "English"
                        }
                    }
                }
            }
        },

        "mappings":  # keyword
            {
                "Property":  # doc type name(table name)
                    {
                        "properties":  # property of doc type
                            {

                                "house_name":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "house_name_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "capacity":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "capacity_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "cost":
                                    {
                                        "type": "integer",
                                        "index": "not_analyzed"


                                    },
                                "cost_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },

                                "description":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "description_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "landmark":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "landmark_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },

                                "apartment_type":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "apartment_type_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },

                                "property_type":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "property_type_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "city":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "city_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },

                                "profile_image":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "review_count":
                                    {
                                        "type": "integer",
                                        "index": "not_analyzed"
                                    },
                                "review_count_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },

                                "rating_score":
                                    {
                                        "type": "float",
                                        "index": "not_analyzed"

                                    },
                                "rating_score_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "rating_frequency":
                                    {
                                        "type": "integer",
                                        "index": "not_analyzed"
                                    },
                                "rating_frequency_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"
                                    },
                                "brokery":
                                    {
                                        "type": "boolean",
                                        "index": "not_analyzed"
                                    },
                                "purpose":
                                    {
                                        "type": "string",
                                        "index": "not_analyzed"

                                    },
                                "purpose_analyzed":
                                    {
                                        "type": "string",
                                        "analyzer": "analyzer_snow"

                                    },

                                "broker_info":
                                    {
                                        "properties":
                                            {
                                                "broker_name":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    },
                                                "address":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    },
                                                "contact_no":
                                                    {
                                                        "type": "integer",
                                                        "index": "not_analyzed"
                                                    }

                                            }

                                    },

                                "images":
                                    {

                                        "properties":
                                            {
                                                "image_date":
                                                    {
                                                        "type": "date",
                                                        "index": "not_analyzed"
                                                    },
                                                "image_url":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    }

                                            }

                                    },

                                "review":
                                    {

                                        "properties":
                                            {
                                                "review_date":
                                                    {
                                                        "type": "date",
                                                        "index": "not_analyzed"

                                                    },

                                                "review_text":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    }

                                            }

                                    },

                                "address":
                                    {
                                        "properties":
                                            {
                                                "address_details":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"

                                                    },
                                                "address_details_analyzed":
                                                    {
                                                        "type": "string",
                                                        "analyzer": "analyzer_snow"
                                                    },
                                                "city":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    },
                                                "city_analyzed":
                                                    {
                                                        "type": "string",
                                                        "analyzer": "analyzer_snow"
                                                    },

                                                "state":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    },
                                                "state_analyzed":
                                                    {
                                                        "type": "string",
                                                        "analyzer": "analyzer_snow"
                                                    },
                                                "street":
                                                    {
                                                        "type": "string",
                                                        "index": "not_analyzed"
                                                    },
                                                "street_analyzed":
                                                    {
                                                        "type": "string",
                                                        "analyzer": "analyzer_snow"
                                                    },

                                            }

                                    },

                            },

                    }

            }
    }
    es.indices.create(index=ES_DREAMHOUSE_INDEX, body=body, ignore=400)  # index=db name


@test.route('/add_update_house', methods=['POST'])
def add_update_house():
    requestObject = request.get_json()
    try:
        if "id" not in requestObject:
            ids = str(uuid.uuid4()) #generates a unique random id which is defined under uuid(python library)
            requestObject['date_added'] = getCurrentTime()
            requestObject['date_modified'] = getCurrentTime()
            requestObject['mod_status'] = "Approval_pending"


            for analysis in analysis_attributes:
                if analysis in requestObject['address']:
                    mod_key = analysis + "_analyzed"
                    requestObject['address'][mod_key] = requestObject['address'][analysis]


            for analysis in analysis_attributes:
                if analysis in requestObject:
                    mod_key = analysis + "_analyzed"
                    if analysis == 'cost':
                        requestObject[mod_key] = str(requestObject[analysis])
                    if analysis == 'review_count':
                        requestObject[mod_key] = str(requestObject[analysis])
                    if analysis == 'rating_score':
                        requestObject[mod_key] = str(requestObject[analysis])
                    if analysis == 'rating_frequency':
                        requestObject[mod_key] = str(requestObject[analysis])
                    requestObject[mod_key] = requestObject[analysis]

            es.index(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=ids, body=requestObject )
            return jsonify({"response": "success", "id": ids})

        else:
            requestObject['date_modified'] = getCurrentTime()
            es.update(
                index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=str(requestObject['id']),
                body={

                    "doc": requestObject
                }
            )
            return jsonify({"response": "success", "id": str(requestObject['id'])})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})


@test.route('/add_moderation', methods=['POST'])
def add_moderation():
    requestObject = request.get_json()
    try:


        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        id=requestObject['id'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        if requestObject['mod_status'] == "Approved":
            result['mod_status'] = "Approved"
        else:
            result['mod_status'] = "Rejected"

        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success"})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})



@test.route('/add_broker_info', methods=['POST'])
def add_broker_info():
    requestObject = request.get_json()
    try:

        ids = str(uuid.uuid4())
        requestObject['brokerId'] = ids
        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        id=requestObject['id'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        result['broker_info'] = {}
        result['broker_info'] = requestObject



        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success", "id": ids})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})




@test.route('/add_house_images', methods=['POST'])
def add_house_images():
    requestObject = request.get_json()
    try:
        ids = str(uuid.uuid4())
        requestObject['imageId'] = ids
        requestObject['image_date'] = getCurrentTime()

        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        id=requestObject['id'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        if 'images' not in result:
            result['images'] = []

        result['images'].append(requestObject)

        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success", "imageId": ids})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})



@test.route('/add_house_address', methods=['POST'])
def add_house_address():
    requestObject = request.get_json()
    try:

        ids = str(uuid.uuid4())
        requestObject['addressId'] = ids
        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        id=requestObject['id'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        result['address'] = {}
        result['address'] = requestObject



        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success", "addressId": ids})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})





@test.route('/add_rating', methods=['POST'])
def add_rating():
    requestObject = request.get_json()
    try:


        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        id=requestObject['id'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        if 'rating_score' not in result:

             result['rating_frequency'] = 1
             result['rating_score'] = requestObject['rating_score']
        else :
            result['rating_frequency'] = result['rating_frequency'] + 1
            result['rating_score'] = (requestObject['rating_score'] + ( result['rating_score']*(result['rating_frequency']-1)) )/float(result['rating_frequency'])



        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success"})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})


@test.route('/add_review', methods=['POST'])
def add_review():
    requestObject = request.get_json()
    try:
        ids = str(uuid.uuid4())
        requestObject['reviewId'] = ids
        requestObject['review_date'] = getCurrentTime()
        result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                        houseId=requestObject['houseId'])
        if result["found"] == False:
            return jsonify({"response": "failure", "error": "No house with given id"})
        result = result.get('_source')
        if 'review' not in result:
            result['review_count']= 1
            result['review'] = []
            result['review'].append(requestObject)
        else :
            result['review_count'] = result['review_count'] +1
            result['review'].append(requestObject)


        es.update(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                  id=requestObject['id'], body={"doc": result})

        return jsonify({"response": "success", "reviewId": ids})
    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})




@test.route('/get_house_by_id',methods=['GET'])
def get_house_by_id():
   idp = request.args["houseId"]
   try:

       query = {
           "query":
               {
                   "bool":
                       {
                           "must":
                               [

                                   {"match_phrase": {"mod_status": "Approved"}},
                                   {"match_phrase": {"_id": idp}},

                               ]

                       }

               }

       }
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=query)

       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']



           return jsonify({"response": "success", "data": result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/multi_filter', methods=['GET'])
def multi_filter():
    city = request.args.get('city', default="")
    cost_gte = request.args.get('cost_max', default="")
    cost_lte = request.args.get('cost_min', default="")
    capacity = request.args.get('capacity', default="")
    apartment_type = request.args.get('apartment_type', default="")
    property_type = request.args.get('property_type', default="")
    purpose = request.args.get('purpose', default="")


    try:

        city = city.split(",")
        capacity = capacity.spilt(",")
        apartment_type = apartment_type.split(",")
        property_type = property_type.split(",")
        purpose = purpose.split(",")


        keys = {

            "city":city,
            "capacity": capacity,
            "apartment_type": apartment_type,
            "property_type":property_type,
            "purpose": purpose
        }

        res_list = []


        for i in keys:

            if keys[i] != '':
                dummy = {"terms": {i: keys[i]}}
                res_list.append(dummy)

        dummy2 = {"term": {"mod_status": "Approved"}}
        dummy3 = {

                "range":{
                    "cost":{
                        "gte":cost_gte,
                        "lte":cost_lte
                    }
                }

        }

        res_list.append(dummy2)
        res_list.append(dummy3)


        query = {

            "query":{
            "bool":{

            "must": {
                "match_all": {}
            },
             "filter":{
                 "bool":{
                     "must":res_list,



                 }

             },

              }
            }
        }
        result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=query)
        res = result["hits"]["hits"]
        filtered_result = []

        for x in res:
            fin = x['_source']
            ab = x['_id']
            fina = {}
            fina['profile_image'] = fin['profile_image']
            fina['address'] = fin['address']['address_details']
            fina['cost'] = fin['cost']
            fina['capacity'] = fin['capacity']
            fina['id'] = ab
            filtered_result.append(fina)

        return jsonify({"response": "success", "data": filtered_result})

    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})





@test.route('/search_houses', methods=['GET'])
def search_question_mod():
    search = request.args["query"]
    page_num = request.args.get('page',default=0)
    page_count = 0


    try:
        question_query_count = {


            "query": {

                "bool": {
                    "must": [

                        {"query_string": {

                            "query": search,
                        }},

                        {"match_phrase": {"mod_status": "Approved", }}

                    ],

                    "should":
                        [
                            {"multi_match":
                                {
                                    "query": search,
                                    "type": "most_fields",
                                    "fields": ["house_name","capacity","cost","description","landmark","apartment_type","property_type",
                                               "city","purpose","review_count","rating_score","rating_frequency","address_details"
                                               ]
                                }},

                        ],
                }}}

        res = es.count(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                           body=question_query_count ,ignore=404)

        k = res["count"]


        if 'page' not in request.args:
            page_number = 0
        else:
            page_number = int(page_num) - 1

        question_query = {
            "from": page_number * 10, "size": (page_number * 10) + 10,

            "query": {

                "bool": {
                    "must": [

                        {"query_string": {

                            "query": search,
                        }},
                        {"match_phrase": {"mod_status": "Approved", }}


                    ],

                    "should":
                        [
                            {"multi_match":
                                {
                                    "query": search,
                                    "type": "most_fields",
                                    "fields": ["house_name","capacity","cost","description","landmark","apartment_type","property_type",
                                               "city","purpose","review_count","rating_score","rating_frequency","address_details"
                                             ]
                                }},


                        ],
                    }}}

        result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,
                           body=question_query)

        res = result["hits"]["hits"]

        filtered_result = []
        for x in res:
            fin = x['_source']
            ab = x['_id']
            fina = {}
            fina['address_details'] = fin['address_details']
            fina['capacity'] = fin['capacity']
            fina['cost'] = fin['cost']
            fina['id'] = ab
            if k % 10 == 0:
                page_count = k / 10

            else:
                page_count = 1 + (k / 10)
        return jsonify({"response": "success", "data": filtered_result,"page_count" : page_count})

    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})



@test.route('/get_sorted_houses', methods=['GET']) #sort by cost
def get_sorted_houses():
   sort_by = request.args.get('sort_by',default="")



   try:

       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           },
               "sort": [
                   {"cost": {"order": "asc"}}
               ]

        }

       result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res:
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/delete_house_by_id', methods=['GET'])
def delete_house_by_id():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else:
        es.delete(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME,id=idp)
        return jsonify({"response": "success", "data": "deleted"})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/get_all_houses', methods=['GET'])
def get_all_houses():
   try:
       house_query = {
           "query": {
               "match_all": {}
           }
       }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res :
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})




@test.route('/get_match_houses', methods=['GET'])
def get_match_houses():
   requestObject=request.args['query']
   try:
       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           }
     }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []

       for x in res :
           fina = x['_source']
           bc =  x['_id']
           fin = {}
           fin['cost'] = fina['cost']
           fin['address'] = fina['address']
           fin['capacity'] = fina['capacity']
           fin['id'] = bc


           filtered_result.append(fin)
       return jsonify({ "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_match_phrase_houses', methods=['GET'])
def get_match_phrase_houses():
   requestObject=request.args['query']
   try:
       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           }
       }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res :
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/get_prefix_phrase_match_houses', methods=['GET'])
def get_prefix_phrase_match_houses():
   requestObject=request.args['query']
   try:
       house_query = {
           "query": {
               "match_phrase_prefix": {
                   "description": requestObject
               }
           }
       }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res :
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_multi_match_houses', methods=['GET'])
def get_multi_match_houses():
   requestObject=request.args['query']
   try:
       house_query = {
           "query": {
               "multi_match": {
                   "query": requestObject,
                   "fields": ["cost", "capacity", "description"]
               }
           }
       }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res :
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})












@test.route('/get_broker', methods=['GET'])
def get_broker():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['broker_info']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_images', methods=['GET'])
def get_images():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['images']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_houses_by_term', methods=['GET'])
def get_houses_by_term():
   requestObject = request.args['query']
   try:
       house_query = {
           "query": {
               "term": {"property_type": requestObject}
           }
       }
       result = es.search(index=ES_DREAMHOUSE_INDEX,doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]


       filtered_result = []
       for x in res :
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_sorted_houses', methods=['GET']) #sort by cost
def get_sorted_houses():
   requestObject = request.args["query"]
   try:
       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           },
               "sort": [
                   {"cost": {"order": "asc"}}
               ]

        }

       result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res:
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/sort_houses_by_date_added', methods=['GET']) #sort by date added
def sort_houses_by_date_added():
   requestObject = request.args["query"]
   try:
       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           },
               "sort": [
                   {"date_added": {"order": "desc"}}
               ]

        }

       result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res:
           fin = x['_source']
           filtered_result.append(fin)
       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/sorted_houses_by_review', methods=['GET']) #sort by review count
def sorted_houses_by_review():
   requestObject = request.args["query"]
   try:
       house_query = {
           "query": {
               "match": {
                   "description": requestObject
               }
           },
               "sort": [
                   {"review_count": {"order": "desc"}}
               ]

        }

       result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
       res = result["hits"]["hits"]
       filtered_result = []
       for x in res:
           fin = x['_source']
           filtered_result.append(fin)

       return jsonify({"response": "success", "data": filtered_result})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/sorted_houses_by_rating', methods=['GET'])  # sort by rating score
def sorted_houses_by_rating():
    requestObject = request.args["query"]
    try:
        house_query = {
            "query": {
                "match": {
                    "description": requestObject
                }
            },
            "sort": [
                {"rating.rating_score": {"order": "desc"}}
            ]

        }

        result = es.search(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, body=house_query)
        res = result["hits"]["hits"]
        filtered_result = []
        for x in res:
            fin = x['_source']
            filtered_result.append(fin)

        return jsonify({"response": "success", "data": filtered_result})

    except Exception as e:
        print str(e)
        return jsonify({"response": "failure", "error": str(e)})






@test.route('/get_cost', methods=['GET'])
def get_cost():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == "false":
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['cost']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})



@test.route('/get_landmark', methods=['GET'])
def get_landmark():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['landmark']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})


@test.route('/get_capacity', methods=['GET'])
def get_capacity():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['capacity']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})




@test.route('/get_address', methods=['GET'])
def get_address():
   idp = request.args["id"]
   try:
       result = es.get(index=ES_DREAMHOUSE_INDEX, doc_type=DREAMHOUSE_DOC_NAME, id=idp)
       print result
       if result["found"] == False:
           return jsonify({"response": "failure", "error": "No house with given id"})
       else :
           result = result['_source']
           return jsonify({"response": "success", "data": result['address']})

   except Exception as e:
       print str(e)
       return jsonify({"response": "failure", "error": str(e)})






























