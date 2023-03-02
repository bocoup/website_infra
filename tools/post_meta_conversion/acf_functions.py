from constants import POST_TYPE_META_FIELDS


def convert_post_meta_fields_to_acf_fields(post_type, data_rows):
    new_acf_fields = { 'acf': {} }
    acf_fields = POST_TYPE_META_FIELDS.get(post_type).get("acf_fields")
    for row in data_rows.iterrows():
        old_meta_field = row[1].meta_key
        acf_field_conversion_dict = next((item for item in acf_fields if item["old"] == old_meta_field), None)
        if acf_field_conversion_dict is not None:
            new_meta_field = acf_field_conversion_dict['new']
            new_acf_fields['acf'][new_meta_field] = row[1].meta_value
    
    return new_acf_fields
        
