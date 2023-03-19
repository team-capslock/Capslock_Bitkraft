<?php
/**
* Plugin Name: vTrack
* Plugin URI: https://www.your-site.com/
* Description: Test.
* Version: 0.1
* Author: Capslock
* Author URI: https://www.your-site.com/
**/

add_action('admin_menu', 'my_menu_pages');
function my_menu_pages(){
    add_menu_page('My Page Title', 'Vkart', 'manage_options', 'my-menu', 'home' );
}


// show the page
function home()
{
    include __DIR__.'/pages/dash.php';
}

add_action( 'woocommerce_single_product_summary', 'do_my_thing' );

function do_my_thing() {
    include __DIR__.'/pages/banner.php';
}

function add_cors_headers() {
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Headers: Authorization, Content-Type');
    header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
}

add_action('init', 'add_cors_headers');

function apiUrl(){
    return "https://capslock-bitkraft.vercel.app/";
}

?>