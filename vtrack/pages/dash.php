<?php
$store_url = get_bloginfo( 'url' );
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'http://127.0.0.1:8000/api/get-user-level',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => 'url=http%3A%2F%2Fwecare.local%2F',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/x-www-form-urlencoded',
    'Cookie: csrftoken=XW0sN9LTamle7LxulrSxjWVBUScH8AN3zsm33JFul9pJSpG3WIwCpJbsA4sTHQXu'
  ),
));

$response = json_decode(curl_exec($curl));

curl_close($curl);
if($response->val == 0){
    include __DIR__.'/signup.php';
}elseif($response->val == 1){
    include __DIR__.'/sync_products.php';
}else{
    include __DIR__.'/goto.php';
}

?>