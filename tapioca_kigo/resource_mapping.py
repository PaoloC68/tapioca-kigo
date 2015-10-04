# coding: utf-8

RESOURCE_MAPPING = {
    'list_properties': {
        'resource': 'listProperties',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
    },
    'create_confirmed_reservation': {
        'resource': 'createConfirmedReservation',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # params example:
        # {
        #   "PROP_ID" => 1434,
        #   "RES_CHECK_IN" => "2011-07-21",
        #   "RES_CHECK_OUT" => "2011-07-26",
        #   "RES_N_ADULTS" => 2,
        #   "RES_N_CHILDREN" => 1,
        #   "RES_N_BABIES" => 0,
        #   "RES_GUEST" => {
        #     "RES_GUEST_FIRSTNAME" => "Robert",
        #     "RES_GUEST_LASTNAME" => "Roquefort",
        #     "RES_GUEST_EMAIL" => "robert@yahoo.co.uk",
        #     "RES_GUEST_PHONE" => "",
        #     "RES_GUEST_COUNTRY" => "GB"
        #   },
        #   "RES_COMMENT" => "",
        #   "RES_COMMENT_GUEST" => "",
        #   "RES_UDRA" => [
        #     {
        #       "UDRA_ID" => 161,
        #       "UDRA_CHOICE_ID" => 199
        #     },
        #     {
        #       "UDRA_ID" => 162,
        #       "UDRA_TEXT" => "John Smith told me about you!"
        #     }
        #   ]
        # }
    },
    'list_properties_2': {
        'resource': 'listProperties2',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
    },
    'read_property': {
        'resource': 'readProperty',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { 'PROP_ID' : property_id }
    },
    'read_property_2': {
        'resource': 'readProperty2',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { 'PROP_ID' : property_id }
    },
    'read_property_photo_file': {
        'resource': 'readPropertyPhotoFile',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { "PROP_ID" : property_id, "PHOTO_ID" : photo_id }
    },
    'read_property_pricing_setup': {
        'resource': 'readPropertyPricingSetup',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { 'PROP_ID' : property_id }
    },
    'calendar_reservations': {
        'resource': 'diffPropertyCalendarReservations',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { 'DIFF_ID' : diff_id }
    },
    'read_reservation': {
        'resource': 'readReservation',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # { 'RES_ID' : res_id }
    },
    'compute_pricing': {
        'resource': 'computePricing',
        'docs': 'https://support.kigo.net/entries/23581401-RA-REST-API-v1-specification',
        "methods": [
            "POST",
         ]
        # Please note that the method does not verify the availability of the property for the specified dates,
        # { 'PROP_ID' : property_id }
        # { 'RES_CREATE' : res_date }
        # { 'RES_CHECK_IN' : check_in }
        # { 'RES_CHECK_OUT' : check_out }
        # { 'RES_N_ADULTS' : adults }
        # { 'RES_N_CHILDREN' : children }
        # { 'RES_N_BABIES' : babies }
    },

}
