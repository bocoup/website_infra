<?php
function custom_post_type_work() {
    $labels = array(
        'name'               => _x( 'Works', 'post type general name' ),
        'singular_name'      => _x( 'Work', 'post type singular name' ),
        'add_new'            => _x( 'Add New', 'book' ),
        'add_new_item'       => __( 'Add New Work' ),
        'edit_item'          => __( 'Edit Work' ),
        'new_item'           => __( 'New Work' ),
        'all_items'          => __( 'All Works' ),
        'view_item'          => __( 'View Work' ),
        'search_items'       => __( 'Search Works' ),
        'not_found'          => __( 'No Works found' ),
        'not_found_in_trash' => __( 'No Works found in the Trash' ), 
        'menu_name'          => 'Works'
      );
      $args = array(
        'labels'        => $labels,
        'description'   => 'Holds our Works and Work specific data',
        'public'        => true,
        'menu_position' => 5,
        'supports'      => array( 'title', 'editor', 'thumbnail', 'excerpt', 'comments' ),
        'has_archive'   => true,
        'show_in_rest' => true,
        // 'template_lock' => 'all',
        'template' => array(
            array( 'core/paragraph', array(
                'placeholder' => 'Heading',
            ) ),
            array( 'core/columns', array(), array(
                array( 'core/column', array(), array(
                    array( 'core/paragraph', array(
                        'placeholder' => 'Tagline',
                    ) ),
                ) ),
                array( 'core/column', array(), array(
                    array( 'core/paragraph', array(
                        'placeholder' => 'Lead',
                    ) ),
                ) ),
            ) ),
            array( 'core/columns', array(), array(
                array( 'core/column', array(), array(
                    array( 'core/paragraph', array(
                        'placeholder' => 'Challenge',
                    ) ),
                ) ),
                array( 'core/column', array(), array(
                    array( 'core/paragraph', array(
                        'placeholder' => 'Solution',
                    ) ),
                ) ),
            ) ),
            array( 'core/paragraph', array(
                'placeholder' => 'Impact',
            ) ),
        ),
      );
  register_post_type( 'bocoup_work', $args ); 
}

add_action( 'init', 'custom_post_type_work' );