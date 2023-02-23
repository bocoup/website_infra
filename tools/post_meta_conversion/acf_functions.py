from constants import POST_TYPE_META_FIELDS


def convert_post_meta_fields_to_acf_fields(post_type, data_rows):
    new_acf_fields = []
    acf_fields = POST_TYPE_META_FIELDS.get(post_type).get("acf_fields")
    for row in data_rows.iterrows():
        x = 4
        # old_meta_field = row.meta_key
        # acf_field_conversion_dict = next((item for item in acf_fields if item["old"] == old_meta_field), None)
        # if acf_field_conversion_dict is not None:
        #     new_meta_field = acf_field_conversion_dict.new
        #     new_acf_fields.append({new_meta_field: row.meta_value})
    
    return new_acf_fields
        
