from constants import POST_TYPE_META_FIELDS
import pandas as pd


def convert_post_meta_fields_to_acf_fields(post_type, data_rows):
    new_acf_fields = { 'acf': {} }
    acf_fields = POST_TYPE_META_FIELDS.get(post_type).get('acf_fields')
    for row in data_rows.iterrows():
        old_meta_field = row[1].meta_key
        acf_field_conversion_dict = next((item for item in acf_fields if item['old'] == old_meta_field), None)
        if acf_field_conversion_dict is not None:
            new_meta_field = acf_field_conversion_dict['new']
            if not pd.isna(row[1].meta_value):
                new_acf_fields['acf'][new_meta_field] = row[1].meta_value
                if "image" in acf_field_conversion_dict['old']:
                    if 'fullwidth' in acf_field_conversion_dict['old'] and row[1].meta_value == '1':
                        new_acf_fields['acf'][new_meta_field] = [' '.join([x.capitalize() for x in acf_field_conversion_dict['new'].replace('extra_', "").split('_')])]
                if acf_field_conversion_dict['old'] == 'bocoup-work-redirect-to-live-url' and row[1].meta_value == '1':
                    new_acf_fields['acf'][new_meta_field] = ['Send to Live URL']
    
    return new_acf_fields
        
