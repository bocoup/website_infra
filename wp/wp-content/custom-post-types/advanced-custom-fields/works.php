<?php 

function add_acf_field_group_for_work() {
    
    acf_add_local_field_group(array(
        'show_in_rest' => true,
        'key' => "group_works",
        'title' => 'Works',
        'fields' => array (
            array (
                'key' => 'field_works_meta_description',
                'label' => 'Meta Description',
                'name' => 'meta_description',
                'type' => 'text',
                'default_value' => "Replace me with an SEO description."
            ),
            array (
                'key' => 'field_works_additional_pages',
                'label' => 'Select Optional Additional Pages:',
                'name' => 'optional_additional_pages',
                'type' => 'select',
                'default_value' => null,
                'choices' => array(
                        "home" => "Home",
                        "service" => "Service"
                ),
                'multiple' => true,   
                'allow_null' => true,
            ),
            array (
                'key' => 'field_works_home_description',
                'label' => 'Home Description',
                'name' => 'home_description',
                'type' => 'text',
                'default_value' => "Replace me with a description for the Home Page.",
                'conditional_logic' => array(
                    array(
                        array(
                            'field' => 'field_works_additional_pages',
                            'operator' => '==',
                            'value' => "home"
                        )
                    )
                )
            ),
            array (
                'key' => 'field_works_service_description',
                'label' => 'Service Description',
                'name' => 'service_description',
                'type' => 'text',
                'default_value' => "Replace me with a description for the Service Page.",
                'conditional_logic' => array(
                    array(
                        array(
                            'field' => 'field_works_additional_pages',
                            'operator' => '==',
                            'value' => "service"
                        )
                    )
                )
            ),
        ),
        'location' => array (
            array (
                array (
                    'param' => 'post_type',
                    'operator' => '==',
                    'value' => 'bocoup_work',
                ),
            ),
        ),
    ));
    
}

add_action('acf/init', 'add_acf_field_group_for_work');